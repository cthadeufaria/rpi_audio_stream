import socket
import struct
import asyncio
import opuslib
import sounddevice as sd
import numpy as np



class UDPClient:
    def __init__(self, multicast_group, port=12345):
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.bind(('', self.port))
        group = socket.inet_aton(multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        self.client_socket.setblocking(False)
        self.BUFFER_SIZE = 1024
        self.SAMPLE_RATE = 48000
        self.CHANNELS = 1
        self.CHUNK_SIZE = 960
        self.decoder = opuslib.Decoder(self.SAMPLE_RATE, self.CHANNELS)

    async def listen_to_voice(self):
        loop = asyncio.get_event_loop()
        print("Listening to voice...")

        with sd.OutputStream(samplerate=self.SAMPLE_RATE, channels=self.CHANNELS, dtype='int16') as stream:
            while True:
                try:
                    data = await loop.sock_recv(self.client_socket, self.BUFFER_SIZE)
                    decoded_audio = self.decoder.decode(data, self.CHUNK_SIZE)
                    audio_array = np.frombuffer(decoded_audio, dtype=np.int16)
                    stream.write(audio_array) # TODO: clear white noise from audio.
                    await asyncio.sleep(0.001)
                
                except BlockingIOError:
                    await asyncio.sleep(0.1)

                except asyncio.CancelledError:
                    break

    async def listen_for_discovery(self): # TODO: test dynamic discovery in different devices.
        loop = asyncio.get_event_loop()
        while True:
            data = await loop.sock_recv(self.client_socket, self.BUFFER_SIZE)
            print("Data received.", data.decode())

            if data:
                print("Data received.", data.decode())
                return data.decode()
import socket
import asyncio
import opuslib
from voice import Voice



class UDPServer:
    def __init__(self, role, port=12345):
        self.role = role
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 3)
        self.server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
        self.SAMPLE_RATE = 48000
        self.CHANNELS = 1
        self.CHUNK_SIZE = 960
        self.encoder = opuslib.Encoder(self.SAMPLE_RATE, self.CHANNELS, opuslib.APPLICATION_VOIP)
        self.voice = Voice(self.SAMPLE_RATE, self.CHANNELS, self.CHUNK_SIZE)
        self.connections = set()

    async def broadcast_voice(self, button, multicast_group):
        # group = (multicast_group, self.port)
        group = ('127.0.0.1', self.port)
        
        async for audio_data in self.voice.capture():
            if not button.streaming:
                print("Voice transmission stopped.")
                break
            encoded_data = self.encoder.encode(audio_data, self.CHUNK_SIZE)
            self.server_socket.sendto(encoded_data, group)            
            await asyncio.sleep(0.01)

    async def send_discovery_packet(self, message):
        # broadcast_group = ('255.255.255.255', self.port)
        broadcast_group = ('127.0.0.1', self.port)
    
        while True:
            self.server_socket.sendto(message.encode(), broadcast_group)
            print("Discovery packet sent.", message)
            await asyncio.sleep(10)
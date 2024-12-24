import sounddevice as sd
import numpy as np
import asyncio



class Voice:
    def __init__(self, sample_rate, channels, chunk_size):
        self.speaking = False
        self.SAMPLE_RATE = sample_rate
        self.CHANNELS = channels
        self.CHUNK_SIZE = chunk_size

    async def capture(self):
        loop = asyncio.get_event_loop()
        queue = asyncio.Queue()

        def audio_callback(indata, frames, time, status):
            try:
                audio_data = np.reshape(indata, (frames * self.CHANNELS,)).astype(np.int16).tobytes()
                loop.call_soon_threadsafe(queue.put_nowait, audio_data)
            except Exception as e:
                print(f"Error encoding audio data: {e}")

        with sd.InputStream(
            samplerate=self.SAMPLE_RATE, 
            channels=self.CHANNELS, 
            callback=audio_callback,
            blocksize=self.CHUNK_SIZE,
            dtype='int16'
        ):
            while True:
                encoded_data = await queue.get()
                yield encoded_data
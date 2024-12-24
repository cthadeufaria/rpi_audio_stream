import sounddevice as sd
# TODO: implement player class for better separation of concerns. Detach playing audio functionality from client/udp.py.



class Player:
    def __init__(self, sample_rate=48000, channels=2, chunk_size=960):
        self.SAMPLE_RATE = sample_rate
        self.CHANNELS = channels
        self.CHUNK_SIZE = chunk_size

    
import websockets
import json
import pygame
import asyncio



class WebSocketClient:
    def __init__(self, uri):
        self.uri = uri
        self.connected = False
        self.tries = 0

    async def connect(self):
        while not self.connected or self.tries > 30:
            try:
                async with websockets.connect(self.uri) as websocket:
                    print("Connected to WebSocket server")
                    self.connected = True
                    await self.listen(websocket)
            except (ConnectionRefusedError, OSError) as e:
                print(f"Connection failed: {e}. Retrying...")
                await asyncio.sleep(1)
                self.tries += 1

    async def listen(self, websocket):
        try:
            async for message in websocket:
                data = json.loads(message)
                command = data.get("command")
                if command == "play":
                    playlist = data.get("playlist")
                    for music in playlist:
                        if music == "bell/bell.mp3":
                            print("Playing bell sound.")
                            file = music
                        else:
                            file = music.split("/")[-1] # TODO: make this work also in windows os.
                        print(f"Playing MP3 file: {file}")
                        pygame.mixer.init()
                        sound = pygame.mixer.Sound('../mp3/' + file)
                        playing = sound.play()
                        while playing.get_busy():
                            if not file:
                                print("no file", file)
                                playing.stop()
                                break
                            elif command == "stop":
                                print("command stop", command)
                                if playing:
                                    playing.stop()
                                    break
                            await asyncio.sleep(1)
                
        except websockets.exceptions.ConnectionClosed as e:
            print(f"Disconnected from server: {e}")
            self.connected = False
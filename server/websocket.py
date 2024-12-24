import asyncio
import websockets
import socket
import requests



class WebSocketServer:
    def __init__(self, port=9999, role='head_master'):
        self.host = self.get_ip()[0]
        self.port = port
        self.role = role
        self.connected_clients = set()

    async def handler(self, websocket, path):
        self.connected_clients.add(websocket)
        try:
            async for message in websocket:
                print(f"Received message from client: {message}")
        except websockets.exceptions.ConnectionClosed as e:
            print(f"Client disconnected: {e}")
        finally:
            self.connected_clients.remove(websocket)

    async def send_message_to_all(self, message):
        tasks = [client.send(message) for client in self.connected_clients]
        if tasks:
            await asyncio.gather(*tasks)

    async def send_message_to_client(self, client, message):
        if client in self.connected_clients:
            await client.send(message)

    async def main(self):
        async with websockets.serve(self.handler, self.host, self.port):
            print(f"WebSocket server running on {self.host}:{self.port}")
            await asyncio.Future()
    
    async def broadcast_voice(self, voice):
        for client in self.connected_clients:
            await client.send(voice)

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while True:
            try:
                s.connect(("8.8.8.8", 80))
                local_ip = s.getsockname()[0]
                public_ip = requests.get('https://api.ipify.org?format=json').json()['ip']
            finally:
                s.close()
                return local_ip, public_ip       

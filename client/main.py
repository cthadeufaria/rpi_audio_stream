import asyncio
from websocket import WebSocketClient
from udp import UDPClient



async def discover_server(udp_client):
    address = await udp_client.listen_for_discovery()
    return address

async def main(): # TODO: handle real connection scenario and cath errors gracefully.
    udp_client = UDPClient(multicast_group='224.0.0.1')
    hostname = await discover_server(udp_client)
    # hostname = "192.168.1.108"
    websocket_client = WebSocketClient(uri=f"ws://{hostname}:9999")
    
    websocket_task = asyncio.create_task(websocket_client.connect())
    udp_task = asyncio.create_task(udp_client.listen_to_voice())
    
    while True:
        try:
            await asyncio.gather(
                websocket_task, 
                udp_task
            )
        except Exception as e:
            await asyncio.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(main())
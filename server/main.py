import asyncio
import json
from udp import UDPServer
from websocket import WebSocketServer
from gui import GUI



async def handle_websocket(server):
    await server.main()

async def handle_bell_and_music(server, button):
    """Handles playing bell or music based on button state."""
    while True: # TODO: play what pc is playing
        playlist = ["bell/bell.mp3"] if button.ringing else button.playlist if button.playing else None
        if playlist and server: # TODO: stop music when button pressed.
            message = json.dumps({"command": "play", "playlist": playlist})
            await server.send_message_to_all(message)
            print("Data sent to clients.")
            if button.ringing:
                button.stop_bell()
            if button.playing:
                button.stop_music()
        if button.stopped:
            message = json.dumps({"command": "stop"})
            await server.send_message_to_all(message)
            print("Stop.")
            button.on()
        await asyncio.sleep(1)

async def handle_voice_transmission(udp_server, button):
    """Handles voice transmission over UDP when button is pressed."""
    while True:
        if button.streaming:
            print("button_streaming", button.streaming)
            await udp_server.broadcast_voice(button, "224.0.0.1") # TODO: what if 2 microfones wanna speak at the same time? Give priority to head master role.
        await asyncio.sleep(1)

async def handle_gui(gui):
    await gui.draw()

async def handle_self_discovery(udp_server, host):
    await udp_server.send_discovery_packet(host)

async def main(): # TODO: handle real connection scenario and catch errors gracefully.
    server = WebSocketServer(role="head_master")
    udp_server = UDPServer(role="head_master") # TODO: make multicast_group dynamic. # TODO: acknowledge before voice transmission to make sure message is sent over unreliable network conditions.
    gui = GUI()

    await asyncio.gather(
        handle_websocket(server),
        handle_bell_and_music(server, gui),
        handle_voice_transmission(udp_server, gui),
        handle_gui(gui),
        handle_self_discovery(udp_server, server.host)
    )


if __name__ == "__main__":
    while True:
        asyncio.run(main())
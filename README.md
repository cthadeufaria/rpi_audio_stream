# rpi_audio_stream

# Sprints?

# Project development steps/tasks
# Hardware requirements gathering 6-8
# Client
    MAX98357A  2EUR
    Raspberry Pi Zero 2 WH 19EUR
        estimate client ram needs
    Rpi box 6EUR
    battery connection 20EUR
        or common power supply - 10EUR
    if we have to connect to wifi, then lcd display 15EUR
    SD card 32GB 5EUR
# Server is pc

# Communication protocol setup 10-12
    implement communications protocol connections and callbacks [ok]
    handle real scenario connection and setup
        dynamic connection using udp [ONGOING]

# Server/Client development 15-18 + 12-15
    implement core classes [ok]
    implement assynchronous handling of connections/inputs/outputs [ok]
    implement song selection for music [ok]
    implement white noise treatment
    handle microphone priority [ONGOING]
    handle real scenario connection and setup 
        handle errors and reconnection gracefully [ONGOING]
    Handle messages to specific addresses or groups [ONGOING]

# UI/Control Interface	6-8
    ui for server user on tkinter [ONGOING]
        3 button for controlling playbacks
        buttons status
        wifi connection
        wifi status
        print important messages for user
        selection for broadcast or message to specific address or group

# RPi Environment Setup	5-6
    install rpi operational system
    install rpi client software
        automate set up and initialization configuration
    create installation binary for server
        run on pc
    how to cryptograph so the software binary will not be decompiled?

# Testing and Debugging	10-12

# Documentation and Training	5-7


## Questions I need to answer:
How to select songs?
How to handle multiple microfones at the same time?
How to select specific client on gui?
    When client connects, warn on gui and select its group str.

# Backlog
Requirements Gathering	6-8
2 microfones
DAC pro or DAC+? https://www.raspberrypi.com/documentation/accessories/audio.html#overview
if there's a power break, battery needed

Communication Protocol Setup	10-12
what protocol for (mp3 playing and breaking sound) or (orders to send to play the sounds saved on rpi)
	quality for music and clear for speech
	address a specific client for streaming
    Answer: UDP for voice and websockets for play instructions !!!
    Answer: Set up WireGuard for connection between private networks

UI/Control Interface	6-8
ui for server user - tkinter
server must select broadcast or specific address or group

RPi Environment Setup	5-6
connect with Wireguard
how to protect so not to be decompiled the software?

Server/Client Development	15-18 + 12-15
class diagram
class implementation
    servers:
        1 head master 
        1 secreteary
    server needs to broadcast live streaming mp3 files to evreyone
    server should play breaking sound (siren or something more enjoyable)
    server must send microfone audio to everyone or to specific client
    clients must listen anything addressed to them


Testing and Debugging	10-12

Documentation and Training	5-7


# TODO: answer following Manesh questions 
- UPDATE BACKLOG []

!!!!!!
- deliver first test [ ]
    - make static ip solution for one simple client server implementation
!!!!!!


####
- check MQTT feasibility for voice [ok]
	- 384 Kbit/s is minimum voice quality []
	- check how to implement mesh network qith MQTT
	- check maximum distance on wifi ad-hoc for mqtt physical layer / if wifi not good than other options
- send products to buy already listed [ok]
- search dac for the pi 5 [ok]
	- write explanation about i2s interface [ok]
- check sd card compatibility [ok]
- deliver first sprint [ok]
	- do simple gui with button [ok]
	- play bell ring message [ok]

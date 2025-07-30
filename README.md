# rpi_audio_stream

A Raspberry Pi–based audio streaming system with a PC server and multiple Raspberry Pi Zero 2 WH clients. The project enables music playback, white noise generation, and microphone priority handling, with communication over UDP.  

---

## 📋 Overview

This project implements a server-client audio streaming system where:  
- **Server** runs on a PC, controlling playback, device management, and group messaging.  
- **Clients** are Raspberry Pi Zero 2 WH devices equipped with audio hardware, capable of playing music, white noise, or microphone audio.  

Communication is handled over UDP, with support for broadcast and targeted messages.  

---

## 🔧 Hardware Requirements

### Client Hardware
| Component                            | Cost (EUR) |
|--------------------------------------|------------|
| Raspberry Pi Zero 2 WH               | 19         |
| MAX98357A Audio Amplifier            | 2          |
| RPi enclosure                        | 6          |
| Power supply / Battery connection    | 20 (Battery) / 10 (Common PSU) |
| Optional LCD (for WiFi status/config)| 15         |
| microSD Card (32GB)                  | 5          |

**Estimated client RAM requirements:** *TBD based on software footprint.*

**Server Hardware:**  
- Standard PC (runs the server application)

---

## 📡 Communication Protocol

**Goal:** Dynamic UDP-based communication between server and clients.  
- ✅ Protocol connections & callbacks implemented  
- 🔄 Dynamic connection setup in real scenarios (**Ongoing**)  

---

## 🛠 Development Roadmap

### **Server & Client Development**  
- ✅ Implement core classes  
- ✅ Asynchronous handling of connections, inputs, outputs  
- ✅ Song selection for music playback  
- ✅ White noise treatment (*basic*)  
- 🔄 Microphone priority handling  
- 🔄 Real scenario connection setup (error handling & graceful reconnections)  
- 🔄 Message routing to specific addresses or groups  

### **UI / Control Interface**  
- **Server UI** (Tkinter-based) – *Ongoing*  
  - Control playback (3 buttons)  
  - Show button status  
  - Manage WiFi connection & status  
  - Display important system messages  
  - Select between broadcast or targeted messages  

### **RPi Environment Setup**  
- Install Raspberry Pi OS  
- Install & configure RPi client software  
  - Automate setup & initialization  
- Create installation binary for server (PC)  
- **Security consideration:** Evaluate cryptographic protection to prevent binary reverse engineering  

---

## 🚀 Installation

### **Server**
```bash
# Clone the repository
git clone https://github.com/<your-username>/rpi_audio_stream.git
cd rpi_audio_stream/server

# (Instructions to build & run server binary here)

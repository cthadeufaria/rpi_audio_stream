from tkinter import filedialog
from os import path



class Button:
    def __init__(self):
        self.ringing = False
        self.streaming = False
        self.playing = False
        self.stopped = False

    def ring_bell(self):
        self.ringing = True
        print("Bell ringing.", self.ringing)
    
    def toggle_voice(self):
        self.streaming = not self.streaming
        print("Voice transmission started." if self.streaming else "Voice transmission stopped.")

    def on(self):
        self.stopped = False

    def off(self):
        self.stopped = True

    def stop_music(self):
        self.playing = False
        print("Music stopped.")

    def stop_bell(self):
        self.ringing = False
        print("Bell stopped.")

    def play_selected(self):
        self.song_selection()
        self.playing = True

    def song_selection(self):
        initial_directory = path.abspath(path.join(path.dirname(__file__), "../mp3"))
        self.playlist = filedialog.askopenfilenames(
            initialdir= initial_directory,
            # filetypes=[("Audio Files", "*.mp3")],
        )
        print("Playlist selected:", self.playlist)
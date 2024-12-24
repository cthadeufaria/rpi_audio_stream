from tkinter import * 
import asyncio
from button import Button as B



class GUI(B):
    def __init__(self):
        super().__init__()

        self.window = Tk()
        self.window.title("Server Control Panel")
        self.window.geometry("500x200")
        
        self.voice_button = Button(self.window, text="Voice", command=self.toggle_voice)
        self.voice_button.grid(row=0, column=0)
        self.bell_button = Button(self.window, text="Bell", command=self.ring_bell)
        self.bell_button.grid(row=0, column=1)
        self.music_button = Button(self.window, text="Music Selection", command=self.play_selected)
        self.music_button.grid(row=0, column=2)
        self.stop_button = Button(self.window, text="Stop Music", command=self.off)
        self.stop_button.grid(row=0, column=3)

    async def update_gui(self):
        """Asynchronous Tkinter GUI update loop."""
        while True:
            self.window.update()
            await asyncio.sleep(0.01)

    async def draw(self):
        await self.update_gui()


# if __name__ == "__main__":
#     gui = GUI()
#     asyncio.run(gui.draw())
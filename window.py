#!/usr/bin/python3

from tkinter import *
from PIL import Image, ImageTk

# sudo apt-get install python3-tk
# sudo apt-get install python-imaging-tk
# ^- ignore sudo apt-get install python3-pil.imagetk
class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master
        self.init_window()
        
    def init_window(self):
        
        self.master.title("Braille Viewer")
        
        # self.bind("<Button-1>", click_call)
        self.pack(fill=BOTH, expand=1)
        
        # quitButton = Button(self, text="Quit")
        
        quitButton = Button(self, text="Quit", command=self.client_exit)
        
        quitButton.place(x=0, y=0)
    
    def show_image(self, image):
        render = ImageTk.PhotoImage(image)
        img = Label(self, image=render)
        img.bind("<Button-1>", click_call)
        img.image = render
        img.place(x=0, y=0)
    
    def client_exit(self):
        exit()
        
def click_call(event):
    print(f"clicked at {event.x} {event.y}")

def start_app():
    root = Tk()
    root.geometry("1000x700")
    app = Window(root)

    greyscale_dog = Image.open('greyscale_dog.png')
    
    app.show_image(greyscale_dog)

    root.mainloop()
    
start_app()
#!/usr/bin/python3

from tkinter import *
from PIL import Image, ImageTk
from ourYolo_opencv import processImage
import os
import numpy as np
import cv2
from gtts import gTTS
# from text2voice import TextToVoice
# from win32com.client import Dispatch

fileNames = []

directory = os.fsencode("images")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    fileNames.append(filename)

global images
global currentImage
global app

images = []

currentImage = 0

for path in fileNames:
    images.append(processImage("images/" + path))

print(images)

# sudo apt-get install python3-tk
# sudo apt-get install python-imaging-tk
# ^- ignore sudo apt-get install python3-pil.imagetk
class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master
        self.init_window()
        self.img = None
        
    def init_window(self):
        
        self.master.title("Braille Viewer")
        self.master.bind("<Key>", key_call)
        # self.bind("<Button-1>", click_call)
        self.pack(fill=BOTH, expand=1)
        
        # quitButton = Button(self, text="Quit")
        
        quitButton = Button(self, text="Quit", command=self.client_exit)
        
        quitButton.place(x=0, y=0)
    
    def show_image(self, image):
        if self.img != None:
            self.img.destroy()
        
        render = ImageTk.PhotoImage(image)
        self.img = Label(self, image=render)
        self.img.bind("<Button-1>", click_call)
        self.master.bind("<Key>", key_call)
        self.img.image = render
        self.img.place(x=0, y=0)
    
    def client_exit(self):
        exit()
        
def click_call(event):
    print(f"clicked at {event.x} {event.y}")
    say_name(event.x, event.y)

def key_call(event):
    global currentImage
    global images
    global app

    print(f"key Press: {repr(event.char) == 'a'}")
    if str(event.char) == 'a':
        print ("aaaa")
        if currentImage != 0:
            print ("ddqddwq")
            currentImage -= 1 
            image = images[currentImage]['image']
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(image)
            app.show_image(img_pil)

    elif str(event.char) == 'z':
        print("ccccc")
        if currentImage != len(images) - 1:
            print("ddddddddd")
            currentImage += 1
            image = images[currentImage]['image']
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(image)
            app.show_image(img_pil)

def say_name(x, y):

    global images
    global currentImage

    imageData = images[currentImage]['data']

    for object in imageData:
        print(f"label: {object['label']} x: {object['x']} y: {object['y']} w: {object['x_plus_w']} h: {object['y_plus_h']}")
        if x >= object['x'] and x <= object['x_plus_w'] and y >= object['y'] and y <= object['y_plus_h']:
            print(f"{object['label']}")
            # t = TextToVoice(object['label'])
            # t.text2voice()
            
            myobj = gTTS(text=object['label'], lang='en', slow=False)

            myobj.save(object['label'].replace(" ", "_") + ".mp3")
            os.system("mpg123 " + object['label'].replace(" ", "_") + ".mp3")
            return

def start_app():
    global app
    global images

    root = Tk()
    root.geometry("1000x700")
    app = Window(root)

    # results = processImage('street.jpg')
    image = images[0]['image']
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(image)

    app.show_image(img_pil)

    root.mainloop()
    
start_app()
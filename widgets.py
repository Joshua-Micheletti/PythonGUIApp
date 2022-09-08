from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter import LEFT
from tkinter import RIGHT
from frames import *
from app import *

widgets = NULL
downloadIcon = NULL

def clickFunction():
    print("clicked!")

def loadWidgets(frames):
    global widgets
    global downloadIcon

    widgets = dict()

    # NORMAL BUTTON
    button = Button(
        frames["first"],
        text = "Click Me",
        command = clickFunction
    )
    button.state(["!disabled"])
    button.pack()
    widgets["button"] = button

    downloadIcon = PhotoImage(file = "./data/download.png")

    # IMAGE BUTTON
    imageButton = Button(
        frames["first"],
        image = downloadIcon,
        command = clickFunction
    )
    imageButton.pack()
    widgets["imageButton"] = imageButton

    # COMPOUND IMAGE + TEXT BUTTONS
    compoundButton = Button(
        frames["first"],
        image = downloadIcon,
        text = "Download",
        compound = LEFT,
        command = clickFunction
    )
    compoundButton.pack()
    widgets["compoundButton"] = compoundButton

    compoundButtonRight = Button(
        frames["first"],
        image = downloadIcon,
        text = "Download",
        compound = RIGHT,
        command = clickFunction
    )
    compoundButtonRight.pack()
    widgets["compoundButtonRight"] = compoundButtonRight



    
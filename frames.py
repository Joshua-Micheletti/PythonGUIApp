from app import *
from widgets import *
from tkinter.ttk import *

def loadFrames(window):
    frames = dict()

    frame = Frame(window)
    frame["padding"] = (20, 20)
    frame["relief"] = "sunken" # flat, raised, sunken, groove, ridge
    frame["cursor"] = "arrow" # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
    frame.pack()

    frames["first"] = frame

    return(frames)

    

    
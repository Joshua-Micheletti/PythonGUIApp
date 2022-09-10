from tkinter import *
from widgets import *
from frames import *
from style import *
from ttkthemes import ThemedTk

window = None

def closeProgram(event):
    global window
    window.destroy()

def main():
    global window

    window = ThemedTk()                     # create the window
    window.geometry("1280x720")             # "1280x720+offsetx+offsety"
    window.title("GUI App")                 # set the window name
    window.resizable(TRUE, TRUE)            # resizable width and height
    window.minsize(400, 400)                # min resize dimensions
    window.maxsize(1920, 1080)              # max resize dimensions
    window.attributes('-alpha', 1)          # opacity
    #window.attributes('-topmost', 1)       # window always on top
    window.iconphoto(False, PhotoImage(file = './data/icon.png')) # load the icon
    window.bind('<Escape>', closeProgram)   # bind the escape button to close the program

    loadStyle(window)

    loadWidgets(loadFrames(window), window) # load the frames and the widgets

    window.mainloop()                       # run the app

if __name__ == "__main__":
    main()
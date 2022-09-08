from asyncio.windows_events import NULL
from tkinter import *
import tkinter.ttk as ttk
from widgets import *
from frames import *

window = NULL

def main():
    global window

    window = Tk()
    window.geometry("1280x720") # "1280x720+offsetx+offsety"
    window.title("GUI App")
    window.resizable(TRUE, TRUE) # width height
    window.minsize(400, 400)
    window.maxsize(1920, 1080)
    window.attributes('-alpha', 1)
    #window.attributes('-topmost', 1)
    window.iconbitmap("./data/icon.ico")

    loadWidgets(loadFrames(window))

    window.mainloop()

if __name__ == "__main__":
    main()
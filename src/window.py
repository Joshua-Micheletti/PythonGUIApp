from tkinter import *
from ttkthemes import ThemedTk

from shared import *
from style import *

# function to call when the window gets closed
def closeWindowCallback(event):
    getWindow().destroy()
    
def closeWindowWM():
    getWindow().destroy()

# function to create a window
def createWindow(title = "GUI App", width = 1280, height = 720, offsetX = 0, offsetY = 0, resizeX = TRUE, resizeY = TRUE, minResizeX = 400, minResizeY = 400, maxResizeX = 1920, maxResizeY = 1080, alpha = 1, icon = ""):
    window = getWindow()

    window = ThemedTk()                     # create the window
    window.geometry(str(width) + "x" + str(height) + "+" + str(offsetX) + "+" + str(offsetY)) # "1280x720+offsetx+offsety"
    window.title(title)                    # set the window name
    window.resizable(resizeX, resizeY)     # resizable width and height
    window.minsize(minResizeX, minResizeY) # min resize dimensions
    window.maxsize(maxResizeX, maxResizeY) # max resize dimensions
    window.attributes('-alpha', alpha)     # opacity
    #window.attributes('-topmost', 1)      # window always on top
    if icon != "":
        window.iconphoto(False, PhotoImage(file = icon)) # load the icon
        
    window.bind('<Escape>', closeWindowCallback)   # bind the escape button to close the program
    window.protocol("WM_DELETE_WINDOW", closeWindowWM)
    
    loadStyle(window)
    setWindow(window)

    return(window)

from app import *
from widgets import *
from tkinter.ttk import *

def loadFrames(window):
    frames = dict()

    window.columnconfigure(0, weight = 2)
    window.columnconfigure(1, weight = 2)
    window.columnconfigure(2, weight = 2)
    window.rowconfigure(0, weight = 0)
    #window.columnconfigure(3, weight = 2)

    buttons = LabelFrame(window)
    buttons["padding"] = (20, 20)
    buttons["relief"] = "sunken" # flat, raised, sunken, groove, ridge
    buttons["cursor"] = "arrow" # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
    buttons["text"] = "Buttons" # specifies the text of the labelframe
    buttons["labelanchor"] = "nw" # specifies the position of the label in the labelframe
    buttons.grid(column = 0, row = 0, sticky="nsew")

    frames["buttons"] = buttons

    checkboxes = LabelFrame(window)
    checkboxes["padding"] = (20, 20)
    checkboxes["relief"] = "sunken"
    checkboxes["cursor"] = "arrow"
    checkboxes["text"] = "Checkboxes"
    checkboxes["labelanchor"] = "n"
    checkboxes.grid(column = 1, row = 0, sticky="nsew")

    frames["checkboxes"] = checkboxes

    entries = LabelFrame(window)
    entries["padding"] = (20, 20)
    entries["relief"] = "sunken"
    entries["cursor"] = "arrow"
    entries["text"] = "Entries"
    entries["labelanchor"] = "ne"
    entries.grid(column = 2, row = 0, sticky = "nsew")

    frames["entries"] = entries

    styles = LabelFrame(window)
    styles["padding"] = (20, 20)
    styles["relief"] = "sunken"
    styles["cursor"] = "arrow"
    styles["text"] = "Styles"
    styles["labelanchor"] = "w"
    styles.grid(column = 0, row = 1, sticky = "nsew")

    frames["styles"] = styles

    labels = LabelFrame(window)
    labels["padding"] = (20, 20)
    labels["relief"] = "sunken"
    labels["cursor"] = "arrow"
    labels["text"] = "Labels"
    labels["labelanchor"] = "n"
    labels.grid(column = 1, row = 1, sticky = "nsew")

    frames["labels"] = labels

    return(frames)

    

    
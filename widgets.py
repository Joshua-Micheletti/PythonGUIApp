from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter import LEFT
from tkinter import RIGHT
from tkinter import StringVar
from frames import *

widgets = dict()
downloadIcon = None
strings = dict()

def clickFunction():
    print("clicked!")

def clickFunctionWithArgs(args):
    print(args)

def checked():
    global strings
    print("checked: " + strings["checkbox"].get())

def entryCallback(*args):
    print(strings[args[0]].get())

def changeTheme(theme, window):
    print(theme)
    style = Style(window)
    style.theme_use(theme)



def loadWidgets(frames, window):
    loadButtons(frames["buttons"])
    loadCheckboxes(frames["checkboxes"])
    loadEntries(frames["entries"])
    loadStyles(frames["styles"], window)


def loadButtons(frame):
    global widgets
    global downloadIcon

    # NORMAL BUTTON
    button = Button(
        frame,
        text = "Click Me",
        command = clickFunction
    )
    button.state(["!disabled"])
    button.pack(pady = 5)
    widgets["button"] = button

    downloadIcon = PhotoImage(file = "./data/download.png")

    # IMAGE BUTTON
    imageButton = Button(
        frame,
        image = downloadIcon,
        command = clickFunction
    )
    imageButton.pack(pady = 5)
    widgets["imageButton"] = imageButton

    # COMPOUND IMAGE + TEXT BUTTONS
    compoundButton = Button(
        frame,
        image = downloadIcon,
        text = "Download",
        compound = LEFT,
        command = clickFunction
    )
    compoundButton.pack(pady = 5)
    widgets["compoundButton"] = compoundButton

    compoundButtonRight = Button(
        frame,
        image = downloadIcon,
        text = "Download",
        compound = RIGHT,
        command = clickFunction
    )
    compoundButtonRight.pack(pady = 5)
    widgets["compoundButtonRight"] = compoundButtonRight

    # BUTTON WITH CALLBACK ARGUMENTS
    argumentButton = Button(
        frame,
        text = "Print this string",
        command = lambda: clickFunctionWithArgs("this string")
    )
    argumentButton.pack(pady = 5)
    widgets["argumentButton"] = argumentButton


def loadCheckboxes(frame):
    global strings
    global widgets

    strings["checkbox"] = StringVar(name = "checkbox")

    checkbox = Checkbutton(
        frame,
        text = "Checkbox",
        command = checked,
        variable = strings["checkbox"],
        onvalue = "True",
        offvalue = "False"
    )
    checkbox.pack()
    widgets["checkbox"] = checkbox


def loadEntries(frame):
    global widgets
    global strings

    entryLabel = Label(
        frame,
        text = "Input"
    )
    strings["entry"] = StringVar(name = "entry")
    strings["entry"].trace('w', entryCallback)
    entry = Entry(
        frame,
        textvariable = strings["entry"],
    )
    entryLabel.pack()
    entry.pack(pady = (0, 5))
    entry.focus()
    widgets["entry"] = entry
    widgets["entryLabel"] = entryLabel

    passwordLabel = Label(
        frame,
        text = "Password"
    )
    strings["password"] = StringVar(name = "password")
    strings["password"].trace('w', entryCallback)
    password = Entry(
        frame,
        textvariable = strings["password"],
        show = '*'
    )
    passwordLabel.pack()
    password.pack(pady = (0, 5))
    widgets["password"] = password


def loadStyles(frame, window):
    style = Style(window)

    for i in range(len(style.theme_names())):
        #theme = style.theme_names()[i]
        button = Button(
            frame,
            text = style.theme_names()[i],
            command = lambda theme = style.theme_names()[i], window = window: changeTheme(theme, window),
        ).pack()

        widgets["styleButton" + str(i)] = button
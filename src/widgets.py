from tkinter.ttk import *
from tkinter import PhotoImage
from tkinter import StringVar
from frames import *
from shared import *

downloadIcon = None

def clickFunction():
    print("clicked!")

def clickFunctionWithArgs(args):
    print(args)

def checked():
    print("checked: " + getStrings()["checkbox"].get())

def entryCallback(*args):
    print(getStrings()[args[0]].get())

def changeTheme(theme):
    print(theme)
    getWindow().set_theme(theme)



def loadWidgets(frames):
    if "buttons" in frames:
        loadButtons(frames["buttons"])
    if "checkboxes" in frames:
        loadCheckboxes(frames["checkboxes"])
    if "entries" in frames:
        loadEntries(frames["entries"])
    if "styles" in frames:
        loadStyles(frames["styles"])
    if "labels" in frames:
        loadLabels(frames["labels"])


def loadButtons(frame):
    global downloadIcon

    # NORMAL BUTTON
    button = Button(
        frame,
        text = "Click Me",
        command = clickFunction
    )
    button.state(["!disabled"])
    button.pack(pady = 5)
    getWidgets()["button"] = button

    downloadIcon = PhotoImage(file = "./data/download.png")

    # IMAGE BUTTON
    imageButton = Button(
        frame,
        image = downloadIcon,
        command = clickFunction
    )
    imageButton.pack(pady = 5)
    getWidgets()["imageButton"] = imageButton

    # COMPOUND IMAGE + TEXT BUTTONS
    compoundFrame = Frame(frame)
    compoundFrame.pack()

    compoundButton = Button(
        compoundFrame,
        image = downloadIcon,
        text = "Download",
        compound = "left",
        command = clickFunction
    )
    compoundButton.grid(row = 0, column = 0, pady = 5, padx = 5)
    getWidgets()["compoundButton"] = compoundButton

    compoundButtonRight = Button(
        compoundFrame,
        image = downloadIcon,
        text = "Download",
        compound = "right",
        command = clickFunction
    )
    compoundButtonRight.grid(row = 0, column = 1, pady = 5, padx = 5)
    getWidgets()["compoundButtonRight"] = compoundButtonRight

    # BUTTON WITH CALLBACK ARGUMENTS
    argumentButton = Button(
        frame,
        text = "Print this string",
        command = lambda: clickFunctionWithArgs("this string")
    )
    argumentButton.pack(pady = 5)
    getWidgets()["argumentButton"] = argumentButton


def loadCheckboxes(frame):
    getStrings()["checkbox"] = StringVar(name = "checkbox")

    checkbox = Checkbutton(
        frame,
        text = "Checkbox",
        command = checked,
        variable = getStrings()["checkbox"],
        onvalue = "True",
        offvalue = "False"
    )
    checkbox.pack()
    getWidgets()["checkbox"] = checkbox


def loadEntries(frame):
    entryLabel = Label(
        frame,
        text = "Input"
    )
    getStrings()["entry"] = StringVar(name = "entry")
    getStrings()["entry"].trace('w', entryCallback)
    entry = Entry(
        frame,
        textvariable = getStrings()["entry"],
    )
    entryLabel.pack()
    entry.pack(pady = (0, 5))
    entry.focus()
    getWidgets()["entry"] = entry
    getWidgets()["entryLabel"] = entryLabel

    passwordLabel = Label(
        frame,
        text = "Password"
    )
    getStrings()["password"] = StringVar(name = "password")
    getStrings()["password"].trace('w', entryCallback)
    password = Entry(
        frame,
        textvariable = getStrings()["password"],
        show = '*'
    )
    passwordLabel.pack()
    password.pack(pady = (0, 5))
    getWidgets()["password"] = password


def loadStyles(frame):
    row = 0
    buttonsPerRow = 4
    for i in range(len(getWindow().get_themes())):
        if (i % buttonsPerRow == 0):
            row += 1

        button = Button(
            frame,
            text = getWindow().get_themes()[i],
            command = lambda theme = getWindow().get_themes()[i]: changeTheme(theme),
        ).grid(column = i % buttonsPerRow, row = row, padx = 5, pady = 5)

        getWidgets()["styleButton" + str(i)] = button


def loadLabels(frame):
    label = Label(
        frame,
        text = "Normal Label"
    )

    label.pack()
    getWidgets()["label"] = label

    warningLabel = Label(
        frame,
        style = "Warning.TLabel",
        text = "Warning"
    )
    warningLabel.pack()
    getWidgets()["warningLabel"] = warningLabel
from tkinter import *
from tkinter import StringVar

from PIL import ImageTk, Image

root = Tk()
root.title('Codemy.com Image Viewer')
root.geometry("400x400")


def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]


clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()

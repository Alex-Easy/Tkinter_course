from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I Clicked a button!!!")
    myLabel.pack()


myButton = Button(root, text="Click me", command=myClick, fg="blue", bg="red")
myButton.pack()

root.mainloop()

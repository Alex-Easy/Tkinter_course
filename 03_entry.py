from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="white", fg="black", borderwidth=5)
e.pack()
e.insert(0, "Enter your name")

def myClick():

    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter yor name", command=myClick)
myButton.pack()

root.mainloop()

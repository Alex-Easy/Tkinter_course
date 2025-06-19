from tkinter import *
from tkinter import StringVar

from PIL import ImageTk, Image

root = Tk()
root.title('Codemy.com Image Viewer')
root.geometry("400x400")


def show():
    my_Label = Label(root, text=var.get()).pack()


# var = IntVar()
var = StringVar()

# c = Checkbutton(root, text="Check this box, I dare you!", variable=var)
# c.pack()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()



myButton = Button(root, text="Show section", command=show).pack()

root.mainloop()

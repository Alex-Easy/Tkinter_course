from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code at Codemy.com')


def open():
    global my_img
    top = Toplevel()
    # lbl = Label(top, text="Hello World!").pack()
    top.title('Learn to code at Codemy.com')
    root.iconbitmap("some your favicon path")
    my_img = ImageTk.PhotoImage(Image.open("path to your image"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()

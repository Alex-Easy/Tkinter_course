from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Learn to code at Codemy.com')


# root.iconbitmap("some your favicon path")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="path to file", title="Select a file",
                                               filetypes=(("png files",
                                                           "*.png"),
                                                          ("all "
                                                           "files",
                                                           "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_button = Button(root, text="Open file", command=open).pack()

mainloop()

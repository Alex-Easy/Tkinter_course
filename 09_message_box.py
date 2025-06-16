from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn to code at Codemy.com')


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

# def popup():
#     response = messagebox.askyesno("This is my Popup", "Hello World!")
#     Label(root, text=response).pack()
#     if response == 1:
#         Label(root, text="You clicked Yes!").pack()
#     else:
#         Label(root, text="You clicked No!").pack()

def popup():
    response = messagebox.askokcancel("This is my Popup", "Hello World!")
    Label(root, text=response).pack()


Button(root, text="Popup", command=popup).pack()

mainloop()

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Learn to code at Codemy.com')
root.iconbitmap('laptop.ico')  # Ensure this file exists in your working directory

# Open and resize the image first, then create PhotoImage
original_image = Image.open("image.jpeg")  # Ensure this file exists
resized_image = original_image.resize((300, 300))  # Resize before PhotoImage
my_img = ImageTk.PhotoImage(resized_image)

my_label = Label(root, image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
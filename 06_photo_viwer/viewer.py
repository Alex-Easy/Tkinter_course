from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Learn to code at Codemy.com')
root.iconbitmap('laptop.ico')

# Загрузка изображений
my_img1 = ImageTk.PhotoImage(Image.open("photos/1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("photos/2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("photos/3.png"))

image_list = [my_img1, my_img2, my_img3]

# Текущий индекс изображения
current_index = 0

my_label = Label(image=image_list[current_index])
my_label.grid(row=0, column=0, columnspan=3)


# Функция "вперёд"
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global current_index

    current_index = image_number - 1
    update_image()


# Функция "назад"
def back(image_number):
    global my_label
    global button_forward
    global button_back
    global current_index

    current_index = image_number - 1
    update_image()


# Обновление изображения и кнопок
def update_image():
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[current_index])

    button_back.grid_forget()
    button_forward.grid_forget()

    if current_index > 0:
        button_back = Button(root, text="<<", command=lambda: back(current_index))
    else:
        button_back = Button(root, text="<<", state=DISABLED)

    if current_index < len(image_list) - 1:
        button_forward = Button(root, text=">>", command=lambda: forward(current_index + 2))
    else:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


# Функции для управления стрелками
def on_left_arrow(event):
    global current_index
    if current_index > 0:
        current_index -= 1
        update_image()


def on_right_arrow(event):
    global current_index
    if current_index < len(image_list) - 1:
        current_index += 1
        update_image()


# Привязка стрелок
root.bind("<Left>", on_left_arrow)
root.bind("<Right>", on_right_arrow)

# Кнопки
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()

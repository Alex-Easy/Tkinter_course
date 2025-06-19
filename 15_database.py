from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Codemy.com Image Viewer')
root.geometry("400x400")

# Create db or connect to one

conn = sqlite3.connect('address_book.db')


# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
first_name text,
last_name text,
adress text,
city text,
state text,
zipcode integer
)""")


# Commit changes
conn.commit()

# Close connection
conn.close()


root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Codemy.com Database')
root.geometry("400x400")

# Create db or connect to one

conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()


# Create table
# c.execute("""CREATE TABLE addresses (
# first_name text,
# last_name text,
# adress text,
# city text,
# state text,
# zipcode integer
# )""")

# Create edit function to update a record

def edit():
    editor = Tk()
    editor.title('Update a record')
    editor.geometry("400x400")

    # Create db or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    # print(records)

    # print_records = ''
    # for record in records:
    #     print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    # Create text boxes

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create text box Labels

    f_name_label = Label(editor, text="First name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address name")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City name")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State name")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode name")
    zipcode_label.grid(row=5, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create a save button to save edited button
    edit_btn = Button(editor, text="Save record", command=edit)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=120)


# Create function to delete a record

def delete():
    # Create db or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


# Create submit function for database

def submit():
    # Create db or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get(),
              })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create query function
def query():
    # Create db or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


# Create text boxes

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create text box Labels

f_name_label = Label(root, text="First name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address name")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City name")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State name")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode name")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Create submit button

submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=90)

# Create a query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=115)

# Create a delete button
delete_btn = Button(root, text="Delete record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=115)

# Create an update button
edit_btn = Button(root, text="Edit record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()

from tkinter import *
import tkinter as tk 
import pg8000


root = Tk()

def get_data(name, age, address):
    # Database connection
    conn = pg8000.connect(database="postgres", user="postgres", password="123", host="localhost", port="5432")
    cur = conn.cursor()
    # Correct query and execution
    query = '''INSERT INTO students (name, age, address) VALUES (%s, %s, %s);'''
    try:
        cur.execute(query, (name, age, address))
        conn.commit()  # Commit the transaction
        print("Data inserted successfully!")
    except pg8000.ProgrammingError as e:
        print("Error: ", e)
    finally:
        cur.close()
        conn.close()






def search(name):
    conn = pg8000.connect(database="postgres", user="postgres", password="123", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM students WHERE name = %s;'''  # Use %s without quotes for parameterization
    try:
        cur.execute(query, (name,))  # Use a tuple with a comma for a single parameter
        row = cur.fetchone()
        conn.commit()
        print(row)
    except pg8000.ProgrammingError as e:
        print("Error: ", e)
    finally:
        cur.close()
        conn.close()








canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relheight=.8,relwidth=.8, relx=0.3,rely=0.1)

label = Label(frame, text="Data Added")
label.grid(row=0, column=1)

label = Label(frame, text="Name")
label.grid(row=2,column=0)

entryName = Entry(frame)
entryName.grid(row=2, column=1)

label = Label(frame, text="Age")
label.grid(row=4,column=0)

entryAge = Entry(frame)
entryAge.grid(row=4, column=1)

label = Label(frame, text="Address")
label.grid(row=6,column=0)

entryAddress = Entry(frame)
entryAddress.grid(row=6, column=1)

button = Button(frame, text="Add", command= lambda: get_data(entryName.get(),entryAge.get(),entryAddress.get()))
button.grid(row=8, column=2)

label = Label(frame, text="Search Data")
label.grid(row=10,column=1)

label = Label(frame, text="Search by Name")
label.grid(row=12,column=0)

entrySearch = Entry(frame)
entrySearch.grid(row=12, column=1)

button = Button(frame, text="Search", command= lambda: search(entrySearch.get()))
button.grid(row=14, column=2)








root.mainloop()
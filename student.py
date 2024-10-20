#packages installation 
from tkinter import *
import tkinter as tk 
import pg8000


root = Tk()
#function to ADD data
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
        displayAll()
    except pg8000.ProgrammingError as e:
        print("Error: ", e)
    finally:
        cur.close()
        conn.close()





#Function for seraching data
def search(name):
    conn = pg8000.connect(database="postgres", user="postgres", password="123", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM students WHERE name = %s;'''  # Use %s without quotes for parameterization
    try:
        cur.execute(query, (name,))  # Use a tuple with a comma for a single parameter
        row = cur.fetchone()
        conn.commit()
        searchDisplay(row)
    except pg8000.ProgrammingError as e:
        print("Error: ", e)
    finally:
        cur.close()
        conn.close()



#Function to display searched data
def searchDisplay(row):
    listbox = Listbox(frame, width=30, height=1)
    listbox.grid(row=16, column=1)
    listbox.insert(END, row)


#Function to display all data in database(students)
def displayAll():
    conn = pg8000.connect(database="postgres", user="postgres", password="123", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT * FROM students;'''  
    try:
        cur.execute(query)  
        row = cur.fetchall()
        conn.commit()
        listbox = Listbox(frame, width=25, height=10)
        listbox.grid(row=18, column=1)
        for x in row:
            listbox.insert(END,x)
    except pg8000.ProgrammingError as e:
        print("Error: ", e)
    finally:
        cur.close()
        conn.close() 



#To controle size of screen
canvas = Canvas(root, height=480, width=900)
canvas.pack()
# To make a frame w.r.t canvas
frame = Frame()
frame.place(relheight=.8,relwidth=.8, relx=0.3,rely=0.1)
#add label using frame attachment
label = Label(frame, text="Data Added")
label.grid(row=0, column=1)
#add label using frame attachment
label = Label(frame, text="Name")
label.grid(row=2,column=0)
#add text-input field using frame attachment
entryName = Entry(frame)
entryName.grid(row=2, column=1)# use grig-layout to comtrole position of forms
#add label using frame attachment
label = Label(frame, text="Age")
label.grid(row=4,column=0)
#add text-input field using frame attachment
entryAge = Entry(frame)
entryAge.grid(row=4, column=1)
#add label using frame attachment
label = Label(frame, text="Address")
label.grid(row=6,column=0)
#add text-input field using frame attachment
entryAddress = Entry(frame)
entryAddress.grid(row=6, column=1)
#created a button to Add data
button = Button(frame, text="Add", command= lambda: get_data(entryName.get(),entryAge.get(),entryAddress.get()))
button.grid(row=8, column=2)
#label for search data
label = Label(frame, text="Search Data")
label.grid(row=10,column=1)
#label for searching by name
label = Label(frame, text="Search by Name")
label.grid(row=12,column=0)
#add text-input field using frame attachment
entrySearch = Entry(frame)
entrySearch.grid(row=12, column=1)
#button for Searching data 
button = Button(frame, text="Search", command= lambda: search(entrySearch.get()))
button.grid(row=14, column=2)


# calling for all display data-rows
displayAll()
root.mainloop()
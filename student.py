from tkinter import *
import tkinter as tk 

root = Tk()
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

button = Button(frame, text="Add")
button.grid(row=8, column=2)



root.mainloop()
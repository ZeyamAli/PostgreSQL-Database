from tkinter import *
import tkinter as tk 

root = Tk()
canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relheight=.8,relwidth=.8, relx=0.3,rely=0.1)

label = Label(frame, text="Data Added")
label.grid(row=0, column=1)

root.mainloop()
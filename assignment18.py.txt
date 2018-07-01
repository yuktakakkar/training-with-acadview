#Ques-1
//Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

import tkinter
from tkinter import *

empty = {}

def func(x, y):
    empty.update({x:int(y)})
    print(empty)

tk = tkinter.Tk()
scrollbar = Scrollbar(tk)
scrollbar.pack(side = RIGHT, fill = Y)
mylist = Listbox(tk, yscrollcommand = scrollbar.set )
lbl = Label(tk, text = "Create a Dictionary:").pack()

x = StringVar()
y = StringVar()

label_1 = Label(tk, text="Enter Name and Phone number: ").pack()
entry_1 = Entry(tk, textvariable=x)
entry_1.pack()
entry_2 = Entry(tk, textvariable=y)
entry_2.pack()

bt = Button(tk, text="Execute", command=lambda :func(x.get(), y.get()))
bt.pack()
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config(command = mylist.yview)
tk.mainloop()

#Ques-2
//In the same tkinter file as created above, create a function to insert items into the dictionary.


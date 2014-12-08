import sys
from Tkinter import *
import os

def call_a():
    os.system('TypeA.pyw')

def call_b():
    os.system('TypeB.pyw')

gui = Tk()

gui.geometry('400x400+500+250')
gui.title('Ez-Finance')



close = Button(gui, text="close", command=gui.destroy)
a = Button(gui, text="Type A", command=call_a)
b = Button(gui, text="type B", command=call_b)
a.place(relx=.3, rely=.6, anchor="c")
b.place(relx=.7, rely=.6, anchor="c")

close.place(relx=.9, rely=.9, anchor="c")

gui.mainloop()

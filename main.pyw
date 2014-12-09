import sys
from Tkinter import *
import os

def call_a():
    '''
    call_a(...)
        Open Type A in new window
    '''
    os.system('TypeA.pyw')

def call_b():
    '''
    call_b(...)
        Open Type B in new window
    '''
    os.system('TypeB.pyw')

class main():
    '''
    main menu
    '''
    def __init__(self):
        self = Tk()
        self.geometry('400x400+500+250')
        self.title('Ez-Finance')



        close = Button(self, text="close", command=self.destroy)
        a = Button(self, text="Type A", command=call_a)
        b = Button(self, text="type B", command=call_b)
        a.place(relx=.3, rely=.6, anchor="c")
        b.place(relx=.7, rely=.6, anchor="c")

        close.place(relx=.9, rely=.9, anchor="c")

        self.mainloop()
main()

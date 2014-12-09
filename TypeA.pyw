import sys
from Tkinter import *
import table1to4 as tb

def okk():
    mtext = money.get()
    mlebel = Label(self, text=mtext)
    mlebel.place(relx=.5, rely=.7, anchor="c")
    
class typea():
    '''type a'''
    def __init__(self):
        '''typea'''        
        self = Tk()
        self.geometry('400x400+600+300')
        self.title('TypeA')
        money = StringVar()
        interest = StringVar()
        year = StringVar()
        
        c = Button(self, text="close", command=self.destroy)
        c.place(relx=.9, rely=.9, anchor="c")

        label1 = Label(self, text='Money      : ')
        label2 = Label(self, text='Interest   : ')
        label3 = Label(self, text='Year       : ')
        label1.place(relx=.3, rely=.3, anchor="c")
        label2.place(relx=.3, rely=.4, anchor="c")
        label3.place(relx=.3, rely=.5, anchor="c")
            
        entry1 = Entry(self,textvariable=money)
        entry2 = Entry(self,textvariable=interest)
        entry3 = Entry(self,textvariable=year)
        entry1.place(relx=.6, rely=.3, anchor="c")
        entry2.place(relx=.6, rely=.4, anchor="c")
        entry3.place(relx=.6, rely=.5, anchor="c")
            
        ok = Button(self, text="OK", command=okk)
        ok.place(relx=.5, rely=.6, anchor="c")

        self.mainloop()
typea()

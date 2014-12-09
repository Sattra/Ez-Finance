import sys
from Tkinter import *
import table1to4 as tb

def calculate(gui, interest, year, money, check):
    if check == 0:
        answer = str(tb.table_3(interest, year, money))
    else:
        answer = str(tb.table_4(interest, year, money))
    mrefesh = Label(gui, text='                             ').place(relx=.6, rely=.8, anchor="c")
    mlebel = Label(gui, text=answer)
    mlebel1 = Label(gui, text='Answer')
    mlebel.place(relx=.6, rely=.8, anchor="c")
    mlebel1.place(relx=.3, rely=.8, anchor="c")
    
class typea():
    '''type a'''
    def __init__(self):
        '''typea'''        
        self = Tk()
        self.geometry('400x400+600+300')
        self.title('Future')
        money = StringVar()
        interest = StringVar()
        year = StringVar()
        check = IntVar()

        Radiobutton(self, text="one time",
                    variable=check, value=0).place(relx=.34,rely=.38, anchor="c")
        Radiobutton(self, text="every years",
                    variable=check, value=1).place(relx=.6, rely=.38, anchor="c")
        c = Button(self, text="close", command=self.destroy)
        c.place(relx=.9, rely=.9, anchor="c")

        label1 = Label(self, text='Money      : ')
        label2 = Label(self, text='Interest   : ')
        label3 = Label(self, text='Year       : ')
        label1.place(relx=.3, rely=.3, anchor="c")
        label2.place(relx=.3, rely=.5, anchor="c")
        label3.place(relx=.3, rely=.6, anchor="c")
            
        entry1 = Entry(self, textvariable=money)
        entry2 = Entry(self, textvariable=interest)
        entry3 = Entry(self, textvariable=year)
        entry1.place(relx=.6, rely=.3, anchor="c")
        entry2.place(relx=.6, rely=.5, anchor="c")
        entry3.place(relx=.6, rely=.6, anchor="c")
        
        ok = Button(self, text="OK",
                    command=lambda: calculate(self, interest.get(), year.get(), money.get(), check.get()))
        ok.place(relx=.5, rely=.7, anchor="c")

        self.mainloop()
typea()

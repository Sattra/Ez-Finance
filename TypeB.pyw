import sys
from Tkinter import *

def okk():
    mtext = money.get()
    mlebel = Label(agui, text=mtext)
    mlebel.place(relx=.5, rely=.7, anchor="c")

agui = Tk()
money = StringVar()
interest = StringVar()
year = StringVar()

agui.geometry('400x400+600+300')
agui.title('TypeB')
c = Button(agui, text="close", command=agui.destroy)
c.place(relx=.9, rely=.9, anchor="c")
    
va1 = Entry(agui,textvariable=money)
va1.place(relx=.5, rely=.3, anchor="c")
va2 = Entry(agui,textvariable=interest)
va2.place(relx=.5, rely=.4, anchor="c")
va3 = Entry(agui,textvariable=year)
va3.place(relx=.5, rely=.5, anchor="c")
    
ok = Button(agui, text="OK", command=okk)
ok.place(relx=.5, rely=.6, anchor="c")

mainloop()
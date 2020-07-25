import tkinter
from tkinter import *
import time
from tkinter import ttk

root = Tk()
root.geometry('1600x800+0+0')
root.title('Hotel Management System')



#=================Window's Partition=================================
Tops = Frame(root, width=1600, height=100, bg='blue',relief=SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width =300, height=700, relief= SUNKEN)
f2.pack(side=RIGHT)

f3=Frame(root,width=35,height=700,relief=SUNKEN)
f3.pack(side=LEFT)

f4 = Frame(root,width=100, height=700, relief=SUNKEN)
f4.pack(side=LEFT)

#=========================MAIN SCREEN===========================
txt_impute = StringVar(value='Master Python Today...')
Display = Entry(Tops,font=('arial',97,'bold'),fg='white',bd=50,bg='blue',justify='right',textvariable=txt_impute)
Display.grid(columnspan=3)




root.mainloop()
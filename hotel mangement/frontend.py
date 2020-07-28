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
Display.grid(columnspan=4)

#============================Date and Time=========================
localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(f2,font=('arial',20,'bold'),text=localtime,fg='dark blue',bd=10,anchor=W)
lblinfo.grid(row=0,column=0,columnspan=4)

#========================Row 1=======================

btn7 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='7')
btn7.grid(row=1,column=0)
btn8 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='8')
btn8.grid(row=1,column=1)
btn9 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='9')
btn9.grid(row=1,column=2)
btnC = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='C')
btnC.grid(row=1,column=3)

#========================Row 2=======================

btn4 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='4')
btn4.grid(row=2,column=0)
btn5 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='5')
btn5.grid(row=2,column=1)
btn6 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='6')
btn6.grid(row=2,column=2)
btnplus = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='+')
btnplus.grid(row=2,column=3)



#========================Row 3=======================

btn1 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='1')
btn1.grid(row=3,column=0)
btn2 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='2')
btn2.grid(row=3,column=1)
btn3 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='3')
btn3.grid(row=3,column=2)
btnminus = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='-')
btnminus.grid(row=3,column=3)


#========================Row 4=======================
btn1 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='1')
btn1.grid(row=3,column=0)
btn2 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='2')
btn2.grid(row=3,column=1)
btn3 = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='3')
btn3.grid(row=3,column=2)
btnminus = Button(f2,padx=15,pady=5,border=8,font=('arial',30,'bold'),text='-')
btnminus.grid(row=3,column=3)




#========================Row 5=======================

root.mainloop()
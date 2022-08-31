from tkinter import *
global operator
#operator=''
def convert(num):
    if num==1:
        display.set(display.get()*2.54)
    elif num==2:
        display.set(display.get()/2.54)
    elif num==3:
        display.set(display.get()/3.281)
    elif num==4:
        display.set(display.get()*3.281)
    elif num==5:
        display.set(display.get()/1.094)
    elif num==6:
        display.set(display.get()*1.094)
    elif num==7:
        display.set(display.get()*1.609)
    elif num==8:
        display.set(display.get()/1.609)
    elif num==9:
        display.set(display.get()*1609)
    elif num==10:
        display.set(display.get()/1609)



def b1():
    convert(1) 
def b2():
    convert(2)
def b3():
    convert(3)
def b4():
    convert(4)
def b5():
    convert(5)
def b6():
    convert(6)
def b7():
    convert(7)
def b8():
    convert(8)
def b9():
    convert(9)
def b10():
    convert(10)




root = Tk()
root.title("Units Convertor")
Label(text="Welcome to units convertor",font='arial 15 bold',bd=6).grid(row=0,column=0,columnspan=2)

display = IntVar()
entry = Entry(root,textvariable=display,font='arial 20 bold',bd=10,justify='right').grid(row=1,column=0,columnspan=2)

Button(text="in->cm",width=8,command=b1,pady=10).grid(row=2,column=0)
Button(text="cm->in",width=8,command=b2,pady=10).grid(row=2,column=1)
Button(text="ft->m",width=8,command=b3,pady=10).grid(row=3,column=0)
Button(text="m->ft",width=8,command=b4,pady=10).grid(row=3,column=1)
Button(text="yd->m",width=8,command=b5,pady=10).grid(row=4,column=0)
Button(text="m->yd",width=8,command=b6,pady=10).grid(row=4,column=1)
Button(text="mile->km",width=8,command=b7,pady=10).grid(row=5,column=0)
Button(text="km->mile",width=8,command=b8,pady=10).grid(row=5,column=1)
Button(text="mile->m",width=8,command=b9,pady=10).grid(row=6,column=0)
Button(text="m->mile",width=8,command=b10,pady=10).grid(row=6,column=1)


root.mainloop()
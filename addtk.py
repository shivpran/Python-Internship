from tkinter import *
t=Tk()
def func():
    x=e.get()
    x1=e1.get()
    x2=e2.get()
    a=int(x)
    b=int(x2)
    if x1=='+':
        s=int(a+b)
        print('Addition =',s)
    elif x1=='-':
        sub=int(a-b)
        print('Substraction =',sub)
    elif x1=='*':
        m=int(a*b)
        print('Multilication=',m)
    else:
        d=int(a/b)
        print('Division =',d)

l=Label(t,text='First Number')
l.pack()
e=Entry(t)
e.pack()

l1=Label(t,text='Operator')
l1.pack()
e1=Entry(t)
e1.pack()

l2=Label(t,text='Second Number')
l2.pack()
e2=Entry(t)
e2.pack()

b=Button(t,text='=',command=func)
b.pack()

t.mainloop()

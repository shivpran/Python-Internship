from tkinter import *
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        #expression = ""
    except:
        equation.set(" error ")
        expression = "" 
  
def clear(): 
    global expression 
    expression = "" 
    equation.set("")
    
if __name__ == "__main__":
    t=Tk()
    t.geometry('220x280')
    t.configure(bg='grey')
    a=Label(t,text='Calculator',fg='black',height=2,width=20)
    a.pack()

    equation = StringVar() 

    t2=Entry(t,textvariable=equation)
    t2.place(x=0,y=65,anchor=W)

#t1=Entry(t)
#t1.place(x=0,y=80,anchor=W)

    b=Button(t,text='clear',fg='black',height=2,width=10,command=clear)
    b.place(x=140,y=65,anchor=W)

    b1=Button(t,text='1',fg='black',height=1,width=5,command=lambda:press(1))
    b1.place(x=0,y=110,anchor=W)

    b2=Button(t,text='2',fg='black',height=1,width=5,command=lambda:press(2))
    b2.place(x=50,y=110,anchor=W)

    b3=Button(t,text='3',fg='black',height=1,width=5,command=lambda:press(3))
    b3.place(x=100,y=110,anchor=W)

    b4=Button(t,text='4',fg='black',height=1,width=5,command=lambda:press(4))
    b4.place(x=0,y=140,anchor=W)

    b5=Button(t,text='5',fg='black',height=1,width=5,command=lambda:press(5))
    b5.place(x=50,y=140,anchor=W)
    
    b6=Button(t,text='6',fg='black',height=1,width=5,command=lambda:press(6))
    b6.place(x=100,y=140,anchor=W)

    b7=Button(t,text='7',fg='black',height=1,width=5,command=lambda:press(7))
    b7.place(x=0,y=170,anchor=W)

    b8=Button(t,text='8',fg='black',height=1,width=5,command=lambda:press(8))
    b8.place(x=50,y=170,anchor=W)

    b9=Button(t,text='9',fg='black',height=1,width=5,command=lambda:press(9))
    b9.place(x=100,y=170,anchor=W)

    b10=Button(t,text='0',fg='black',height=1,width=5,command=lambda:press(0))
    b10.place(x=0,y=200,anchor=W)

    b11=Button(t,text='.',fg='black',height=1,width=5,command=lambda:press("."))
    b11.place(x=50,y=200,anchor=W)

    b12=Button(t,text='=',fg='black',height=1,width=5,command=lambda:equalpress())
    b12.place(x=100,y=200,anchor=W)

    s=Button(t,text='+',fg='black',height=1,width=7,command=lambda:press("+"))
    s.place(x=160,y=110,anchor=W)

    s1=Button(t,text='-',fg='black',height=1,width=7,command=lambda:press("-"))
    s1.place(x=160,y=140,anchor=W)

    s2=Button(t,text='*',fg='black',height=1,width=7,command=lambda:press("*"))
    s2.place(x=160,y=170,anchor=W)

    s3=Button(t,text='/',fg='black',height=1,width=7,command=lambda:press("/"))
    s3.place(x=160,y=200,anchor=W)

    t.mainloop()


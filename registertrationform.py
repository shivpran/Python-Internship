from tkinter import *
r=Tk()

def show():
    a=t.get()
    print(a)
    b=t1.get()
    print('Email Id:',b)
    c=t2.get()
    print('Mobile No:',c)
    d=t3.get()
    print('Date-Of-Birth:',d)
    x=v.get()
    print("Gender:")
    if x==1:
        print("Male")
    elif x==2:
        print("Female")
    else :
        print("Other")
   
r.geometry('1000x1000')
r.configure(bg='black')
a=Label(r,text='Registration Form',fg='red',height=2,width=20)
a.pack()


n=Label(r,text='Enter Name:',height=2,width=15,fg='white',bg='black')
n.place(x=280,y=100,anchor=W)


t=Entry(r,height=2,width=35)
t.place(x=400,y=100,anchor=W)


n=Label(r,text='Email-Id:',height=2,width=15,fg='white',bg='black')
n.place(x=280,y=150,anchor=W)

t1=Entry(r,height=2,width=35)
t1.place(x=400,y=150,anchor=W)


n=Label(r,text='Mobile No.:',height=2,width=15,fg='white',bg='black')
n.place(x=280,y=200,anchor=W)

t2=Entry(r,height=2,width=35)
t2.place(x=400,y=200,anchor=W)


n=Label(r,text='Date-Of-Birth:',height=2,width=15,fg='white',bg='black')
n.place(x=280,y=250,anchor=W)

t3=Entry(r,height=2,width=35)
t3.place(x=400,y=250,anchor=W)


n=Label(r,text='Gender:',height=2,width=15,fg='white',bg='black')
n.place(x=280,y=300,anchor=W)

v=IntVar()
bb=Radiobutton(r,text='Male',variable=v,fg='black',value=1)
bb.place(x=400,y=300,ancho=W)

bbb=Radiobutton(r,text='FeMale',variable=v,fg='black',value=2)
bbb.place(x=460,y=300,ancho=W)


bbb1=Radiobutton(r,text='Other',variable=v,fg='black',value=3)
bbb1.place(x=530,y=300,ancho=W)

n=Label(r,text='Password:',height=2,width=15,fg='white',bg='black')
n.place(x=280,y=350,anchor=W)

t=Entry(r,height=2,width=35)
t.place(x=400,y=350,anchor=W)


n=Label(r,text='Confirm Password:',height=2,width=15,fg='white',bg='black')
n.place(x=280,y=400,anchor=W)

t1=Entry(r,height=2,width=35)
t1.place(x=400,y=400,anchor=W)


b=Button(r,text="Submit",bg="black",fg="white",height=2,width=10,command=show)
b.place(relx = 0.5, rely = 0.6, anchor = CENTER)
b1=Button(r,text="Cancel",bg="black",fg="white",height=2,width=10)
b1.place(relx = 0.6, rely = 0.6, anchor = CENTER)
r.mainloop()

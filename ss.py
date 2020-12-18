from tkinter import *
r=Tk()
r.geometry('1000x1000')
r.configure(bg='black')
a=Label(r,text='Login',fg='red',height=2,width=20)
a.grid(row=0,column=5,padx=(450,450), pady=(10,10))

n=Label(r,text='Email-Id',height=2,width=15,fg='white',bg='black')
n.grid(row=3,column=5,padx=(280,500), pady=(50,50))

t=Text(r,height=2,width=25)
t.grid(row=3,column=5,padx=(400,250), pady=(50,50))
t.insert(END,'')

n=Label(r,text='Password',height=2,width=15,fg='white',bg='black')
n.grid(row=4,column=5,padx=(280,500), pady=(5,5))

t=Text(r,height=2,width=25)
t.grid(row=4,column=5,padx=(400,250), pady=(5,5))
t.insert(END,'')

b=Button(r,text="Login",bg="black",fg="white",height=2,width=10)
b.grid(row=5,column=5,padx=(350,280), pady=(10,10))

b=Button(r,text="Cancel",bg="black",fg="white",height=2,width=10)
b.grid(row=5,column=5,padx=(500,250), pady=(10,10))

r.mainloop()

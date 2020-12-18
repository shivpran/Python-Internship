from tkinter import *
r=Tk()

def val():
    x=t.get()
    y=t1.get()
    if 'Admin'==x and 'Admin'==y:
        #l1.configure(text='Valid',fg='green',bg='white')
        #l2.configure(text='Valid',fg='green',bg='white')
        l4.configure(text='Login Successful',fg='green',bg='white')
    elif 'Admin'!=x and 'Admin'==y:
        #l1.configure(text='Invalid Username',fg='red',bg='white')
        #l2.configure(text='Valid',fg='green',bg='white')
        l4.configure(text='Username or Password you entered is incorrect\nplease enter valid credentials',fg='red',bg='white')
    elif 'Admin'!=y and 'Admin'==x:
        #l1.configure(text='Valid',fg='green',bg='white')
        #l2.configure(text='Invalid Password',fg='red',bg='white')
        l4.configure(text='Username or Password you entered is incorrect\n please enter valid credentials',fg='red',bg='white')
    #elif x=='' and y=='':
        #l1.configure(text='Enter Username',fg='red',bg='white')
        #l4.configure(text='Username and Passwoed Required',fg='red',bg='white')
        #l2.configure(text='Enter Password',fg='red',bg='white')
    else:
        l4.configure(text='Enter Valid Credentials',fg='white',bg='black')
    


r.geometry('1000x1000')
#r.configure(bg='black')
a=Label(r,text='Login',fg='red',height=2,width=20)
a.grid(row=0,column=5,padx=(450,450), pady=(10,10))



n=Label(r,text='Email-Id',height=2,width=15,fg='white',bg='black')
n.grid(row=3,column=5,padx=(240,500), pady=(50,50))

s=StringVar()
t=Entry(r)
t.grid(row=3,column=5,padx=(360,250), pady=(50,50))

#l1=Label(r,text='',height=1,width=15,bg='white')
#l1.grid(row=3,column=5,padx=(470,100), pady=(50,50))

n=Label(r,text='Password',height=2,width=15,fg='white',bg='black')
n.grid(row=4,column=5,padx=(240,500), pady=(5,5))

t1=Entry(r)
t1.grid(row=4,column=5,padx=(360,250), pady=(5,5))

#b2=Button(r,text="show password",bg="grey",fg="black",height=1,width=13)
#b2.grid(row=4,column=5,padx=(635,200), pady=(5,5))


#l2=Label(r,text='',height=1,width=15,bg='white')
#l2.grid(row=4,column=5,padx=(470,100), pady=(5,5))

bb=Button(r,text="Login",bg="black",fg="white",height=2,width=10,command=val)
bb.grid(row=5,column=5,padx=(300,280), pady=(15,15))

bb1=Button(r,text="Cancel",bg="black",fg="white",height=2,width=10)
bb1.grid(row=5,column=5,padx=(450,250), pady=(15,15))

#l3=Label(r,text='',height=1,width=15,bg='black')
#l3.grid(row=5,column=5,padx=(510,100), pady=(5,5))

l4=Label(r,text='',height=4,width=40,bg='white')
l4.grid(row=6,column=5,padx=(350,250), pady=(10,10))

b1=Button(r,text="Login Using Google",bg="white",fg="red",height=2,width=25)
b1.grid(row=8,column=5,padx=(350,250), pady=(10,10))

b3=Button(r,text="Login Using Facebook",bg="blue",fg="white",height=2,width=25)
b3.grid(row=8,column=6,padx=(350,250), pady=(10,5))



r.mainloop()

from tkinter import *
m=Tk()
m.geometry('500x500')
m.configure(bg='purple')
a=Label(m,text="Python Internship")
a.pack()
e=Entry(m)
e.place(relx = 1, x =-2, y = 2, anchor = NE)
b=Button(m,text="Submit",bg="blue",fg="white")
b.place(relx = 0.5, rely = 0.5, anchor = CENTER)

t=Text(m,height=1,width=20)
t.place(x=10,y=10,anchor=NW)
t.insert(END,'Name:')
t.insert(END,'')

w=Spinbox(m,from_=0,to=10)
w.place(x=10,y=30,anchor=NW)

v=IntVar()
bb=Radiobutton(m,text='ABC',variable=v)
bb.place(x=10,y=50,ancho=NW)

var1=IntVar()
cc=Checkbutton(m,text='Male',variable=var1)
cc.place(x=10,y=70,ancho=NW)

l1=Listbox(m)
l1.insert(1,'Hello')
l1.insert(2,'Python.....')
l1.place(x=10,y=90,ancho=NW)

me=Menu(m)
m.config(menu=me)
filemenu=Menu(me)
editmenu=Menu(me)
me.add_cascade(label='File',menu=filemenu)
me.add_cascade(label='Edit',menu=editmenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_command(label='Save As')
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
editmenu.add_command(label='Undo')

from tkinter import *
from Backend import db

database=db('Booksdata.db')

def selection(event):
    try:
        global selected_tuple
        index=lb1.curselection()[0]
        selected_tuple=lb1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass    

def view_command():      #Wrapper function used to pass arguments and call functions from another file
    lb1.delete(0,END)       #which cannot be done directly in button mapping (command=function)
    for row in database.view():
        lb1.insert(END,row)

def search_command():
    lb1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        lb1.insert(END,row)

def add_command():
    lb1.delete(0,END)
    if not (title_text.get()=={} and author_text.get()=={} and year_text.get()=={} and isbn_text.get()=={}):
        database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        lb1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
    
def update_command():
    try:
        database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        view_command()
    except NameError:
        pass

def delete_command():
    try:
        database.delete(selected_tuple[0])
        view_command()
    except NameError:
        pass

window=Tk()
window.title("Bookstore")

lab1=Label(window,text="Title")
lab1.grid(row=0,column=0)
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

lab2=Label(window,text="Author")
lab2.grid(row=0,column=2)
author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

lab3=Label(window,text="Year")
lab3.grid(row=1,column=0)
year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

lab2=Label(window,text="ISBN")
lab2.grid(row=1,column=2)
isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

lb1=Listbox(window,height=6,width=35)
lb1.grid(row=2,column=0,rowspan=6,columnspan=2)
#Bind the widget to a function in case of an event
lb1.bind('<<ListboxSelect>>',selection)

sb1=Scrollbar(window)
sb1.grid(row=3,column=2,rowspan=6)

#Tell both scrollbar and listbox whom they are connected to by configuring them
lb1.configure(yscrollcommand =sb1.set)
sb1.configure(command=lb1.yview)

b1=Button(window,text='View All',width=12,command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text='Search All',width=12,command=search_command)
b2.grid(row=3,column=3)
b3=Button(window,text='Add Entry',width=12,command=add_command)
b3.grid(row=4,column=3)
b4=Button(window,text='Update Selected',width=12,command=update_command)
b4.grid(row=5,column=3)
b5=Button(window,text='Delete Selected',width=12,command=delete_command)
b5.grid(row=6,column=3)
b6=Button(window,text='Close',width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
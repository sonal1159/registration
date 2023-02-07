# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:03:39 2023

@author: SONAL
"""
from tkinter import *
import tkinter as tk
from tkinter import ttk

win=tk.Tk()

win.geometry('700x700')
win.title('Registration Form')

var2=''
l1=tk.Label(win,text="")


def selection():
   selected = radio.get()
   var3=int(selected)
   #print(type(var3))
   global var2
   if var3==1:
      var2='Male'
   elif var3==2:
      
      var2='Female'
   elif var3==3:
      
      var2='Other'
      
     
def submit():
    #l1.config(text="Form Submitted Successfully....!!", font=("arial bold",15),foreground='red')
    if n1.get()=='' :
        l1.config(text="Enter Full name!!", font=("arial bold",15),foreground='red')
        
    elif e1.get()=='':
        l1.config(text="Enter email....!!", font=("arial bold",15),foreground='red')
    
    elif m1.get()=='':
        l1.config(text="Enter contact no....!!", font=("arial bold",15),foreground='red')
    
    
    elif p1.get()=='':
        l1.config(text="Enter the password....!!", font=("arial bold",15),foreground='red')
        
    else:
        win1=tk.Tk()
        l1.config(text="Form Submitted Successfully....!!", font=("arial bold",15),foreground='red')
        win1.title('Database')
        tree = ttk.Treeview(win1, column=("Full Name", "Email", "Contact no","Gender","Password"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Full Name")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Email")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Contact no")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Gender")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="Password")
       
         
        tree.insert('', 'end', text="1", values=(n1.get(),e1.get(), m1.get(),var2,p1.get(),p2.get()))
        tree.pack()



name=tk.Label(win,text="Full Name: ",padx=5,pady=5, font=("arial",15),bg='Sky blue')
email=tk.Label(win,text="Email: ",padx=5,pady=5, font=("arial ",15),bg='Sky blue')
mob=tk.Label(win,text="Contact No: ",padx=5,pady=5, font=("arial",15),bg='Sky blue')
gender=tk.Label(win,text="Gender: ",padx=5,pady=5, font=("arial",15),bg='Sky blue')
pass1=tk.Label(win,text="Password: ",padx=5,pady=5, font=("arial",15),bg='Sky blue')
pass2=tk.Label(win,text="Reenter Password: ",padx=5,pady=5, font=("arial",15),bg='Sky blue')

n1=tk.StringVar()
en_name=tk.Entry(win,textvariable=n1)
e1=tk.StringVar()
en_email=tk.Entry(win,textvariable=e1)
m1=tk.StringVar()
en_mob=tk.Entry(win,textvariable=m1)
p1=tk.StringVar()
en_pass1=tk.Entry(win,show='.',textvariable=p1)
p2=tk.StringVar()
en_pass2=tk.Entry(win,show='.',textvariable=p2)


radio =tk.IntVar()

g1=tk.Radiobutton(win,text="Male",variable=radio,value=1,padx=5,pady=5, font=("arial",15),command=lambda:selection())
g2=tk.Radiobutton(win,text="Female",variable=radio,value=2,padx=5,pady=5, font=("arial",15),command=lambda:selection())
g3=tk.Radiobutton(win,text="Other",variable=radio,value=3,padx=5,pady=5, font=("arial",15),command=lambda:selection())


button=tk.Button(win,text="Submit" ,font=("arial",15),command=lambda:submit(),padx=5,pady=5,bg='Yellow')

name.grid(row=1,column=0)
email.grid(row=3,column=0)
mob.grid(row=6,column=0)
gender.grid(row=9,column=0)
pass1.grid(row=12,column=0)
pass2.grid(row=15,column=0)


en_name.grid(row=1,column=1)
en_email.grid(row=3,column=1)
en_mob.grid(row=6,column=1)
en_pass1.grid(row=12,column=1)
en_pass2.grid(row=15,column=1)

g1.grid(row=9,column=1)
g2.grid(row=9,column=2)
g3.grid(row=9,column=4)

button.grid(row=20 ,column=1)
l1.grid(row=27,column=1)

win.mainloop()

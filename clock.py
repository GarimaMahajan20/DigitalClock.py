from tkinter import *
from time import strftime
r= Tk()
r.title('Clock')
r.minsize(300,300)
def time():
    s =strftime('%d-%B-%Y , %H:%M:%S %p')
    l.config(text= s)
    l.after(1000,time)
l =Label(r,font=('calibri',40 , 'bold'),background ='purple' , foreground ='white')
l.pack(anchor ='center')
time()
def exit():
    r.destroy()
exit =Button(r,text='Exit' ,height=5,width =9,command = exit,font=8)
exit.pack(side=BOTTOM , anchor='e')

mainloop()

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('Basic Git & GitHub by Uncle Engineer')
GUI.geometry('500x700')

L = Label(GUI,text='Loong Wissawakorn')
L.pack()

L = Label(GUI,text='Uncle Engineer')
L.pack()

L = Label(GUI,text='tardev35')
L.pack()

L = Label(GUI,text='Cannonskr')
L.pack()

L = Label(GUI,text='somchai_dev')
L.pack()

v1 = StringVar()
E1 = ttk.Entry(GUI,textvariable=v1)
E1.pack()

v2 = StringVar()
E2 = ttk.Entry(GUI,textvariable=v2)
E2.pack()

def cal():
    c = float(v1.get()) * float(v2.get())
    r1 = v1.get()
    r2 = v2.get()
    text = f'{r1}x{r2}={c}'
    messagebox.showinfo('Result',text)

b1 = ttk.Button(GUI,text='Calculate Now!',command=cal)
b1.pack()

GUI.mainloop()
from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk 
import time
style = Style()

window= style.master
window.title("Machine Learning")
window.geometry("633x552")
window.resizable(False,False)

#633 552

    
x=PhotoImage(file="q.png")
y=Label(window,image=x).pack(fill="x")
#z=ttk.Button(window,text="Start",style='success.Outline.TButton',command=safal).place(x=393,y=233,width=130,height=70)

window.mainloop()
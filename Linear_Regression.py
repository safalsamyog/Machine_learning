from tkinter import *
from ttkbootstrap import Style
from tkinter import ttk 
from tkinter import filedialog as fd
import numpy as np
import pandas as pd
from sklearn import linear_model 
from sklearn.metrics import mean_squared_error
from tkinter import messagebox as msg
import matplotlib.pyplot as plt
def _Next():
    
    window1=win
    window1.title("Linear House Prediction")
    window1.geometry("633x552")
    window1.resizable(False,False)
    file1=StringVar()
    area=IntVar()
  
    
        
   
    def Model():
        file_data=file1.get()
        area_data=area.get()
       
        cx=pd.read_csv(file_data)
        xxx=cx.iloc[:,1].values
        yyy=cx.iloc[:,2].values
        z=linear_model.LinearRegression()


        cq=xxx.reshape(-1,1)#we should make x row vector y column vector in 2d only x and value passing is also 2d

        z.fit(cq,yyy)
        result=z.predict([[area_data]])
        #print(result)
        accuracy=np.around(z.score(cq,yyy),decimals=2)
        msg.showinfo("Result","The Predicted Price Of this Area with {}% accuraxy and with mean square error {}  is: {} ".format(accuracy*100,mean_squared_error(cq,yyy),np.around(result,decimals=2)))
        data=[]
        for i in xxx:
            res=z.predict([[i]])
            data.append(res)
        plt.title("Linear Regression House Price Prediction")
        plt.scatter(xxx,yyy,color="k",label="Testing Data")
        plt.scatter(xxx,data,color="r",label="Trained Data")
        plt.plot(xxx,data,color="b",label="Fitting Line",linestyle="--")
        plt.xlabel("Area",{"color":"red","size":16})
        plt.ylabel("House Price",{"color":"g","size":16})
        plt.grid()
        plt.legend()
        plt.show()
    xx=PhotoImage(file='E:/ML_Project/Linear_Regression/mm.png')
    yy=Label(window1,image=xx).place(x=0,y=0)
    e1=ttk.Entry(window1,style="info.TEntry",textvariable=file1).place(x=258,y=151,height=50,width=190)
    e2=ttk.Entry(window1,style="danger.TEntry",textvariable=area).place(x=258,y=245,height=50,width=190)
    def j_j():
       
        xx=fd.askopenfilename()
        file1.set(xx)
    open1=ttk.Button(window1,text="Open",style="info.Outline.TButton",command=j_j).place(x=460,y=151,height=50,width=150)
    
    
        
    z=ttk.Button(window1,text="Start Prediction",style='primary.Outline.TButton',command=Model).place(x=219,y=319,width=130,height=60)
    area.set("Enter area of house...")
    ext=ttk.Button(window1,text="Quit",style='danger.Outline.TButton',command=window1.destroy).place(x=500,y=500,width=100,height=40)
    
    window.quit()
    window1.mainloop() 


style = Style()

window= style.master
win=style.master
window.title("Machine Learning")
window.geometry("616x541")
window.resizable(False,False)

    
x=PhotoImage(file="Linear_Regression/p.png")
y=Label(window,image=x).pack(fill="x")
z=ttk.Button(window,text="Start",style='success.Outline.TButton',command=_Next).place(x=393,y=233,width=130,height=70)

window.mainloop()
win.mainloop()

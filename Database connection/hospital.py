from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="+ HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("Times New Roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        
    # ====================Data frame===================================
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                font=("Times New Roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                font=("Times New Roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)

        # ============================ buttons frame ===================================

        Buttonframe = Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)


        # ============================ Details frame ===================================

        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        # ============================ DataFrameLeft ===================================

        lblNameTablet = Label(DataframeLeft,text="Names OF Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet = ttk.Combobox(DataframeLeft,state="readonly",font=("times new roman",12,"bold"),
                                                                                width=33)
        comNametablet["values"]= ("Nice","Corona Vaccine","Acetaminophen","Adderall","Ativan")
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No Of Tables:",padx=2,pady=6)
        lblNoOftablets.grid(row=2,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtLot.grid(row=4,column=1)

        lblissueData=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueData.grid(row=5,column=0,sticky=W)
        txtissueData=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtissueData.grid(row=5,column=1)

        lblExpData=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Data:",padx=2,pady=6)
        lblExpData.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        lblFurtherinfo=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblBloodPressure.grid(row=0,column=2,sticky=W)
        lblBloodPressure=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        lblBloodPressure.grid(row=1,column=3)


        
root = Tk()
ob=Hospital(root)
root.mainloop()


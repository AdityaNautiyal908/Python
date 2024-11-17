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
        self.root.title("Database Management System")
        self.root.geometry("1540x800+0+0")
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="DATABASE MANAGEMENT SYSTEM",fg="red",bg="white",font=("Times New Roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        
    # ====================Data frame===================================
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)


        
root = Tk()
ob=Hospital(root)
root.mainloop()
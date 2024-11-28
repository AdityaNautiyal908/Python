import tkinter as tk
from tkinter import *
import mysql.connector as myConn
import os

root = tk.Tk()

root.geometry("1800x800+0+0")  # Set window size

# Title Label
lbltitle = tk.Label(bd=20, relief=RIDGE, text="CRICKET SCORE BOARD", bg="red", fg="white", font=("Times New Roman", 50, "bold"))
lbltitle.pack(side=TOP, fill=X)  # Title label fills horizontally

# Frame for content
dataframe = tk.Frame(root, bd=20, relief=RIDGE, bg="lightblue")
dataframe.place(x=0, y=130, width=1530, height=500)

# Left frame for user input
data_frame_left = tk.LabelFrame(dataframe,bd=5,relief=RIDGE,font=("Times New Roman",15,"bold"),text="Details")
data_frame_left.place(x=5,y=20,width=765,height=410)

data_frame_right = tk.LabelFrame(dataframe,bd=5,relief=RIDGE,font=("Times New Roman",15,"bold"),text="Watch")
data_frame_right.place(x=780,y=20,width=700,height=410)

# ================= Button frame ============================================

button_frame = tk.Frame(root,bd=10,relief=RIDGE,bg="lightblue")
button_frame.place(x=0,y=625,width=1530,height=50)

root.mainloop()


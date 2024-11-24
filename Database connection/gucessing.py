import tkinter as tk
from tkinter import messagebox
import mysql.connector as myConn
from tkinter import *

def db_connector():
    connection = myConn.connect(
        host = "localhost",
        user = "root",
        password = "8979826321luffy",
        database = "college"
    )
    return connection

def add_student():
    name = name_entry.get()
    roll_number = roll_number_entry.get()
    course = course_entry.get()

    try:
        if name and roll_number and course:
            connection = db_connector()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO student (name,roll_number,course) VALUES (%s,%s,%s)",(name,roll_number,course))
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success","Student details added successfully!")
            clear_field()
        else:
            messagebox.showerror("Please fill all the detail")
            
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid roll number (numeric).")
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")

def clear_field():
    name_entry.delete(0,tk.END)
    roll_number_entry.delete(0,tk.END)
    course_entry.delete(0,tk.END)

root = tk.Tk()

root.geometry("1600x800+0+0")

root.title("Student Management system")
    
lbltitle = tk.Label(bd=20,relief=RIDGE,text="STUDENT MANAGEMENT SYSTEM",fg="black",bg="white",font=("Arial",50,"bold"))
lbltitle.pack(side=TOP,fill=X)


Dataframe = Frame(bd=20,relief=RIDGE)
Dataframe.place(x=0,y=130,width=1530,height=400)

DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
font=("Arial",12,"bold"),text= "Student Infromation")
DataframeLeft.place(x=0,y=5,width=980,height=350)

# Label
lbl_name = tk.Label(Dataframe,text="Name",font=("Arial",20,"bold"))
lbl_name.grid(row=0,column=0,padx=10,pady=20,sticky="w")

# Entry
name_entry = tk.Entry(Dataframe,font=("Arial",20,"bold"))
name_entry.grid(row=0,column=1,padx=10,pady=10)

# Label
lbl_roll_number = tk.Label(Dataframe,text="Roll Number",font=("Arial",20,"bold"))
lbl_roll_number.grid(row=1,column=0,padx=10,pady=10,sticky="w")

# Entry
roll_number_entry = tk.Entry(Dataframe,font=("Arial",20,"bold"))
roll_number_entry.grid(row=1,column=1,padx=10,pady=10)

# Label
lbl_course = tk.Label(Dataframe,text="Course",font=("Arial",20,"bold"))
lbl_course.grid(row=2,column=0,padx=10,pady=10,sticky="w")

# Entry
course_entry = tk.Entry(Dataframe,font=("Arial",20,"bold"))
course_entry.grid(row=2,column=1,padx=10,pady=10)

# Add button
add_button = tk.Button(Dataframe,text="Add Student",font=("Arial",20),bg="green",fg="white",command=add_student)
add_button.grid(row=3,column=0,columnspan=2,padx=20)


root.mainloop()
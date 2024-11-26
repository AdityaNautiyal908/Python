import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector as myConn
import os
from dotenv import load_dotenv

load_dotenv()

def db_connect():
    password = os.getenv("DB_PASSWORD")
    if not password:
        raise ValueError("DB_PASSWORD environment variable is not set.")
    
    try:
        connection = myConn.connect(
            user="root",
            host="localhost",
            password=password,
            database="student_management"
        )
        return connection
    except myConn.Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise  

# Add student function
def add_student():
    name = name_entry.get()
    roll_number = roll_number_entry.get()
    course = course_entry.get()

    if name and roll_number and course:
        try:
            connection = db_connect()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO student (name, roll_number, course) VALUES (%s, %s, %s)",
                            (name, roll_number, course))
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Student added successfully")
            clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred : {e}")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")
    

# View student record function
def view_student():
    roll_number = roll_number_view_entry.get()

    if roll_number:
        try:
            connection = db_connect()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM student WHERE roll_number = %s", (roll_number,))
            student = cursor.fetchone()

            if student:
                name_label.config(text=f"Name: {student[1]}")
                roll_number_label.config(text=f"Roll Number: {student[2]}")
                course_label.config(text=f"Course: {student[3]}")
            else:
                messagebox.showerror("Not Found", "No student found with this roll number.")
            cursor.close()
            connection.close()
            clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred : {e}")
    else:
        messagebox.showerror("Error", "Please enter a roll number.")

# Delete student function
def delete_student():
    roll_number = roll_number_view_entry.get()

    if roll_number:
        try:
            connection = db_connect()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM student WHERE roll_number = %s", (roll_number,))
            connection.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Student record deleted successfully!")
                clear_fields()  # Clear fields after deletion
            else:
                messagebox.showerror("Not Found", "No student found with this roll number.")
            cursor.close()
            connection.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Error", "Please enter a roll number.")
        
# Clear fields function
def clear_fields():
    name_entry.delete(0, tk.END)
    roll_number_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    roll_number_view_entry.delete(0, tk.END)

# Main application window
root = tk.Tk()
root.title("Student Management System")
root.geometry("1600x800+0+0")

# Title label
lbltitle = tk.Label(bd=20, relief=RIDGE, text="Student Management System", fg="black", bg="White", font=("Arial", 50, "bold"))
lbltitle.pack(side=TOP, fill=X)

# Main Frame
Dataframe = Frame(bd=20, relief=RIDGE)
Dataframe.place(x=0, y=130, width=1530, height=400)

# Left Frame (Student Info)
DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("Times New Roman", 12, "bold"), text="Student Information")
DataframeLeft.place(x=0, y=5, width=980, height=350)

# Right Frame (Results)
DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("Times New Roman", 12, "bold"), text="Results")
DataframeRight.place(x=990, y=5, width=460, height=350)

# Left Frame Widgets (Student Info)
lbl_name = tk.Label(DataframeLeft, text="Name", font=("Arial", 20, "bold"))
lbl_name.grid(row=0, column=0, padx=10, pady=20, sticky="w")

name_entry = tk.Entry(DataframeLeft, font=("Arial", 20, "bold"))
name_entry.grid(row=0, column=1, padx=10, pady=10)

lbl_roll_number = tk.Label(DataframeLeft, text="Roll Number", font=("Arial", 20, "bold"))
lbl_roll_number.grid(row=1, column=0, padx=10, pady=10, sticky="w")

roll_number_entry = tk.Entry(DataframeLeft, font=("Arial", 20, "bold"))
roll_number_entry.grid(row=1, column=1, padx=10, pady=10)

lbl_course = tk.Label(DataframeLeft, text="Course", font=("Arial", 20, "bold"))
lbl_course.grid(row=2, column=0, padx=10, pady=10, sticky="w")

course_entry = tk.Entry(DataframeLeft, font=("Arial", 20, "bold"))
course_entry.grid(row=2, column=1, padx=10, pady=10)

add_button = tk.Button(DataframeLeft, text="Add Student", font=("Arial", 15), bg="green", fg="white", command=add_student, width=15, height=2)
add_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

# Right Frame Widgets (Results)
roll_number_view_label = tk.Label(DataframeRight, text="Enter Roll Number to View", font=("Arial", 15, "bold"))
roll_number_view_label.grid(row=0, column=0, padx=10, pady=20)

roll_number_view_entry = tk.Entry(DataframeRight, font=("Arial", 15, "bold"), width=10)
roll_number_view_entry.grid(row=0, column=1, padx=10, pady=10)

view_button = tk.Button(DataframeRight, text="View Student", font=("Arial", 12), bg="green", fg="white", command=view_student, width=12, height=2)
view_button.grid(row=1, column=0, padx=20, pady=10)

delete_button = tk.Button(DataframeRight, text="Delete Student", font=("Arial", 12), bg="red", fg="white", command=delete_student, width=12, height=2)
delete_button.grid(row=1, column=1, padx=20, pady=10)

# Labels for Displaying Student Info
name_label = tk.Label(DataframeRight, text="Name", font=("Arial", 15, "bold"))
name_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

roll_number_label = tk.Label(DataframeRight, text="Roll Number", font=("Arial", 15, "bold"))
roll_number_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

course_label = tk.Label(DataframeRight, text="Course", font=("Arial", 15, "bold"))
course_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

# Start the application loop
root.mainloop()



import tkinter as tk
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv
import mysql.connector as myConn
import os

load_dotenv()

# Function to connect to the database
def db_connected():
    password = os.getenv("DB_PASSWORD")
    connection = myConn.connect(
        user="root",
        host="localhost",
        password=password,
        database="college"
    )
    return connection

# Function to add students
def add_students():
    roll_number = roll_number_entry.get()
    name = name_entry.get()
    contact_number = contact_number_entry.get()
    semester = semester_entry.get()
    section = section_entry.get()
    father_name = father_name_entry.get()
    mother_name = mother_name_entry.get()

    # Validation for required fields
    if roll_number and name and contact_number and semester and section and father_name and mother_name:
        if len(contact_number) != 10 or not contact_number.isdigit():
            error_label.config(text="Please enter a valid 10-digit contact number.")            
            return
        try:
            connection = db_connected()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO students (roll_number, name, contact_number, semester, section, father_name, mother_name) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (roll_number, name, contact_number, semester, section, father_name, mother_name))
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Student details entered correctly.")
            clear_fields()
        
        except myConn.Error as e:
            messagebox.showerror("Database Error", f"Error while connecting to the database: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")
    else:
        error_label.config(text="All fields must be filled out.")

# Function to view student details by roll number
def view_students():
    roll_number = roll_number_entry.get()

    if roll_number:
        try:
            connection = db_connected()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students WHERE roll_number = %s", (roll_number,))
            student = cursor.fetchone()

            if student:
                name_label.config(text=f"Name: {student[1]}")
                roll_number_label.config(text=f"Roll Number: {student[2]}")
                contact_number_label.config(text=f"Contact Number: {student[3]}")
                semester_label.config(text=f"Semester: {student[4]}")
                section_label.config(text=f"Section: {student[5]}")
                father_name_label.config(text=f"Father Name: {student[6]}")
                mother_name_label.config(text=f"Mother Name: {student[7]}")
            else:
                messagebox.showerror("Not Found", "No student found with this roll number.")
            
            cursor.close()
            connection.close()
            clear_fields()
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Please enter a roll number.")

# Function to clear input fields
def clear_fields():
    roll_number_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    contact_number_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)
    section_entry.delete(0, tk.END)
    father_name_entry.delete(0, tk.END)
    mother_name_entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.geometry("1600x800+0+0")
root.title("Student Management System")

# Title Label
lbltitle = tk.Label(root, bd=20, relief=RIDGE, text="STUDENT MANAGEMENT SYSTEM", bg="black", fg="white", font=("Times New Roman", 50, "bold"))
lbltitle.pack(side=TOP, fill=X)

# Frame for student data entry
Dataframe = Frame(root, bd=20, relief=RIDGE)
Dataframe.place(x=0, y=130, width=1530, height=400)

# Create Entry fields for student data
roll_number_label = Label(Dataframe, text="Roll Number", font=("Times New Roman", 15))
roll_number_label.grid(row=0, column=0, padx=10, pady=10)

roll_number_entry = Entry(Dataframe, font=("Times New Roman", 15))
roll_number_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = Label(Dataframe, text="Name", font=("Times New Roman", 15))
name_label.grid(row=0, column=2, padx=10, pady=10)

name_entry = Entry(Dataframe, font=("Times New Roman", 15))
name_entry.grid(row=0, column=3, padx=10, pady=10)

contact_number_label = Label(Dataframe, text="Contact Number", font=("Times New Roman", 15))
contact_number_label.grid(row=2, column=0, padx=10, pady=10)

contact_number_entry = Entry(Dataframe, font=("Times New Roman", 15))
contact_number_entry.grid(row=2, column=1, padx=10, pady=10)

semester_label = Label(Dataframe, text="Semester", font=("Times New Roman", 15))
semester_label.grid(row=2, column=2, padx=10, pady=10)

semester_entry = Entry(Dataframe, font=("Times New Roman", 15))
semester_entry.grid(row=2, column=3, padx=10, pady=10)

section_label = Label(Dataframe, text="Section", font=("Times New Roman", 15))
section_label.grid(row=4, column=0, padx=10, pady=10)

section_entry = Entry(Dataframe, font=("Times New Roman", 15))
section_entry.grid(row=4, column=1, padx=10, pady=10)

father_name_label = Label(Dataframe, text="Father Name", font=("Times New Roman", 15))
father_name_label.grid(row=5, column=0, padx=10, pady=10)

father_name_entry = Entry(Dataframe, font=("Times New Roman", 15))
father_name_entry.grid(row=5, column=1, padx=10, pady=10)

mother_name_label = Label(Dataframe, text="Mother Name", font=("Times New Roman", 15))
mother_name_label.grid(row=6, column=0, padx=10, pady=10)

mother_name_entry = Entry(Dataframe, font=("Times New Roman", 15))
mother_name_entry.grid(row=6, column=1, padx=10, pady=10)

# Create Error Label for validation messages
error_label = Label(Dataframe, text="", fg="red", font=("Times New Roman", 12))
error_label.grid(row=7, columnspan=2, pady=10)

# Create buttons for Add and View with grid configuration
add_button = Button(Dataframe, text="Add Student",font=("Times New Roman", 15),bg="green",fg="white" ,command=add_students)
add_button.grid(row=8, column=0, padx=10, pady=10, sticky="ew")

view_button = Button(Dataframe, text="View Student", font=("Times New Roman", 15),bg="green",fg="white",command=view_students)
view_button.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

# Display Area for Student Information
DisplayFrame = Frame(root, bd=20, relief=RIDGE)
DisplayFrame.place(x=0, y=530, width=1530, height=300)

roll_number_label = Label(DisplayFrame, text="Roll Number: ", font=("Times New Roman", 15))
roll_number_label.grid(row=0, column=0, padx=10, pady=10)

name_label = Label(DisplayFrame, text="Name: ", font=("Times New Roman", 15))
name_label.grid(row=1, column=0, padx=10, pady=10)

contact_number_label = Label(DisplayFrame, text="Contact Number: ", font=("Times New Roman", 15))
contact_number_label.grid(row=2, column=0, padx=10, pady=10)

semester_label = Label(DisplayFrame, text="Semester: ", font=("Times New Roman", 15))
semester_label.grid(row=3, column=0, padx=10, pady=10)

section_label = Label(DisplayFrame, text="Section: ", font=("Times New Roman", 15))
section_label.grid(row=4, column=0, padx=10, pady=10)

father_name_label = Label(DisplayFrame, text="Father Name: ", font=("Times New Roman", 15))
father_name_label.grid(row=5, column=0, padx=10, pady=10)

mother_name_label = Label(DisplayFrame, text="Mother Name: ", font=("Times New Roman", 15))
mother_name_label.grid(row=6, column=0, padx=10, pady=10)

root.mainloop()

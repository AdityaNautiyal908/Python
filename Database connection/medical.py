import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as myConn
from tkcalendar import DateEntry
from tkinter import *
import os
from dotenv import load_dotenv
import re  

load_dotenv()

class MedicalRecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Record System")
        self.root.geometry("1800x800+0+0")  # Set window size
        
        # Establish the database connection
        password = os.getenv("DB_PASSWORD")
        self.conn = myConn.connect(
            host="localhost",  # or your MySQL server IP
            user="root",  # MySQL username
            password=password,  # MySQL password
            database="medical_records"
        )
        self.cursor = self.conn.cursor()

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.lbltitle = tk.Label(self.root, bd=20, relief=RIDGE, text="Medical Record System", bg="red", fg="white", font=("Times New Roman", 50, "bold"))
        self.lbltitle.pack(side=TOP, fill=X)  # Title label fills horizontally

        # Frame for content
        dataframe = tk.Frame(self.root, bd=20, relief=RIDGE, bg="lightblue")
        dataframe.place(x=0, y=130, width=1530, height=500)

        # Left Frame for user input
        data_frame_left = tk.LabelFrame(dataframe, bd=5, relief=RIDGE, font=("Times New Roman", 15, "bold"), text="Patient Details")
        data_frame_left.place(x=5, y=20, width=765, height=410)

        # Right Frame to display the records
        data_frame_right = tk.LabelFrame(dataframe, bd=5, relief=RIDGE, font=("Times New Roman", 15, "bold"), text="Patient Records")
        data_frame_right.place(x=780, y=20, width=700, height=410)

        # ==================== Form Fields for Left Frame ====================
        # Patient Information
        tk.Label(data_frame_left, text="First Name:").grid(row=0, column=0, padx=10, pady=10)
        self.first_name_entry = tk.Entry(data_frame_left)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(data_frame_left, text="Last Name:").grid(row=1, column=0, padx=10, pady=10)
        self.last_name_entry = tk.Entry(data_frame_left)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Use DateEntry widget for Date of Birth
        tk.Label(data_frame_left, text="Date of Birth:").grid(row=2, column=0, padx=10, pady=10)
        self.dob_entry = DateEntry(data_frame_left, width=12, date_pattern="yyyy-mm-dd")
        self.dob_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(data_frame_left, text="Gender:").grid(row=3, column=0, padx=10, pady=10)
        self.gender_combobox = ttk.Combobox(data_frame_left, values=["Male", "Female", "Other"])
        self.gender_combobox.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(data_frame_left, text="Phone:").grid(row=4, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(data_frame_left)
        self.phone_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(data_frame_left, text="Address:").grid(row=5, column=0, padx=10, pady=10)
        self.address_entry = tk.Entry(data_frame_left)
        self.address_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(data_frame_left, text="Disease:").grid(row=6, column=0, padx=10, pady=10)
        self.disease_entry = tk.Entry(data_frame_left)
        self.disease_entry.grid(row=6, column=1, padx=10, pady=10)

        tk.Label(data_frame_left, text="Treatment:").grid(row=7, column=0, padx=10, pady=10)
        self.treatment_entry = tk.Entry(data_frame_left)
        self.treatment_entry.grid(row=7, column=1, padx=10, pady=10)

        # Use DateEntry widget for Last Visit
        tk.Label(data_frame_left, text="Last Visit:").grid(row=8, column=0, padx=10, pady=10)
        self.last_visit_entry = DateEntry(data_frame_left, width=12, date_pattern="yyyy-mm-dd")
        self.last_visit_entry.grid(row=8, column=1, padx=10, pady=10)

        # ==================== Button Frame ====================================
        button_frame = tk.Frame(self.root, bd=10, relief=RIDGE, bg="lightblue")
        button_frame.place(x=0, y=625, width=1530, height=50)

        self.add_button = tk.Button(button_frame, text="Add Patient", command=self.add_patient, width=20)
        self.add_button.grid(row=0, column=0, padx=10)

        self.update_button = tk.Button(button_frame, text="Update Patient", command=self.update_patient, width=20)
        self.update_button.grid(row=0, column=1, padx=10)

        self.delete_button = tk.Button(button_frame, text="Delete Patient", command=self.delete_patient, width=20)
        self.delete_button.grid(row=0, column=2, padx=10)

        # ==================== Treeview for Patient Records ====================
        self.tree = ttk.Treeview(data_frame_right, columns=("patient_id", "first_name", "last_name", "dob", "gender", "phone", "address", "disease", "treatment", "last_visit"), show="headings")
        self.tree.pack(fill="both", padx=20, pady=20)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.replace("_", " ").title())

        self.refresh_treeview()

    def refresh_treeview(self):
        # Clear the treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch patient records from the database
        self.cursor.execute("SELECT * FROM patients")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)

    # Phone number validation function
    def validate_phone_number(self, phone_number):
        # Regex to check if the phone number is exactly 10 digits
        if re.match(r'^\d{10}$', phone_number):
            return True
        else:
            return False

    def add_patient(self):
        # Get data from form
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        dob = self.dob_entry.get_date()  # Get the date from the date picker
        gender = self.gender_combobox.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        disease = self.disease_entry.get()
        treatment = self.treatment_entry.get()
        last_visit = self.last_visit_entry.get_date()  # Get the date from the date picker

        # Validation
        if not first_name or not last_name or not dob or not gender:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Validate phone number
        if not self.validate_phone_number(phone):
            messagebox.showerror("Error", "Phone number must be exactly 10 digits.")
            return

        # Insert into the database
        query = """
        INSERT INTO patients (first_name, last_name, dob, gender, phone, address, disease, treatment, last_visit)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (first_name, last_name, dob, gender, phone, address, disease, treatment, last_visit))
        self.conn.commit()

        # Refresh Treeview
        self.refresh_treeview()

        messagebox.showinfo("Success", "Patient record added successfully!")

    def update_patient(self):
        selected_item = self.tree.selection()  # Get the selected item from the treeview
        if not selected_item:  # If no item is selected, show an error message
            messagebox.showerror("Error", "Please select a patient to update!")
            return

        patient_id = self.tree.item(selected_item)["values"][0]  # Get the patient_id from the selected row

        # Get the new values from the form fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        dob = self.dob_entry.get_date()  # Get the date from the date picker
        gender = self.gender_combobox.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        disease = self.disease_entry.get()
        treatment = self.treatment_entry.get()
        last_visit = self.last_visit_entry.get_date()  # Get the date from the date picker

        # Validate phone number
        if not self.validate_phone_number(phone):
            messagebox.showerror("Error", "Phone number must be exactly 10 digits.")
            return

        # SQL update query
        query = """
        UPDATE patients
        SET first_name = %s, last_name = %s, dob = %s, gender = %s, phone = %s, address = %s, disease = %s, treatment = %s, last_visit = %s
        WHERE patient_id = %s
        """
        self.cursor.execute(query, (first_name, last_name, dob, gender, phone, address, disease, treatment, last_visit, patient_id))
        self.conn.commit()  # Commit the changes to the database
        self.refresh_treeview()  # Refresh the treeview to reflect the changes
        messagebox.showinfo("Success", "Patient record updated successfully!")  # Show success message

    def delete_patient(self):
        selected_item = self.tree.selection()  # Get the selected item from the treeview
        if not selected_item:  # If no item is selected, show an error message
            messagebox.showerror("Error", "Please select a patient to delete!")
            return

        patient_id = self.tree.item(selected_item)["values"][0]  # Get the patient_id from the selected row

        query = "DELETE FROM patients WHERE patient_id = %s"  # SQL delete query
        self.cursor.execute(query, (patient_id,))  # Execute the delete query
        self.conn.commit()  # Commit the changes to the database
        self.refresh_treeview()  # Refresh the treeview to reflect the changes
        messagebox.showinfo("Success", "Patient record deleted successfully!")  # Show success message

# Running the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalRecordApp(root)
    root.mainloop()

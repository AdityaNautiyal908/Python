import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from dotenv import load_dotenv
import os

load_dotenv()

class CricketScoreboard:
    def __init__(self, root):
        self.root = root
        self.team_name = ""
        self.total_overs = 0
        self.score = 0
        self.wickets = 0
        self.overs = 0
        self.ball_count = 0  # Track number of balls played
        self.conn = None
        self.cursor = None
        self.match_id = None
        self.current_turn = 1  # Track player turn
        self.stage = 1  # Track the current stage of the game

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Set up the window title and size
        self.root.title("Cricket Scoreboard")
        
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size to screen width, and a fixed height
        self.root.geometry(f"{screen_width // 2}x{int(screen_height // 1.5)}")  # Adjusted height and width

        # Create a title label
        self.lbltitle = tk.Label(self.root, bd=20, relief=RIDGE, text="CRICKET SCORE BOARD", bg="black", fg="white", font=("Times New Roman", 30, "bold"))
        self.lbltitle.pack(side=TOP, fill=X)

        # Frame for content (left side: input, right side: score display)
        dataframe = tk.Frame(self.root, bd=20, relief=RIDGE, bg="lightblue")
        dataframe.place(x=0, y=100, width=screen_width-20, height=600)

        # Left frame for user input
        left_frame = tk.LabelFrame(dataframe, bd=5, relief=RIDGE, font=("Helvetica", 15, "bold"), text="Team & Match Details")
        left_frame.place(x=5, y=20, width=700, height=550)

        # Right frame for score display and match details
        right_frame = tk.LabelFrame(dataframe, bd=5, relief=RIDGE, font=("Helvetica", 15, "bold"), text="Match Details & Score")
        right_frame.place(x=720, y=20, width=700, height=550)

        # Left side input fields and buttons
        self.team_label = tk.Label(left_frame, text="Enter Team Name:", font=("Helvetica", 12))
        self.team_label.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        
        self.team_entry = tk.Entry(left_frame, width=40, font=("Helvetica", 12))
        self.team_entry.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        # Total Overs
        self.overs_label = tk.Label(left_frame, text="Enter Total Overs:", font=("Helvetica", 12))
        self.overs_label.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        
        self.overs_entry = tk.Entry(left_frame, width=40, font=("Helvetica", 12))
        self.overs_entry.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # Button for starting match
        self.start_button = tk.Button(left_frame, text="Start Match", command=self.set_team_details, width=20, height=2, font=("Helvetica", 12))
        self.start_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Button to delete selected record
        self.delete_button = tk.Button(left_frame, text="Delete Selected Record", command=self.delete_selected_record, width=20, height=2, font=("Helvetica", 12))
        self.delete_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Right side match details and score
        self.match_label = tk.Label(right_frame, text="Match ID: Not Started", font=("Helvetica", 12))
        self.match_label.pack(pady=10)

        # Now, create score-related fields for stage 2 (hidden initially)
        self.runs_label = tk.Label(right_frame, text="Enter Runs Scored (1,2,3,4, or 6):", font=("Helvetica", 12))
        
        self.runs_frame = tk.Frame(right_frame)
        self.runs_entry = tk.Entry(self.runs_frame, width=15, font=("Helvetica", 12))
        self.update_run_button = tk.Button(self.runs_frame, text="Update Run", command=self.update_score, font=("Helvetica", 12))

        self.wicket_label = tk.Label(right_frame, text="Was a Wicket Taken? (yes/no):", font=("Helvetica", 12))
        self.wicket_entry = tk.Entry(right_frame, width=40, font=("Helvetica", 12))
        self.turn_label = tk.Label(right_frame, text="Current Player Turn: 1", font=("Helvetica", 12))
        self.ball_count_label = tk.Label(right_frame, text="Balls Played: 0", font=("Helvetica", 12))

        # Buttons for score updating (hidden initially)
        self.update_score_button = tk.Button(right_frame, text="Update Score", command=self.update_score, width=20, height=2, font=("Helvetica", 12))
        self.display_score_button = tk.Button(right_frame, text="Display Score", command=self.display_score, width=20, height=2, font=("Helvetica", 12))

        # Create the treeview for displaying scores
        self.tree = ttk.Treeview(right_frame, columns=("Match ID", "Team Name", "Total Overs", "Score", "Wickets", "Overs"), show="headings", height=8)
        self.tree.pack(pady=20, padx=20, fill=BOTH)

        # Set up the column headings
        self.tree.heading("Match ID", text="Match ID")
        self.tree.heading("Team Name", text="Team Name")
        self.tree.heading("Total Overs", text="Total Overs")
        self.tree.heading("Score", text="Score")
        self.tree.heading("Wickets", text="Wickets")
        self.tree.heading("Overs", text="Overs")

        # Hide the widgets related to updating score initially
        self.hide_stage_2_widgets()

    def show_stage_2_widgets(self):
        # Show widgets for updating score
        self.runs_label.pack(pady=10)
        self.runs_frame.pack(pady=5)  # Pack the frame that contains the entry and button

        # Align the widgets horizontally using grid inside the frame
        self.runs_entry.grid(row=0, column=0, padx=10)  # Grid for the run entry field
        self.update_run_button.grid(row=0, column=1, padx=10)  # Grid for the update run button

        self.wicket_label.pack(pady=10)
        self.wicket_entry.pack(pady=5)
        self.turn_label.pack(pady=10)
        self.ball_count_label.pack(pady=10)
        self.update_score_button.pack(pady=5)
        self.display_score_button.pack(pady=5)

    def hide_stage_2_widgets(self):
        # Hide widgets for score updating
        self.runs_label.pack_forget()
        self.runs_frame.pack_forget()  # Unpack the frame that contains the entry and button
        self.wicket_label.pack_forget()
        self.wicket_entry.pack_forget()
        self.turn_label.pack_forget()
        self.ball_count_label.pack_forget()
        self.update_score_button.pack_forget()
        self.display_score_button.pack_forget()

    def connect_db(self):
        password = os.getenv("DB_PASSWORD")
        self.conn = mysql.connector.connect(
            host="localhost",  
            user="root",  
            password=password,  
            database="cricket_db"  
        )
        self.cursor = self.conn.cursor()

    def set_team_details(self):
        self.team_name = self.team_entry.get()
        self.total_overs = int(self.overs_entry.get())

        if not self.team_name or self.total_overs <= 0:
            messagebox.showerror("Invalid Input", "Please enter a valid team name and total overs.")
            return

        # Insert match details into the database and get match_id
        self.cursor.execute(""" 
            INSERT INTO match_scores (team_name, total_overs, score, wickets, overs) 
            VALUES (%s, %s, %s, %s, %s)
        """, (self.team_name, self.total_overs, self.score, self.wickets, self.overs))
        self.conn.commit()

        # Get the match_id for the current match
        self.cursor.execute("SELECT LAST_INSERT_ID()")
        self.match_id = self.cursor.fetchone()[0]

        self.match_label.config(text=f"Match ID: {self.match_id}")

        # Switch to stage 2
        self.stage = 2
        self.show_stage_2_widgets()

    def update_score(self):
        try:
            runs = int(self.runs_entry.get())  # Get the runs from the user input
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of runs (1,2,3,4, or 6).")
            return
        
        if runs not in [0,1,2,3,4,6]:  # Validating the runs input (only 1, 4, or 6)
            messagebox.showerror("Invalid Input", "Please enter 1, 4, or 6 for runs.")
            return

        wicket = self.wicket_entry.get().lower()  # Get wicket info (yes/no)

        if wicket not in ["yes", "no"]:
            messagebox.showerror("Invalid Input", "Please enter 'yes' or 'no' for wicket.")
            return

        self.score += runs
        if wicket == "yes":
            self.wickets += 1

        # Increment the ball count by 1 for each ball played
        self.ball_count += 1

        # If ball count reaches 6, increment the overs count and reset ball count
        if self.ball_count == 6:
            self.overs += 1
            self.ball_count = 0

        # Update the score in the database
        self.cursor.execute(""" 
            UPDATE match_scores 
            SET score = %s, wickets = %s, overs = %s 
            WHERE match_id = %s AND team_name = %s
        """, (self.score, self.wickets, self.overs, self.match_id, self.team_name))
        self.conn.commit()

        # Update the score on the GUI
        self.turn_label.config(text=f"Current Player Turn: {self.current_turn}")
        self.ball_count_label.config(text=f"Balls Played: {self.ball_count}")
        self.refresh_table()

        # Increment player turn
        self.current_turn += 1

    def display_score(self):
        # Display score details in the GUI
        self.score_label.config(text=f"Score: {self.score}/{self.wickets}, Overs: {int(self.overs)}.{int((self.overs % 1) * 10)}")

    def refresh_table(self):
        # Clear the table
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch data from the database and insert into table
        self.cursor.execute("SELECT * FROM match_scores")
        rows = self.cursor.fetchall()

        for row in rows:
            self.tree.insert("", "end", values=row)

    def delete_selected_record(self):
        # Get selected record from treeview
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showerror("No Selection", "Please select a record to delete.")
            return

        # Get the match_id of the selected record
        match_id = self.tree.item(selected_item)["values"][0]

        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete match ID: {match_id}?")
        
        if confirm:
            # Delete from the database
            self.cursor.execute("DELETE FROM match_scores WHERE match_id = %s", (match_id,))
            self.conn.commit()

            # Refresh the table
            self.refresh_table()

def main():
    root = tk.Tk()
    scoreboard = CricketScoreboard(root)
    scoreboard.connect_db()
    root.mainloop()

if __name__ == "__main__":
    main()


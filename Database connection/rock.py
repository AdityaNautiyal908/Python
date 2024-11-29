import tkinter as tk
import mysql.connector
import random
from tkinter import ttk

# Establishing connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8979826321luffy",
    database="rock_paper_scissors_db"  
)

# Creating a cursor object using the cursor() method
my_cursor = mydb.cursor()

# Create the game_results table if it doesn't exist
my_cursor.execute("CREATE TABLE IF NOT EXISTS game_results (id INT AUTO_INCREMENT PRIMARY KEY, player_choice VARCHAR(10), computer_choice VARCHAR(10), result VARCHAR(10))")

# Function to insert game result into the database
def insert_game_result(player_choice, computer_choice, result):
    sql = "INSERT INTO game_results (player_choice, computer_choice, result) VALUES (%s, %s, %s)"

    val = (player_choice, computer_choice, result)
    my_cursor.execute(sql, val)
    mydb.commit()

# Function to determine game result
def determine_result(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
        insert_game_result(player_choice, computer_choice, "Tie")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result_label.config(text="You win!")
        insert_game_result(player_choice, computer_choice, "Win")
    else:
        result_label.config(text="Computer wins!")
        insert_game_result(player_choice, computer_choice, "Loss")

    update_scoreboard()

# Function to update the scoreboard
def update_scoreboard():

    scoreboard.delete(*scoreboard.get_children())
    my_cursor.execute("SELECT * FROM game_results")
    rows = my_cursor.fetchall()
    for row in rows:
        scoreboard.insert('', 'end', values=row)

# Function handlers for user choices
def on_rock():
    determine_result("Rock")

def on_paper():
    determine_result("Paper")

def on_scissors():
    determine_result("Scissors")

# GUI setup using tkinter
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

rock_button = tk.Button(root, text="Rock", width=10, command=on_rock)
rock_button.pack()

paper_button = tk.Button(root, text="Paper", width=10, command=on_paper)

paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", width=10, command=on_scissors)
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Scoreboard setup using Treeview
scoreboard = ttk.Treeview(root, columns=('ID', 'Player Choice', 'Computer Choice', 'Result'), show='headings')
scoreboard.heading('ID', text='ID')
scoreboard.heading('Player Choice', text='Player Choice')
scoreboard.heading('Computer Choice', text='Computer Choice')
scoreboard.heading('Result', text='Result')
scoreboard.pack()

update_scoreboard()  # Update the scoreboard initially

root.mainloop()


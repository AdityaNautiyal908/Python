import tkinter as tk
import random

def get_computer_choice():
    """Randomly returns computer's choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the game rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    """Handles the game logic and displays the result in the GUI."""
    # Get computer's choice
    computer_choice = get_computer_choice()
    
    # Update computer's choice label
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    
    # Update result label
    result_label.config(text=result)

# Set up the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Add a label for instructions
instructions_label = tk.Label(window, text="Choose Rock, Paper, or Scissors!", font=('Arial', 14))
instructions_label.pack(pady=10)

# Button for Rock with color
rock_button = tk.Button(window, text="Rock", width=20, height=2, font=('Arial', 12), 
                        command=lambda: play_game("rock"), bg='lightblue', fg='black')
rock_button.pack(pady=5)

# Button for Paper with color
paper_button = tk.Button(window, text="Paper", width=20, height=2, font=('Arial', 12),
                         command=lambda: play_game("paper"), bg='lightgreen', fg='black')
paper_button.pack(pady=5)

# Button for Scissors with color
scissors_button = tk.Button(window, text="Scissors", width=20, height=2, font=('Arial', 12),
                            command=lambda: play_game("scissors"), bg='lightcoral', fg='black')
scissors_button.pack(pady=5)

# Label to display the computer's choice
computer_choice_label = tk.Label(window, text="Computer chose: ", font=('Arial', 12))
computer_choice_label.pack(pady=10)

# Label to display the result (winner or tie)
result_label = tk.Label(window, text="Make your choice!", font=('Arial', 12))
result_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()

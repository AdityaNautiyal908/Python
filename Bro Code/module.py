import random

options = ("rock","paper","scissor")
running = True

while running:
    print("--------------  Rock paper Scissor Game ---------------------")
    player = input("Enter your choice (rock/paper/scissor) (q to quite) : ").lower()
    computer = random.choice(options)
    print(f"Player choice : {player}")
    print(f"Computer choice {computer}")
    if player.isdigit():
        print("Please enter only valid input")    
    elif player in options:
        if player == computer:
            print("Match is Tie")
        elif player == "rock" and computer == "scissor":
            print("Player Win")
        elif player == "paper" and computer == "rock":
            print("Player Win")
        elif player == "scissor" and computer == "paper":
            print("Player Win")
        else:
            print("Computer Win")
    elif player == 'q':
        break
    else:
        print("Invalid choice")
    


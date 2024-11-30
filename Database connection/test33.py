import random
options = ("rock","paper","scissor")
running = True

while running:
    print("------------------------------------")
    print("--------ROCK PAPER SCISSOR GAME--------")
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock,paper,scissor) : ").lower()


    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It'a TIE")

    elif player == "rock" and computer == "scissor":
        print("You WIN!")

    elif player == "paper" and computer == "rock":
        print("You WIN!")

    elif player == "scissor" and computer == "paper":
        print("You WIN!")

    else:
        print("You LOSE!")
        
    play_again = input("Do you want to play again (y/n) : ").lower()
    if play_again != 'y':
        break
    
    print("----------------------------------------")


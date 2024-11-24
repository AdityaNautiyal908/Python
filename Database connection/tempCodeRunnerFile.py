import random

# Function to start the game
def start_game():
    print("+--------------------------------------------+")
    print("|            Start the Game                 |")
    print("+--------------------------------------------+")

    while True:
        # Generate a random number between 1 and 10
        game_number = random.randint(1, 10)
        print("\nWelcome to the Number Guessing Game!")
        print("I have selected a random number between 1 and 10.")
        
        # While the game is running, continue prompting the user
        while True:
            # Prompt the user for input (their guess)
            guess = input("Enter your guess: ")

            # Check if the user input is a valid number
            if guess.isdigit():
                guess = int(guess)

                # Check if the guess is correct
                if guess == game_number:
                    print("You guessed it right!")
                    break  # Exit the loop after the correct guess

                elif guess < game_number:
                    print("Too low, try again!")
                else:
                    print("Too high, try again!")

            else:
                print("Please enter a valid number.")

        # Ask if the user wants to play again (Yes/No)
        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != 'y':
            print("+-----------------------+")
            print("|     End the game      |")
            print("+-----------------------+")
            break  # Exit the outer loop and end the game

# Start the game
start_game()


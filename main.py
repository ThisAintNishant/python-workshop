from enum import Enum
import random

class Choice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

# Define a dictionary to determine the winning choice for each option
winning_choices = {
    Choice.ROCK: Choice.SCISSORS,
    Choice.PAPER: Choice.ROCK,
    Choice.SCISSORS: Choice.PAPER
}

# Define a function to play a single round of the game
def play_round():
    # Get user input
    user_choice_str = input("Enter your choice (rock/paper/scissors): ").upper()
    while user_choice_str not in Choice.__members__:
        user_choice_str = input("Invalid choice. Please enter rock/paper/scissors: ").upper()
    user_choice = Choice[user_choice_str]

    # Generate computer choice
    computer_choice = random.choice(list(Choice))

    # Determine winner
    if user_choice == computer_choice:
        print("Tie!")
    elif winning_choices[user_choice] == computer_choice:
        print("You win!")
    else:
        print("Computer wins!")

# Play the game
while True:
    play_round()
    play_again = input("Play again? (y/n)").lower()
    if play_again != 'y':
        break

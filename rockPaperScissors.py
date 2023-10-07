# import random module
import random

# Welcome to Rock, Paper, Scissors!
print("Welcome to Rock, Paper, Scissors!\n")
print("Your options are:\n")

# list of actions
actions = ["Rock", "Paper", "Scissors"]

for action in actions:
    print('- ' + action)

# player pick
player_pick = input("\nEnter your selection: ").lower()  # Convert input to lowercase

# randomize computer pick
computer_pick = random.choice(actions)

# Compare player pick with computer pick

# conditional statement
# if player and computer pick are the same
if player_pick == computer_pick.lower():  # Convert computer_pick to lowercase for comparison
    print(f"Both players selected {player_pick}. It's a tie!")

# if player picks Rock
elif player_pick == "rock":
    if computer_pick == "Paper":
        print(f"Computer picked {computer_pick}, you picked {player_pick}. {computer_pick} beats {player_pick}. You Lose!")
    else:
        print(f"Computer picked {computer_pick}, you picked {player_pick}. {player_pick} beats {computer_pick}. You Win!")

# if player picks Paper
elif player_pick == "paper":
    if computer_pick == "Rock":
        print(f"Computer picked {computer_pick}, you picked {player_pick}. {player_pick} beats {computer_pick}. You Win!")
    else:
        print(f"Computer picked {computer_pick}, you picked {player_pick}. {player_pick} beats {computer_pick}. You Lose!")

# if player picks Scissors
elif player_pick == "scissors":
    if computer_pick == "Rock":
        print(f"Computer picked {computer_pick}, you picked {player_pick}. {computer_pick} beats {player_pick}. You Lose!")
    else:
        print(f"Computer picked {computer_pick}, you picked {player_pick}. {player_pick} beats {computer_pick}. You Win!")

# Handle invalid user input
else:
    print("Invalid selection. Please choose Rock, Paper, or Scissors.")

#Line 1-2: Imports the random module and creates a list of valid game options.
import random
Options = ["rock", "paper", "scissors"]

#function (lines 4-8):
#Asks the player to input their choice (rock, paper, or scissors)
#The computer randomly picks from the options
#Returns both choices as a dictionary with "Player" and "Computer" keys

def get_choices():
    Player_choice = input("Enter your choice (rock, paper, scissors): ")
    Computer_choice = random.choice(Options)
    Choices = {"Player": Player_choice, "Computer": Computer_choice}
    return Choices
#function (lines 11-27):
#Prints what both the player and computer chose
#Checks all possible game outcomes:
#If both chose the same → tie
#If player chose rock → beats scissors, loses to paper
#If player chose paper → beats rock, loses to scissors
#If player chose scissors → beats paper, loses to rock
#Returns a message describing the result

def check_winner(Player, Computer):
   print(f"You chose  {Player}  , computer chose  {Computer} .")
   if Player == Computer:
       return "It's a tie!"
   # Check all win/lose conditions
   if Player == "rock":
       if Computer == "scissors":
           return "Rock smashes scissors! You win!"
       else:
           return "Paper covers rock! You lose!"
   if Player == "paper":
       if Computer == "rock":  
           return "Paper covers rock! You win!"
       else:
           return "Scissors cuts paper! You lose!"
   if Player == "scissors":
       if Computer == "paper":
           return "Scissors cuts paper! You win!"
       else:
           return "Rock smashes scissors! You lose!"

#Main program (lines 30-32):
choices = get_choices()
result = check_winner(choices["Player"], choices["Computer"])
print(result)
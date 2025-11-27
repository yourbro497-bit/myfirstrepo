import random
Options = ["rock", "paper", "scissors"]

def get_choices():
    Player_choice = input("Enter your choice (rock, paper, scissors): ")
    Computer_choice = random.choice(Options)
    Choices = {"Player": Player_choice, "Computer": Computer_choice}
    return Choices

def check_winner(Player, Computer):
   print(f"You chose  {Player}  , computer chose  {Computer} .")
   if Player == Computer:
       return "It's a tie!"
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

# Main game loop
choices = get_choices()
result = check_winner(choices["Player"], choices["Computer"])
print(result)
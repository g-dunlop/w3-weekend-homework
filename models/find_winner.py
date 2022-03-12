from models.player import Player
import random

# player1 = Player("Bill", "rock")
# player2 = Player("Tom", "paper")

# players = [player1, player2]

def play(player1, player2):
    if player1.choice == player2.choice:
        return None
    if player1.choice == "scissors": 
        if player2.choice == "paper":
            return player1
        else:
            return player2
    if player1.choice == "paper": 
        if player2.choice == "rock":
            return player1
        else:
            return player2
    if player1.choice == "rock": 
        if player2.choice == "scissors":
            return player1
        else:
            return player2
        
def generate_choice():
    choices=["rock", "paper", "scissors"]
    choice=choices[random.randint(0,2)]
    return choice

    
    
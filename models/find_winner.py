from models.player import Player

player1 = Player("Bill", "paper")
player2 = Player("Tom", "rock")

players = [player1, player2]

def play(player1, player2):
    if player1.choice == "scissors": 
        if player2.choice == "paper":
            return f"player 1 wins with {player1.choice}"
        else:
            return f"player 2 wins with {player2.choice}"
    if player1.choice == "paper": 
        if player2.choice == "rock":
            return f"player 1 wins with {player1.choice}"
        else:
            return f"player 2 wins with {player2.choice}"
    if player1.choice == "rock": 
        if player2.choice == "scissors":
            return f"player 1 wins with {player1.choice}"
        else:
            return f"player 2 wins with {player2.choice}"

    
    
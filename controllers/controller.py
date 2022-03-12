from flask import render_template, request
from app import app
from models.find_winner import *
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/game')
def show_game():
    return render_template('game.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title="Welcome")

@app.route('/two_player')
def enter_details():
    return render_template('two_player.html', title="2 player" )

@app.route('/versus_computer')
def enter_details_vcomp():
    return render_template('versus_computer.html', title="1 player" )

@app.route('/game', methods = ['POST'])
def play_game():
    player1_name = request.form["p1name"]
    player1_choice = request.form["p1choice"]
    player2_name = request.form["p2name"]
    player2_choice = request.form["p2choice"]
    print(player2_choice)
    player1 = Player(player1_name, player1_choice)
    player2 = Player(player2_name, player2_choice)
    winner = play(player1, player2)
    increase_score(winner, player1, player2)
    return render_template("game.html", title='winner', winner=winner, player1=player1, player2=player2)

@app.route('/game_1p', methods = ['POST'])
def play_game_1p():
    player1_name = request.form["p1name"]
    player1_choice = request.form["p1choice"]
    player2 = generate_computer_player()
    player1 = Player(player1_name, player1_choice)
    winner = play(player1, player2)
    increase_score(winner, player1, player2)
    
    return render_template("game_1p.html", title="winner", winner=winner, player1=player1, player2=player2)
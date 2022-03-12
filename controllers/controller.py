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
    return render_template('two_player.html', title="play" )

@app.route('/game', methods = ['POST'])
def play_game():
    player1_name = request.form["p1name"]
    player1_choice = request.form["p1choice"]
    player2_name = request.form["p2name"]
    player2_choice = request.form["p2choice"]
    player1 = Player(player1_name, player1_choice)
    player2 = Player(player2_name, player2_choice)
    print(player1.name)
    print(player2.name)
    winner = play(player1, player2)
    return render_template("game.html", title='winner', winner=winner, player1=player1, player2=player2)
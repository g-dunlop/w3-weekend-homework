from flask import render_template
from app import app
from models.find_winner import *
from models.player import Player

@app.route('/Home')
def index():
    return render_template('index.html', title='Home', players=players)
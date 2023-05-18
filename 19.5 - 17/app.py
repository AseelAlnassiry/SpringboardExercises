from boggle import Boggle
from flask import Flask, session, render_template, request

# Flask initializers
app = Flask(__name__)
app.secret_key = "BLACKDHALIA"

# Game initializers
boggle_game = Boggle()


# Routers
@app.route("/")
def index():
    game_board = boggle_game.make_board()
    session["board"] = game_board
    return render_template("index.html", game_board=game_board)



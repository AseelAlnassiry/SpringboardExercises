"""Blogly application."""

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db

app = Flask(__name__)

app.secret_key = "PROWLERCAR"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

toolbar = DebugToolbarExtension(app)

db.init_app(app)


@app.route("/")
def index():
    return render_template('index.html')

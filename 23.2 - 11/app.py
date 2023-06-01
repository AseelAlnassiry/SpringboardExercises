from flask import Flask, session, request, flash, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Post

app = Flask(__name__)
app.secret_key = "PROWLERCAR"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUT_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_ECHO"] = False

app.debug = True
# toolbar = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def index():
    # block o code
    return render_template('index.html')

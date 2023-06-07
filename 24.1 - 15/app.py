from flask import Flask, session, request, render_template, flash
from models import db, connect_db, Pet

app = Flask(__name__)
app.secret_key = "PROWLERCAR"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUT_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_RECORD_QUERIES"] = True

connect_db(app)


@app.route("/")
def index():
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

from flask import Flask, render_template, request
from models import Cupcake, connect_db, db

app = Flask(__name__)
app.secret_key = "PROWLERCAR"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUT_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_RECORD_QUERIES"] = True

connect_db(app)


from flask import Flask, jsonify, render_template, request
from models import Cupcake, connect_db, db

app = Flask(__name__)
app.secret_key = "PROWLERCAR"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUT_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_RECORD_QUERIES"] = True

connect_db(app)


@app.get("/api/cupcakes")
def get_all_cupcakes():
    res = Cupcake.query.all()
    serialized = [Cupcake.serialize(d) for d in res]
    return jsonify(cupcakes=serialized)

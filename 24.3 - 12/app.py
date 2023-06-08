from flask import Flask, jsonify, render_template, request
from models import Cupcake, connect_db, db

app = Flask(__name__)
app.app_context().push()
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


@app.post("/api/cupcakes")
def add_one_cupcake():
    flavor = request.form["flavor"]
    size = request.form["size"]
    rating = request.form["rating"]
    image = request.form["image"]

    if image:
        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    else:
        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating)
    db.session.add(new_cupcake)
    db.session.commit()
    serialized = Cupcake.serialize(new_cupcake)
    return jsonify(cupcake=serialized)


@app.get("/api/cupcakes/<int:id>")
def get_one_cupcake(id):
    res = Cupcake.query.get(id)
    serialized = Cupcake.serialize(res)
    return jsonify(cupcake=serialized)

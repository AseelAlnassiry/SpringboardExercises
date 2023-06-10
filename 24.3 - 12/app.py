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


# FRONTEND
@app.route("/")
def index():
    return render_template("index.html")


# BACKEND


@app.get("/api/cupcakes")
def get_all_cupcakes():
    res = Cupcake.query.all()
    serialized = [Cupcake.serialize(d) for d in res]
    return jsonify(cupcakes=serialized)


@app.post("/api/cupcakes")
def add_one_cupcake():
    data = request.json
    flavor = data["flavor"]
    size = data["size"]
    rating = data["rating"]
    image = data.get("image", None)
    print(flavor, size, rating)
    if image:
        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    else:
        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating)
    db.session.add(new_cupcake)
    db.session.commit()
    serialized = Cupcake.serialize(new_cupcake)
    return (jsonify(cupcake=serialized), 201)


@app.get("/api/cupcakes/<int:id>")
def get_one_cupcake(id):
    try:
        res = Cupcake.query.get(id)
        serialized = Cupcake.serialize(res)
        return jsonify(cupcake=serialized)
    except:
        msg = {"message": "unable to find cupcake based on id"}
        return (jsonify(msg), 404)


@app.patch("/api/cupcakes/<int:id>")
def patch_one_cupcake(id):
    try:
        cupcake = Cupcake.query.get(id)
        data = request.json
        cupcake.flavor = data["flavor"]
        cupcake.size = data["size"]
        cupcake.rating = data["rating"]
        cupcake.image = data["image"]
        db.session.add(cupcake)
        db.session.commit()
        serialized = Cupcake.serialize(cupcake)
        return jsonify(cupcake=serialized)
    except:
        return ("unable to find/update cupcake", 404)


@app.delete("/api/cupcakes/<int:id>")
def delete_one_cupcake(id):
    try:
        res = Cupcake.query.get(id)
        db.session.delete(res)
        db.session.commit()
        msg = {"message": "Deleted"}
        return jsonify(msg, 200)
    except:
        return ("unable to find cupcake", 404)

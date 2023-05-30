"""Blogly application."""

from flask import Flask, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, User

app = Flask(__name__)

app.secret_key = "PROWLERCAR"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

toolbar = DebugToolbarExtension(app)

db.init_app(app)


@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)


@app.post("/users")
def add_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")


@app.get("/users/<user_id>")
def show_user(user_id):
    curr_user = User.query.get(user_id)
    return render_template("user.html", user=curr_user)


@app.post("/users/<user_id>/delete")
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")


@app.get("/users/<user_id>/edit")
def edit_form(user_id):
    user = User.query.get(user_id)
    return render_template("edit.html", user=user)


@app.post("/users/<user_id>/edit")
def edit_user (user_id):
    user = User.query.get(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]
    db.session.add(user)
    db.session.commit()
    return redirect(f"/users/{user.id}")

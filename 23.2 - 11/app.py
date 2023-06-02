from flask import Flask, redirect, session, request, flash, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Post

app = Flask(__name__)
app.secret_key = "PROWLERCAR"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUT_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.debug = True
toolbar = DebugToolbarExtension(app)

connect_db(app)


@app.get("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)


@app.get("/users/<user_id>")
def user_page(user_id):
    user = User.query.get(user_id)
    return render_template("user.html", user=user)


@app.get("/users/<user_id>/edit")
def user_edit_page(user_id):
    user = User.query.get(user_id)
    return render_template("user-edit.html", user=user)


@app.post("/users/<user_id>/edit")
def user_edit_request(user_id):
    user = User.query.get(user_id)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url
    db.session.add(user)
    db.session.commit()
    return redirect("/")


@app.get("/posts/<user_id>/new")
def new_post_form(user_id):
    return render_template("new-post.html", user_id=user_id)


@app.post("/posts/<user_id>/new")
def add_post(user_id):
    title = request.form["title"]
    content = request.form["content"]
    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f"/users/{user_id}")


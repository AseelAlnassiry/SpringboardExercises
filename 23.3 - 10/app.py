from flask import Flask, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, User

app = Flask(__name__)
app.app_context().push()
app.secret_key = "PROWLERCAR"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUT_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_RECORD_QUERIES"] = True

connect_db(app)


@app.route("/")
def index():
    return redirect("/users")


@app.route("/users")
def all_users():
    users = User.query.all()
    return render_template("index.html", users=users)


@app.get("/users/new")
def add_user_form():
    return render_template("add_user_form.html")


@app.post("/users/new")
def post_new_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form.get("image_url", None)
    if image_url:
        new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    else:
        new_user = User(first_name=first_name, last_name=last_name)
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")


@app.get("/users/<int:user_id>")
def user_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user.html", user=user)


@app.get("/users/<int:user_id>/edit")
def edit_user_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit_user_form.html", user=user)


@app.post("/users/<int:user_id>/edit")
def edit_user_post(user_id):
    user = User.query.get_or_404(user_id)
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url
    db.session.add(user)
    db.session.commit()
    return redirect(f"/users/{user_id}")


@app.post("/users/<int:user_id>/delete")
def user_delete(user_id):
    User.query.filter(User.id == user_id).delete()
    db.session.commit()
    return redirect("/")

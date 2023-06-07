from flask import Flask, session, request, render_template, flash, redirect
from models import db, connect_db, Pet
from forms import AddPetForm

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
    pets = Pet.query.order_by(Pet.id).all()
    return render_template("index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(
            name=name, species=species, photo_url=photo_url, age=age, notes=notes
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:id>", methods=["GET", "POST"])
def edit_pet_form(id):
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_form.html", form=form, pet=pet)

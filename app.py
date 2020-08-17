from flask import Flask, request, render_template, redirect, flash, session, url_for
from form import AddPetForm, EditPetForm
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "SECRET!"

connect_db(app)


@app.route('/')
def home():
    return redirect('/pets')


@app.route('/pets', methods=["GET", "POST"])
def show_pets():
    pets = Pet.query.order_by(Pet.name).all()
    return render_template("home.html", pets=pets)


@app.route('/pets/new', methods=["GET", "POST"])
def add_pet_form():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url,
                  age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} added")
        return redirect('/pets')
    else:
        return render_template("add_pet.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated")
        return redirect('/pets')

    else:
        return render_template("pet_edit_form.html", form=form, pet=pet)

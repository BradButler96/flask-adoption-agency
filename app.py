from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "Dog12345"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def homepage():
    pets = Pet.query.all()

    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def pet_add():
    """Displays and handles add pet form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data 
        age = form.age.data
        notes = form.notes.data

# If photo url is submitted update the url, otherwise set it to default value
        if form.photo_url.data:
            db.session.add(Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes))
            db.session.commit()
        else:
            db.session.add(Pet(name=name, species=species, age=age, notes=notes))
            db.session.commit()

        flash(f"You have successfully added { name }")
        return redirect("/")
    else:
        return render_template('pet-add.html', form=form)

@app.route('/<int:pet_id>')
def pet_page(pet_id):
    """Displays pet info page"""

    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet.html', pet=pet)

@app.route('/<int:pet_id>/edit', methods=["GET", "POST"])
def pet_edit(pet_id):
    """Displays and handles edit pet form"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

# Set pet age, notes and availability to form values
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

# If photo url is submitted update the url, otherwise set it to current value
        if form.photo_url.data:
            pet.photo_url = form.photo_url.data 
        else:
            pet.photo_url = pet.photo_url

        db.session.commit()

        flash(f"You have successfully edited { pet.name }")
        return redirect(f"/{ pet_id }")
    else:
        return render_template('pet-edit.html', pet=pet, form=form)


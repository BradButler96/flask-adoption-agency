from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired(message="Name cannot be blank")])
    species = StringField("Species", validators=[InputRequired(message="Species cannot be blank")])
    photo_url = StringField("Image Link", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?", default=True)

class EditPetForm(FlaskForm):
    """Form for adding pets"""

    photo_url = StringField("Image Link", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?", default=True)
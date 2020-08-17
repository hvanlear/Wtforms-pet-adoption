from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(
        message="Pet Name field cannot be blank")])
    species = SelectField("Pet Species", choices=[
                          ("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Pet Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Pet Age", validators=[
                       Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Additional Pet Notes")


class EditPetForm(FlaskForm):
    """ For for ediditn an existing pet:"""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional()])
    available = BooleanField("Available for Adoption?")

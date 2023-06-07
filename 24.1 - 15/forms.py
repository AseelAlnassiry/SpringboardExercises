from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf


class AddPetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    species = StringField(
        "Species", validators=[InputRequired(), AnyOf(["cat", "dog", "porcupine"])]
    )
    photo_url = StringField("Image Link", validators=[Optional(), URL()])
    age = FloatField("Age", validators=[InputRequired(), NumberRange(0, 30)])
    notes = TextAreaField("Notes", validators=[Optional()])

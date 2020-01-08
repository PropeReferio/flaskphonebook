from wtforms import Stringfield, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_wtf import FlaskForm

class BookEntry(FlaskForm):
    avenger = StringField("Avenger", validators=[DataRequired()])
    address = Stringfield("Address", validators=[DataRequired()])
    phone = Stringfield("Phone Number", validators=[DataRequired()])
    submit = SubmitField("Submit")
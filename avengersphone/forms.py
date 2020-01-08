from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_wtf import FlaskForm

class BookEntry(FlaskForm):
    avenger = StringField("Avenger", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    phone = StringField("Phone Number", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    avenger = StringField("Avenger", validators=[DataRequired()])
    phone = PasswordField("Phone", validators=[DataRequired()])
    submit = SubmitField("Submit")
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, length
from flask_wtf import FlaskForm

class BookEntry(FlaskForm):
    avenger = StringField("Avenger", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    phone = StringField("Phone Number", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm): 
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Submit")
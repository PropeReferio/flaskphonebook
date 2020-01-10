from flask_sqlalchemy import SQLAlchemy
from avengersphone import app, db
from werkzeug.security import generate_password_hash
from datetime import datetime

#Import User Mixin
from avengersphone import login #Is it called the same here??
from flask_login import UserMixin

@login.user_loader
def load_user(user_id): #Careful, I renamed it here
    return User.query.get(int(user_id))

class Entry(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    avenger = db.Column(db.String(30), nullable = False)
    address = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,avenger,address,phone):
        self.avenger = avenger
        self.address = address
        self.phone = phone

    def __repr__(self):
        return 'An entry has been made for {}'.format(self.avenger)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    post = db.relationship('Entry', backref = 'author', lazy = True)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password, salt_length=10)
        return self.pw_hash

    def __repr__(self):
        return '{} has been created'.format(self.username)

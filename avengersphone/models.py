from flask_sqlalchemy import SQLAlchemy
from avengersphone import app, db
from werkzeug.security import generate_password_hash
from datetime import datetime

#Import User Mixin
from avengersphone import login #Is it called the same here??
from flask_login import UserMixin

@login.user_loader
def load_entry(user_id): #Careful, I renamed it here
    return Entry.query.get(int(user_id))

class Entry(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    avenger = db.Column(db.String(30), nullable = False)
    address = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(12), nullable=False)

    def __init__(self,avenger,address,phone):
        self.avenger = avenger
        self.address = address
        self.phone = phone

    def __repr__(self):
        return 'An entry has been made for {}'.format(self.avenger)
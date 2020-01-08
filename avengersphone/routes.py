from avengersphone import app, db
from flask import render_template, request, redirect, url_for
from avengersphone.forms import BookEntry, LoginForm

#From Werkzeug for Security Import
from werkzeug.security import check_password_hash

#Import for Flask-Login
from flask_login import login_user, current_user

#User Model Import
from avengersphone.models import Entry ### Create models.py first!!!

#Home Route
@app.route("/")
def home():
    return render_template("home.html")
    
#Phone Book Entry Route
@app.route("/phonebookentry", methods=["GET", "POST"])
def addEntry():
    bookEntry = BookEntry()
    if request.method == "POST":
        avenger = bookEntry.avenger.data
        address = bookEntry.address.data
        phone = bookEntry.phone.data
        print(avenger, address, phone)
        entry = Entry(avenger,address,phone)
        db.session.add(entry)
        db.session.commit()

    return render_template("phonebookentry.html",bookentry = bookEntry)

#Come back for login once successfully committing to database
#Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if request.method == 'POST':
        avenger = loginForm.avenger.data
        phone = loginForm.phone.data
        logged_user = Entry.query.filter(Entry.avenger == avenger).first()
        if logged_user:
            login_user(logged_user)
            print(current_user.avenger) #or .username??
            return redirect(url_for('home'))

    else:
        print("Not Valid Method")
    return render_template('login.html', loginform=loginForm)
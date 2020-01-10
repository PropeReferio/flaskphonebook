from avengersphone import app, db
from flask import render_template, request, redirect, url_for
from avengersphone.forms import BookEntry, LoginForm, SignupForm

#From Werkzeug for Security Import
from werkzeug.security import check_password_hash

#Import for Flask-Login
from flask_login import login_user, current_user, login_required

#User Model Import
from avengersphone.models import User, Entry ### Create models.py first!!!

#Home Route
@app.route("/")
def home():
    return render_template("home.html")
    
#Phone Book Entry Route
@app.route("/phonebookentry", methods=["GET", "POST"])
@login_required
def addEntry():
    bookEntry = BookEntry()
    avenger = bookEntry.avenger.data
    address = bookEntry.address.data
    phone = bookEntry.phone.data
    user_id = current_user.id
    print(avenger, address, phone)
    entry = Entry(avenger = avenger,address = address,phone = phone,user_id = user_id)
    db.session.add(entry)
    db.session.commit()

    return render_template("phonebookentry.html",bookentry = bookEntry)

#Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if request.method == 'POST':
        user_email = loginForm.email.data
        password = loginForm.password.data
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username) #or .username??
            return redirect(url_for('home'))

    else:
        print("Not Valid Method")
    return render_template('login.html', loginform=loginForm)

#Signup Route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    signupForm = SignupForm()
    if request.method == "POST":
        username = signupForm.username.data
        email = signupForm.email.data
        password = signupForm.password.data
        print(username, email, password)
        #Add form data to User Model Class(AKA Database)
        #First import User Model(at top)
        #Second - Open a database session, then add our data
        user = User(username,email,password)
        db.session.add(user) #Start communication with database
        db.session.commit()

    return render_template("signup.html",signupform = signupForm)

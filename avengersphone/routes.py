from avengersphone import app
from flask import render_template
from avengersphone.forms import BookEntry

#Home Route
@app.route("/")
def home():
    return render_template("home.html")
    
#Phone Book Entry Route
@app.route("/phonebookentry", methods=["GET", "POST"])
def addEntry():
    bookEntry = BookEntry()
    avenger = bookEntry.avenger.data
    address = bookEntry.address.data
    phone = bookEntry.phone.data
    print(avenger, address, phone)
    return render_template("phonebookentry.html",bookentry = bookEntry)
import os
import json
from flask import (
    Flask, flash, render_template, request, redirect, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from requests.exceptions import HTTPError
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI_BOOKS')
app.config['API_KEY'] = os.environ.get('API_KEY')
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

API_KEY = os.environ.get('API_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
MONGO_URI = os.environ.get('MONGO_URI_BOOKS')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')


@app.route('/')
@app.route('/get_home')
def get_home():
    return render_template(
        "index.html", 
        featured=mongo.db.feature_books.find())


@app.route("/book_search", methods=["GET", "POST"])
def book_search():
    return render_template("book_search.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        ## check if username already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("reg-email")})
        existing_display_name = mongo.db.users.find_one(
            {"display_name": request.form.get(
                "create-display-name")})

        if existing_email:    
            flash("Email already exists")
            return redirect({{ url_for("register") }})


        elif existing_display_name:
            flash("Display Name already exists")
            return redirect({{ url_for("register") }})

        else:
            register = {
                "email": request.form.get("reg-email"),
                "password": generate_password_hash(request.form.get(
                    "create-password")),
                "display_name": request.form.get("create-display-name")
            }
            mongo.db.insert_one(register)

            #put the new user into the 'session" cookie
            session["email"] = request.form.get("email")
            flash("Account Creation Successful")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        ## check if username already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if existing_email:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_email["password"], request.form.get("password")):
                session["email"] = request.form.get("email")
                flash("Welcome, {}".format(request.form.get("email")))
            else:
                #invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            #username doesn't exist 
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

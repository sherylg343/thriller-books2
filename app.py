import os
import requests
import json
import shutil
from flask import (
    Flask, flash, render_template, request, redirect, url_for, session)
from flask_pymongo import PyMongo
from requests.exceptions import HTTPError
from bson.objectid import ObjectId
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
    get_feature_image()
    return render_template(
        "index.html",
        featured=mongo.db.feature_books.find())


@app.route('/')
@app.route('/get_feature_image')
def get_feature_image():
    check_images = mongo.db.feature_books.find()
    for image in check_images:
        if image["image"] == "":
            isbn = image["isbn"]
            url = 'https://www.googleapis.com/books/v1/volumes?q=' + isbn + ":isbn" + '&key=' + API_KEY
        # from pynative.com/parse-json-response-
        # #using-python-requests-library/
            try:
                response = requests.get(url)
                response.raise_for_status()
                j_response = response.json()

                for x in range(1):
                    cover_img = j_response['items'][0]['volumeInfo']['imageLinks']['thumbnail']
                    str_cover = str(cover_img)
                    str_isbn = str(isbn)

                    mongo.db.feature_books.update_one( 
                        { 'isbn' : str_isbn },
                        { '$set' :
                            { 
                             'image' : str_cover 
                             }
                        }
                    )


            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')

            except Exception as err:
                print(f'Other error occurred: {err}')



@app.route("/search_api", methods=["GET", "POST"])
def search_api():
    if os.path.exists("books.json"):
        os.remove("books.json")
    search_text = request.form.get('search')
    search_text_formatted = search_text.replace(" ", "+")
    search_type = request.form.get('search-type')
    search_type_formatted = "in" + search_type + ":"
    url = 'https://www.googleapis.com/books/v1/volumes?q=' + search_text_formatted + search_type_formatted + '&key=' + API_KEY
    try: 
        response = requests.get(url)
        response.raise_for_status()
        j2_response = response.json()
        if j2_response:
            j2_len = len(j2_response)
            search_results = {}
            for x in range(j2_len):          
                title = str(j2_response["items"][x]["volumeInfo"]["title"])
                author = str(j2_response["items"][x]["volumeInfo"]["authors"][0])
                sm_image = str(j2_response['items'][x]['volumeInfo']['imageLinks']['smallThumbnail'])
                pub_date = str(j2_response['items'][x]['volumeInfo']['publishedDate'])
                descrip = str(j2_response['items'][x]['volumeInfo']['description'])
                isbn2 = str(j2_response['items'][x]['volumeInfo']['industryIdentifiers'][0]['identifier'])
                _id = str(ObjectId())
                loop_data = {}
                loop_data = { 
                    'book':  {'id': _id, 'isbn': isbn2, 'title': title, 'author' : author,'image': sm_image, 'publication_date': pub_date, 'description': descrip}        
                }
                search_results.update(loop_data)
            #save search results to json file move to json directory for access later
            json_data = json.dumps(search_results)
            f = open("books.json", "w")
            f.write(json_data)
            f.close()
#           source = "books.json"I hav
#            destination = "data"
#            new_path = shutil.move(source, destination)
#            print("------------", new_path)
        else:
            flash("Search returned no results, please change your search terms and try again.")
            
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        
    except Exception as err:
        print(f'Other error occurred: {err}')
        
    return render_template('book_search_results.html')


@app.route('/book_search_results')
def book_search_results():
    book_data = []
    with open("books.json", "r") as json_data:
        book_data = json.load(json_data)
    print("------------", json_data)
    return render_template('book_search_results.html', results=book_data)


@app.route('/book_profile/<profile_id>')
def book_profile(profile_id):
    str_profile_id = str(profile_id)
#    the_book = search_results.get(str_profile_id)
    print("---------", the_book_)
    return render_template('book_profile.html')


@app.route('/book_review_form/<isbn>')
def book_review_form(isbn):
    return render_template("book_profile.html")


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
                "email": request.form.get("reg-email").lower(),
                "password": generate_password_hash(request.form.get(
                    "create-password")),
                "display_name": request.form.get("create-display-name").lower()
            }
            mongo.db.insert_one(register)

            #put the new user into the 'session" cookie
            session["email"] = request.form.get("reg-email")
            session['display_name'] = request.form.get("display_name")
            flash("Account Creation Successful")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        ## check if username already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_email["password"], request.form.get("password")):
                    session["email"] = request.form.get("email").lower()
                    d_name = mongo.db.users.find_one(
                        {"email": session["email"]})["display_name"]
                    session["display_name"] =  d_name
                    flash("Welcome, {}".format(mongo.db.users.find_one(
                        {"email": session["email"]})["display_name"]))
                    return redirect(url_for(
                        "login", display_name=d_name))
                    
            else:
                #invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            #username doesn't exist 
            flash("Account does not exist, please create one")
            return redirect(url_for("register"))
    return render_template("login.html")


@app.route("/profile/<email>", methods=["GET", "POST"])
def profile(email):
    if session["email"]:
        #grab the session user's display-name from the db
        d_name = mongo.db.users.find_one(
            {"email": session["email"]})["display_name"]
        return render_template("profile.html", display_name=d_name)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("email")
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

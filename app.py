import os
import requests
from flask import (
    Flask, flash, render_template, request, redirect, url_for)
from flask_pymongo import PyMongo
#from bson.objectid import ObjectId
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

    
@app.route("/book_search")
def book_search():
    return render_template("book_search.html")


@app.route("/search_api", methods=["GET", "POST"])
def search_api():
    search_text = (request.form.get('search')).lower()
    search_text_formatted = search_text.replace(" ", "+")
    search_type = (request.form.get('search-type')).lower()
    search_type_formatted = "in" + search_type + ":"
    url = 'https://www.googleapis.com/books/v1/volumes?q=' + search_text + search_type_formatted + '&key=' + API_KEY
    try: 
        response = requests.get(url)
        response.raise_for_status()
        j2_response = response.json()
        if j2_response:
            j2_len = len(j2_response)
            book_search = {}
            for x in range(j2_len):          
                title = str(j2_response["items"][x]["volumeInfo"]["title"])
                author = str(j2_response["items"][x]["volumeInfo"]["authors"][0])
                sm_image = str(j2_response['items'][x]['volumeInfo']['imageLinks']['smallThumbnail'])
                pub_date = str(j2_response['items'][x]['volumeInfo']['publishedDate'])
                descrip = str(j2_response['items'][x]['volumeInfo']['description'])
                isbn2 = str(j2_response['items'][x]['volumeInfo']['industryIdentifiers'][0]['identifier'])
                _id = ObjectId()
                book_search.update({ 
                    _id:  {'isbn': isbn2, 'title': title, 'author' : author,'image': sm_image, 'publication_date': pub_date, 'description': descrip}
                })
        
        else:
            flash("Search returned no results, please adjust your search terms and try again.")
            
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except Exception as err:
        print(f'Other error occurred: {err}')
    return redirect(url_for('book_search', book_search=book_search))


@app.route("/my_book_reviews", methods=["GET", "POST"])
def my_book_reviews():
    return render_template("my_book_reviews.html")


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

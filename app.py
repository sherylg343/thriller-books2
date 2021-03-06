import os
import requests
import json
from flask import (
    Flask, flash, render_template, request, redirect, url_for, session)
from flask_pymongo import PyMongo
from requests.exceptions import HTTPError
from bson.objectid import ObjectId
from datetime import date
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


SEARCH_BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q='
VOLUME_BASE_URL = 'https://www.googleapis.com/books/v1/volumes/'


@app.route('/')
@app.route('/get_home', methods=["GET", "POST"])
def get_home():
    get_feature_image()
    return render_template(
        "index.html",
        featured=mongo.db.feature_books.find())


@app.route('/get_feature_image')
def get_feature_image():
    """ if needed, obtains the url address for
    book cover images as well as the volume ids to facilitate
    adding and editing book reviews for these select books 
    """
    check_books = mongo.db.feature_books.find()
    for book in check_books:
        if (book["image"] == "") or (book["volume_id"] == ""):
            isbn = book["isbn"]
            img_url = SEARCH_BASE_URL + "isbn:" + isbn + '&key=' + API_KEY
            """ Calling Google Books API and putting in json format
            while accommodating any errors that occur with HTTPError module
            """
            try:
                response = requests.get(img_url)
                response.raise_for_status()
                j_response = response.json()
                for x in range(1):
                    cover_img = j_response['items'][x]['volumeInfo']['imageLinks']['thumbnail']
                    vol_id = j_response['items'][x]['id']
                    str_cover = str(cover_img)
                    str_isbn = str(isbn)
                    str_id = str(vol_id)

                    mongo.db.feature_books.update_one(
                        {'isbn': str_isbn},
                        {'$set':
                            {
                                'image': str_cover,
                                'volume_id': str_id
                            }
                        }
                    )

            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
                return render_template('index.html')

            except Exception as err:
                print(f'Other error occurred: {err}')
                return render_template('index.html')


@app.route('/book_search_results', methods=["GET", "POST"])
def book_search_results():
    """ using search criteria and keywords to call 
    Google Books API, putting response in json format
    and displaying search results in template
    """
    search_text = request.form.get('search')
    search_text_formatted = search_text.replace(" ", "+")
    search_type = request.form.get('search-type')
    search_type_formatted = "in" + search_type + ":"
    search_url = SEARCH_BASE_URL + search_type_formatted + search_text_formatted + '&key=' + API_KEY
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        # convert json response into Python data
        j2_response = response.json()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        flash("An error occurred in processing your search. Please try again or try at a later time.")
        return render_template('index.html')

    except Exception as err:
        print(f'Other error occurred: {err}')
        flash("An error occurred in processing your search. Please try again or try at a later time.")
        return render_template('index.html')

    return render_template(
        'book_search_results.html', books=j2_response)


@app.route('/book_profile/<volume_id>', methods=["GET", "POST"])
def book_profile(volume_id):
    """ calling Google Books API by volume id to display single
    Book Profile
    """
    reviews_list = []
    reviews = mongo.db.book_reviews.find({'volume_id': volume_id})
    reviews_list = True if len(list(reviews)) else False
    if not reviews_list:
        flash(
            "No reviews have been written yet for this book. Consider writing one if you've read the book.")
    volume_full_url = VOLUME_BASE_URL + volume_id
    try:
        vol_response = requests.get(volume_full_url)
        vol_response.raise_for_status()
        # convert json response into Python data
        vol_response = vol_response.json()
        reviews = mongo.db.book_reviews.find({"volume_id": volume_id})

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        flash("An error occurred in processing your search. Please try again or try at a later time.")
        return render_template('index.html')

    except Exception as err:
        print(f'Other error occurred: {err}')
        flash("An error occurred in processing your search. Please try again or try at a later time.")
        return render_template('index.html')

    return render_template(
        'book_profile.html', book=vol_response, reviews=reviews)


@app.route('/book_review_form/<volume_id>', methods=["GET", "POST"])
def book_review_form(volume_id):
    """checking if user is logged in and if user already wrote
    a book review before calling Google Books API
    and presenting review form
    """
    if 'email' in session:
        reviews = mongo.db.book_reviews.find(
            {'volume_id': volume_id})
        d_name = mongo.db.users.find_one(
            {"email": session["email"]})["display_name"]
        today = date.today()
        for review in reviews:
            if review['display_name'] == d_name:
                flash("You have already submitted a review for this book. You may edit or delete it below.")
                return render_template(
                    "my_book_reviews.html", display_name=d_name, book_reviews=mongo.db.book_reviews.find())
        volume_full_url = VOLUME_BASE_URL + volume_id
        try:
            vol_response = requests.get(volume_full_url)
            vol_response.raise_for_status()
            # convert json response into Python data
            vol_response = vol_response.json()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            flash("An error occurred in processing your search. Please try again or try at a later time.")
            return render_template('index.html')

        except Exception as err:
            print(f'Other error occurred: {err}')
            flash("An error occurred in processing your search. Please try again or try at a later time.")
            return render_template('index.html')

        return render_template(
            'book_review_form.html', book=vol_response, today=today)
    else:
        flash("Please log in first prior to writing a review.")
        return render_template("login.html")


@app.route('/insert_review', methods=["POST"])
def insert_review():
    """ inserting new book review in Mongo DB
    """
    book_reviews = mongo.db.book_reviews
    d_name = mongo.db.users.find_one(
        {"email": session["email"]})["display_name"]
    review_data = request.form.to_dict()
    review_data["display_name"] = d_name
    book_reviews.insert_one(review_data)
    book_reviews = mongo.db.book_reviews.find({'display_name': d_name})
    flash("Thank you for submitting your review. You may view it by scrolling down this page.")
    return render_template(
        'my_book_reviews.html', display_name=d_name, book_reviews=book_reviews)


@app.route('/my_book_reviews')
def my_book_reviews():
    """ displaying user's book reviews
    """
    d_name = mongo.db.users.find_one(
        {"email": session["email"]})["display_name"]
    return render_template(
        'my_book_reviews.html', display_name=d_name, book_reviews=mongo.db.book_reviews.find())


@app.route('/edit_book_review/<review_id>')
def edit_book_review(review_id):
    """ displays form to edit a book review
    """
    the_review = mongo.db.book_reviews.find_one({"_id": ObjectId(review_id)})
    return render_template(
        'edit_book_review.html', review=the_review)


@app.route('/update_review/<review_id>', methods=["GET", "POST"])
def update_review(review_id):
    """ update a book review based on edit review form
    and confirm update to user
    """
    book_reviews = mongo.db.book_reviews.find()
    d_name = mongo.db.users.find_one(
        {"email": session["email"]})["display_name"]
    mongo.db.book_reviews.update_one(
        {'_id': ObjectId(review_id)},
        {'$set':
            {
                'book_title': request.form.get('book-title'),
                'rating': request.form.get('rating'),
                'review_title': request.form.get('review-title'),
                'review_text': request.form.get('review-text'),
                'spoiler': request.form.get('spoiler')
            }
        }
    )
    flash("Thank you for editing your review. You may view the revised review by scrolling down this page.")
    return render_template(
        'my_book_reviews.html', display_name=d_name, book_reviews=book_reviews)


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    """ delete review per user reequest
    and confirm deletion
    """
    d_name = mongo.db.users.find_one(
        {"email": session["email"]})["display_name"]
    book_reviews = mongo.db.book_reviews.find()
    mongo.db.book_reviews.delete_one({'_id': ObjectId(review_id)})
    flash("Review successfully deleted")
    return redirect(url_for(
        'my_book_reviews', display_name=d_name, book_reviews=book_reviews))


@app.route("/register", methods=["GET", "POST"])
def register():
    """ create a user account
    """
    if request.method == "POST":
        """ check if username already exists in db
        """
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("reg-email")})
        existing_display_name = mongo.db.users.find_one(
            {"display_name": request.form.get(
                "create-display-name")})

        if existing_email:
            flash("Email already exists")
            return render_template("login.html")

        elif existing_display_name:
            flash("Display Name already exists, please choose another one.")
            return redirect({{url_for("register")}})

        else:
            register = {
                "email": request.form.get("reg-email").lower(),
                "password": generate_password_hash(
                    request.form.get("create-password")),
                "display_name": request.form.get(
                    "create-display-name").lower()
            }
            mongo.db.users.insert_one(register)

            """ put the new user into the 'session" cookie
            """
            session["email"] = request.form.get("reg-email")
            session['display_name'] = request.form.get(
                "display_name")
            flash("Account Creation Successful - You are Logged In")
            return render_template("index.html")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ login proces with validation and security
    hashed password
    """
    if request.method == "POST":
        """ check if username already exists in db
        """
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            """ ensure hashed password matches user input
            """
            if check_password_hash(
                existing_email["password"], request.form.get("password")):
                session["email"] = request.form.get("email").lower()
                d_name = mongo.db.users.find_one(
                    {"email": session["email"]})["display_name"]
                session["display_name"] = d_name
                flash("Welcome, {}".format(mongo.db.users.find_one(
                    {"email": session["email"]})["display_name"]))
                return render_template(
                    "profile.html", display_name=d_name, book_reviews=mongo.db.book_reviews.find())

            else:
                """ if invalid password match
                """
                flash("Incorrect Username and/or Password")
                return render_template("login.html")

        else:
            """ if username doesn't exist
            """
            flash("Account does not exist, please create one")
            return redirect(url_for("register"))
    return render_template("login.html")


@app.route("/profile")
def profile():
    """ Display user profile with list of 
    reviewed books based on display_name
    """
    if session["email"]:
        d_name = mongo.db.users.find_one(
            {"email": session["email"]})["display_name"] 
        return render_template(
            "profile.html", display_name=d_name, book_reviews=mongo.db.book_reviews.find())
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """remove user from session cookies
    """
    flash("You have been logged out")
    session.pop("email")
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)

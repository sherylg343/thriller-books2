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


@app.route('/')
@app.route('/get_home', methods=["GET", "POST"])
def get_home():
    get_feature_image()
    return render_template(
        "index.html",
        featured=mongo.db.feature_books.find())


@app.route('/get_feature_image')
def get_feature_image():
    check_books = mongo.db.feature_books.find()
    for book in check_books:
        if (book["image"] == "") or (book["volume_id"] == ""):
            isbn = book["isbn"]
            title = book['title']
            title_formatted = title.replace(" ", "+")
            author = book['author']
            author_formatted = author.replace(" ", "+")
            url = 'https://www.googleapis.com/books/v1/volumes?q=' + "intitle:" + title_formatted + "+" + "inauthor:" + author_formatted + '&key=' + API_KEY
        # from pynative.com/parse-json-response-
        # using-python-requests-library/
            try:
                response = requests.get(url)
                response.raise_for_status()
                j_response = response.json()
                for x in range(1):
                    cover_img = j_response['items'][x]['volumeInfo']['imageLinks']['thumbnail']
                    vol_id = j_response['items'][x]['id']
                    (print("--------", cover_img, vol_id))
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

            except Exception as err:
                print(f'Other error occurred: {err}')


@app.route('/book_search_results', methods=["GET", "POST"])
def book_search_results():
    if request.method == "POST":
        search_text = request.form.get('search')
        search_text_formatted = search_text.replace(" ", "+")
        search_type = request.form.get('search-type')
        search_type_formatted = "in" + search_type + ":"
        url = 'https://www.googleapis.com/books/v1/volumes?q=' + search_type_formatted + search_text_formatted + '&key=' + API_KEY
        try:
            response = requests.get(url)
            response.raise_for_status()
            # convert json response into Python data
            j2_response = response.json()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')

        except Exception as err:
            print(f'Other error occurred: {err}')

    return render_template(
        'book_search_results.html', books=j2_response)


@app.route('/book_profile/<volume_id>', methods=["GET", "POST"])
def book_profile(volume_id):
    reviews = mongo.db.book_reviews.find({'volume_id': volume_id})
    reviews_list = True if len(list(reviews)) else False
    if not reviews_list:
        flash(
            "No reviews have been written yet for this book. Consider writing one if you've read the book.")
    volume_base_url = 'https://www.googleapis.com/books/v1/volumes/'
    volume_full_url = volume_base_url + volume_id
    try:
        vol_response = requests.get(volume_full_url)
        vol_response.raise_for_status()
        # convert json response into Python data
        vol_response = vol_response.json()
        ratings = mongo.db.book_reviews.find({'volume_id': volume_id})['rating']
        ratings_list = list(ratings)
        sum_num = 0
        for x in ratings_list:
            sum_num = sum_num + x

        count = len(ratings_list)
        avg = sum_num / count
        stars = round(avg, 0)
        print("-------", count, avg, stars)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except Exception as err:
        print(f'Other error occurred: {err}')

    return render_template(
        'book_profile.html', book=vol_response, reviews=reviews)


@app.route('/book_review_form/<volume_id>', methods=["GET", "POST"])
def book_review_form(volume_id):
    if 'email' in session:
        email = session['email']
        today = date.today()
        d_name = mongo.db.users.find_one(
            {"email": session["email"]})["display_name"]
        volume_base_url = 'https://www.googleapis.com/books/v1/volumes/'
        volume_full_url = volume_base_url + volume_id
        try:
            vol_response = requests.get(volume_full_url)
            vol_response.raise_for_status()
            # convert json response into Python data
            vol_response = vol_response.json()
        
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')

        except Exception as err:
            print(f'Other error occurred: {err}')

        return render_template(
            "book_review_form.html", book=vol_response, display_name=d_name, today=today)

    else:
        flash("Please log in first prior to writing a review.")
        return redirect(url_for("login"))


@app.route('/insert_review', methods=["POST"])
def insert_review():
    book_reviews = mongo.db.book_reviews
    book_reviews.insert_one(request.form.to_dict())
    d_name = mongo.db.users.find_one(
        {"email": session["email"]})["display_name"]
    book_reviews = mongo.db.book_reviews.find({'display_name': d_name})
    return render_template(
        'my_book_reviews.html', display_name=d_name, book_reviews=book_reviews)


@app.route('/avg_ratings/<volume_id>')
def avg_ratings(volume_id):
    ratings = mongo.db.book_reviews.find({'volume_id': volume_id})['rating']
    ratings_list = list(ratings)
    sum_num = 0
    for x in ratings_list:
        sum_num = sum_num + x

    count = len(ratings_list)
    avg = sum_num / count
    stars = round(avg, 0)



@app.route('/my_book_reviews')
def my_book_reviews():
    d_name = mongo.db.users.find_one(
        {"email": session["email"]})["display_name"]
    return render_template(
        'my_book_reviews.html', display_name=d_name, book_reviews=mongo.db.book_reviews.find())


@app.route('/edit_book_review/<review_id>')
def edit_book_review(review_id):
    the_review = mongo.db.book_reviews.find_one({"_id": ObjectId(review_id)})
    return render_template(
        'edit_book_review.html', review=the_review)


@app.route('/update_review/<review_id>', methods=["GET", "POST"])
def update_review(review_id):
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

    return render_template(
        'my_book_reviews.html', display_name=d_name, book_reviews=book_reviews)


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    d_name = mongo.db.users.find_one(
        {"email": session["email"]})["display_name"]
    book_reviews = mongo.db.book_reviews.find()
    mongo.db.tasks.remove({'_id': ObjectId(review_id)})
    return redirect(url_for(
        'my_book_reviews', display_name=d_name, book_reviews=book_reviews))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #
        # print(mongo.db.users.find())
        # check if username already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("reg-email")})
        existing_display_name = mongo.db.users.find_one(
            {"display_name": request.form.get(
                "create-display-name")})

        if existing_email:
            flash("Email already exists")
            return redirect({{url_for("register")}})

        elif existing_display_name:
            flash("Display Name already exists")
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

            # put the new user into the 'session" cookie
            session["email"] = request.form.get("reg-email")
            session['display_name'] = request.form.get(
                "display_name")
            flash("Account Creation Successful")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            # ensure hashed password matches user input
            print(existing_email["password"])
            print(request.form.get("password"))
            if check_password_hash(
                    existing_email["password"], request.form.get("password")):
                session["email"] = request.form.get("email").lower()
                d_name = mongo.db.users.find_one(
                    {"email": session["email"]})["display_name"]
                session["display_name"] = d_name
                flash("Welcome, {}".format(mongo.db.users.find_one(
                    {"email": session["email"]})["display_name"]))
                return redirect(url_for(
                    "profile"))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Account does not exist, please create one")
            return redirect(url_for("register"))
    return render_template("login.html")


@app.route("/profile/")
def profile():
    if session["display_name"]:
        d_name = session["display_name"]
        return render_template(
            "profile.html", display_name=d_name, book_reviews=mongo.db.book_reviews.find())
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

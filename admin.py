import os
import requests
import json
import shutil
from flask import (
    Flask, flash, render_template, redirect, request, url_for)
from flask_pymongo import PyMongo
from requests.exceptions import HTTPError
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
    

@app.route('/get_feature_image')
def get_feature_image():
    check_images = mongo.db.feature_books.find()
    for image in check_images:
        if image["image"] == "":
            isbn = image["isbn"]
            url = 'https://www.googleapis.com/books/v1/volumes?q=' + isbn + '&key=' + API_KEY
            # from pynative.com/parse-json-response-
            # #using-python-requests-library/
            try:
                json_response = {}
                response = requests.get(url)
                response.raise_for_status()
                json_response = response.json()
                outfile = open('json-api1.json', 'w')
                outfile.write(json_response)
                outfile.close()
                source = "json-api1.json"
                destination = "/static/assets/json/json-api1.json"
                shutil.move(source, destination)

                
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=5001,
            debug=True)

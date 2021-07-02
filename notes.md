# Start up terminal commands (not in full order)

(whenever installing new packages you must update the requirements.txt file (see 1.) so Heroku knows we require more to run the app)

1. pip3 freeze --local > requirements.txt
    - tells Heroku which applications and dependencies are required to run our app
    - creats the requirements.txt file

2. echo web: python app.py > Procfile
    - the Procfile is what Heroku looks for to know which file runs the app & how to run it

3. pip3 install flask-pymongo
4. pip3 install dnspython
    - in order to use the Mongo SRV connection string


# Important set up on app.py

import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
## to use environment variables need to import env package
## env.py wont be pushed to github...
## once app deployed to Heroku it wont find env.py and throw error
## why only need to import env if the os can find existing file path for env.py
if os.path.exists("env.py"):
    import env

## instance of Flask stored in variable app
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

## set up an instance of PyMongo and add the app into that using the below constructor method. 
## This is the Flast 'app' object we defined above and is the final step to ensure our Flask app is properly communicating with the Mongo database.
mongo = PyMongo(app)


## / refers to default route
@app.route("/")

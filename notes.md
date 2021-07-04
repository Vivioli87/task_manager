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


# For search lesson and creating indexes.

The task name and the task description are suitable for what I want my users to be able
to search by.
Within the Index, we need to provide a list of fields that will be queried.
This list will contain a tuple () for each field that we'd like to query, which is two
for our purposes.
The first tuple that we want to search within, is our 'task_name' field.
The type of query we'll use is 'text', which is the most common Index type.

example from mini project.


in terminal:

python3
from app import mongo

mongo.db.tasks.create_index([("task_name", "text"), ("task_description", "text")])

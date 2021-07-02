import os
from flask import Flask
# to use environment variables need to import env package
# env.py wont be pushed to github...
# once app deployed to Heroku it wont find env.py and throw error
# why only need to import env if the os can find existing file path for env.py
if os.path.exists("env.py"):
    import env

# instance of Flask stored in variable app
app = Flask(__name__)


# / refers to default route
@app.route("/")
def hello():
    return "Hello World... again!"


# tells our app how & where to run the app
# gets IP and PORT variables from env.py file
# only use debug=True during development, change to False before submission
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

# Starting terminal commands

1. pip3 freeze --local > requirements.txt
    - tells Heroku which applications and dependencies are required to run our app
    - creats the requirements.txt file

2. echo web: python app.py > Procfile
    - the Procfile is what Heroku looks for to know which file runs the app & how to run it
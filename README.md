# python_flask_boilerplate
Simple webApp with Python Flask + mongoDB

## Files and Dir Info
* Procfile -> for heroku
* requirements.txt -> list of the all the installed python packages
* app/ -> actual app
* templates/ -> static HTML templates

## Commands
### command for setting up the virtualenv
```bash
virtualenv -p /usr/bin/python3 --no-download  --no-wheel --no-setuptools  virtual/
```
### command for installing the required packages
```bash
pip install -r requirements.txt
```
### command for updating the requirements.txt file
```bash
pip freeze > requirements.txt
```

## Imp Links
* https://python-flask-mongo.herokuapp.com/
* https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0
* https://flask-pymongo.readthedocs.io/en/latest/
* https://flask-login.readthedocs.io/en/latest/
* https://codeburst.io/jinja-2-explained-in-5-minutes-88548486834e
* https://www.youtube.com/watch?v=rGER0KDdJqI

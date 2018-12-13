from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:flask@localhost/flask'
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# from app import views
from app import models

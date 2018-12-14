from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

db = SQLAlchemy(app)
Migrate = Migrate(app, db)
# db.create_all()

from app import views, models, forms

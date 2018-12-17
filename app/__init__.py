from flask import Flask, render_template
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)

db = SQLAlchemy(app)
Migrate = Migrate(app, db)
# db.create_all()

@app.errorhandler(404)
def not_found(error):  
    return render_template('404.html')

from app import routes, models

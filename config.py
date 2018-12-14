import os
from app import app

POSTGRES = {
    'user': 'flask',
    'pw': 'flask',
    'db': 'flask',
    'host': 'db',
    'port': '5432',
}

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db_repository')

TEMPLATES_AUTO_RELOAD = True 

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

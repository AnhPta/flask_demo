import os

POSTGRES = {
    'user': 'flask',
    'pw': 'flask',
    'db': 'flask',
    'host': 'localhost',
    'port': '54321',
}

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_DATABASE_URI = 'postgres://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
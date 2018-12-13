from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Haink'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'lucy'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'thuy'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

# from flask import render_template, flash, redirect
# from app import app
# from .forms import LoginForm

# # index view function suppressed for brevity

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for OpenID="%s", remember_me=%s' %
#               (form.openid.data, str(form.remember_me.data)))
#         return redirect('/index')
#     return render_template('login.html',
#                            title='Sign In',
#                            form=form)
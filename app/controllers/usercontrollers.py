from app import app, db, models, forms, routes
from flask import render_template, request, redirect, url_for, flash

def index():
    users = models.User.query.all()
    return render_template("users/users.html", users = users)

def store():
    action = 'store'
    form = forms.UserForm()

    if form.validate_on_submit():
        user = models.User(
            username = form.username.data, 
            email = form.email.data
            )
        try:
            db.session.add(user)
            db.session.commit()
            flash('Create success', 'success')
            return redirect(url_for('index'))
        except:
            flash('Error : Username already exists', 'error')
    return render_template("users/form.html", form = form, action = action)

def update(id):
    action = 'update'

    user = models.User.query.get_or_404(id)
    form = forms.UserForm(obj=user)

    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data

        try:
            db.session.commit()
            flash('Edit success', 'success')
            return redirect(url_for('index'))
        except:
            flash('Error : Username already exists', 'error')
    form.username.data = user.username 
    form.email.data = user.email
    return render_template('users/form.html', form = form)

def destroy(id):
    """
    Delete a user from the database
    """
    user = models.User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Delete success', 'success')

    # redirect to the users page
    return redirect(url_for('index'))

    return render_template(title="Delete User")

    # user = models.User(request.form['username'], request.form['email'])
    # db.session.add(user)
    # db.session.commit()
    # return redirect(url_for('index'))

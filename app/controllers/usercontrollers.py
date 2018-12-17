from app import db, models, forms
from flask import render_template, redirect, url_for, flash

def user_index():
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
            return redirect(url_for('user_index'))
        except Exception:
            flash('Error: Username or Email is already', 'error')
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
            return redirect(url_for('user_index'))
        except:
            flash('Error: Username or Email is already', 'error')
    form.username.data = user.username 
    form.email.data = user.email
    return render_template('users/form.html', form = form)

def destroy(id):
    user = models.User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Delete success', 'success')
    return redirect(url_for('user_index'))

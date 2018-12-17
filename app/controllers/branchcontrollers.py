from app import db, models, forms
from flask import render_template, redirect, url_for, flash

def branch_index():
    branches = models.Branch.query.all()
    return render_template("branches/branches.html", branches = branches)

def store():
    action = 'store'
    form = forms.BranchForm()

    if form.validate_on_submit():
        branch = models.Branch(
			name        = form.name.data,
			email       = form.email.data,
			phone       = form.phone.data,
			tax_number  = form.tax_number.data,
			website     = form.website.data,
			description = form.description.data,
			bank        = form.bank.data,
			city_id     = form.city_id.data,
			district_id = form.district_id.data,
			status      = form.status.data
            )
        try:
            db.session.add(branch)
            db.session.commit()
            flash('Create success', 'success')
            return redirect(url_for('branch_index'))
        except:
            flash('Error: Something errors', 'error')
    return render_template("branches/form.html", form = form, action = action)

def update(id):
    action = 'update'

    branch = models.Branch.query.get_or_404(id)
    form = forms.BranchForm(obj=branch)

    if form.validate_on_submit():
    	branch.name		   = form.name.data
    	branch.email       = form.email.data
    	branch.phone       = form.phone.data
    	branch.tax_number  = form.tax_number.data
    	branch.website     = form.website.data
    	branch.description = form.description.data
    	branch.bank        = form.bank.data
    	branch.city_id     = form.city_id.data
    	branch.district_id = form.district_id.data
    	branch.status      = form.status.data

    	try:
    		db.session.commit()
    		flash('Edit success', 'success')
    		return redirect(url_for('branch_index'))
    	except:
    		flash('Error: Something errors', 'error')
    form.name.data        = branch.name
    form.email.data       = branch.email
    form.phone.data       = branch.phone
    form.tax_number.data  = branch.tax_number
    form.website.data     = branch.website
    form.description.data = branch.description
    form.bank.data        = branch.bank
    form.city_id.data     = branch.city_id
    form.district_id.data = branch.district_id
    form.status.data      = branch.status
    return render_template('branches/form.html', form = form)

def destroy(id):
    branch = models.Branch.query.get_or_404(id)
    db.session.delete(branch)
    db.session.commit()
    flash('Delete success', 'success')
    return redirect(url_for('branch_index'))

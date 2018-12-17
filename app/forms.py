from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email
from app import models

class UserForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired()])
	email    = StringField('Email', validators = [DataRequired(), Email()])

	submit   = SubmitField('Submit')

	# def validate_username(self, field):
	# 	if models.User.query.filter_by(username=field.data).first():
	# 		raise ValidationError('Username is already in use')
	
	# def validate_email(self, field):
	# 	if models.User.query.filter_by(email=field.data).first():
	# 		raise ValidationError('Email is already in use')

class BranchForm(FlaskForm):
	name        = StringField('Name', validators = [DataRequired()])
	email       = StringField('Email', validators = [DataRequired()])
	phone       = StringField('Phone', validators = [DataRequired()])
	tax_number  = StringField('Tax_number', validators = [DataRequired()])
	website     = StringField('Website')
	description = TextAreaField(u'Description')
	bank        = StringField('Bank')
	city_id     = SelectField('City',
        choices=[('1', 'Hà nội'), ('0', 'HCM')])
	district_id = SelectField('District',
        choices=[
        ('1', 'Đống Đa'),
        ('1', 'Thanh Xuân'),
        ('3', 'Quận 1'),
        ('4', 'Quận 2')
        ])
	status      = SelectField('Status',
        choices=[('1', 'Hoạt động'), ('0', 'Không hoạt động')])

	submit = SubmitField('Submit')

	# def validate_name(self, field):
	# 	if models.Branch.query.filter_by(name=field.data).first():
	# 		raise ValidationError('Name is already in use.')

	# def validate_email(self, field):
	# 	if models.Branch.query.filter_by(email=field.data).first():
	# 		raise ValidationError('Email is already in use.')

# from flask.ext.wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app import models

class UserForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	submit = SubmitField('Submit')

	# def validate_email(self, field):
 #        if models.User.query.filter_by(email=field.data).first():
 #            raise ValidationError('Email is already in use.')

 #    def validate_username(self, field):
 #        if models.User.query.filter_by(username=field.data).first():
 #            raise ValidationError('Username is already in use.')
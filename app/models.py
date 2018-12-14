from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, username, email):
    	self.username = username
    	self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

class Branches(db.Model):
	id          = db.Column(db.Integer, primary_key=True)
	name        = db.Column(db.String(120), index=True, unique=True)
	email       = db.Column(db.String(120), index=True, unique=True)
	phone       = db.Column(db.String(120), index=True, unique=True)
	tax_number  = db.Column(db.String(120), index=True, unique=True)
	website     = db.Column(db.String(120), index=True)
	description = db.Column(db.String(155), index=True)
	bank        = db.Column(db.String(120), index=True)
	city_id     = db.Column(db.Integer, index=True)
	district_id = db.Column(db.Integer, index=True)
	status      = db.Column(db.Integer, index=True)

	def __init__(
		self,
		name,
		email,
		phone,
		tax_number,
		website,
		description,
		bank,
		city_id,
		district_id,
		status):
		self.name        = name
		self.email       = email
		self.phone       = phone
		self.tax_number  = tax_number
		self.website     = website
		self.description = description
		self.bank        = bank
		self.city_id     = city_id
		self.district_id = district_id
		self.status      = status

	def __repr__(self):
		return '<Branch: %r>' % (self.name)


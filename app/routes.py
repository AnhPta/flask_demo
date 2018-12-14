from app import app, db, models, forms
from app.controllers import usercontrollers

@app.route('/', methods = ['GET'])
def hi():  
    return 'Home'

@app.route('/users', methods = ['GET', 'POST'])
def index():
    return usercontrollers.index()

@app.route('/users/add', methods = ['GET', 'POST'])
def store():
    return usercontrollers.store()

@app.route('/users/edit/<id>', methods=['GET', 'POST'])
def update(id):
    return usercontrollers.update(id)

@app.route('/users/delete/<id>', methods=['GET', 'POST'])
def destroy(id):
    return usercontrollers.destroy(id)
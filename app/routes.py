from app import app
from app.controllers import usercontrollers, branchcontrollers

@app.route('/', methods = ['GET'])
def home():  
    return branchcontrollers.branch_index()

# user
@app.route('/users', methods = ['GET', 'POST'])
def user_index():
    return usercontrollers.user_index()

@app.route('/users/add', methods = ['GET', 'POST'])
def user_store():
    return usercontrollers.store()

@app.route('/users/edit/<id>', methods=['GET', 'POST'])
def user_update(id):
    return usercontrollers.update(id)

@app.route('/users/delete/<id>', methods=['GET', 'POST'])
def user_destroy(id):
    return usercontrollers.destroy(id)

# branch
@app.route('/branches', methods = ['GET', 'POST'])
def branch_index():
    return branchcontrollers.branch_index()

@app.route('/branches/add', methods = ['GET', 'POST'])
def branch_store():
    return branchcontrollers.store()

@app.route('/branches/edit/<id>', methods=['GET', 'POST'])
def branch_update(id):
    return branchcontrollers.update(id)

@app.route('/branches/delete/<id>', methods=['GET', 'POST'])
def branch_destroy(id):
    return branchcontrollers.destroy(id)
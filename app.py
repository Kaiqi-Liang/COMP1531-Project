"""Flask server"""
from json import dumps
from flask import Flask, request

from server.auth import *

DATA = {
    'user': [], #[{'u_id': u_id1, 'email': email1, 'password': password1}, {'u_id': u_id2, 'email': email2, 'password': password2}]
    'channel': [],
    'message': []
}

def get_data():
    global DATA
    return DATA

APP = Flask(__name__)

@APP.route('/auth/login', methods=['POST'])
def login():
    """ Given a registered users' email and password and generates a valid token for the user to remain authenticated """
    return dumps(auth_login(request.form.get('email'), request.form.get('password')))

@APP.route('/auth/logout', methods=['POST'])
def logout():
    """ Given an active token, invalidates the taken to log the user out. If a valid token is given, and the user is successfully logged out, it returns true, otherwise false. """
    return dumps(auth_logout(request.form.get('token')))

@APP.route('/auth/register', methods=['POST'])
def register():
    """ Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session. A handle is generated that is the concatentation of a lowercase-only first name and last name. If the handle is already taken, a number is added to the end of the handle to make it unique. """
    return dumps(auth_register(request.form.get('email'), request.form.get('password'), request.form.get('name_first'), request.form.get('name_last')))

if __name__ == '__main__':
    APP.run(debug=True)

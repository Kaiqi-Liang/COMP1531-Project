''' Flask server '''
from json import dumps
from flask import Flask, request

''' import all local packages '''
from backend import auth 
from backend import channel


APP = Flask(__name__)

@APP.route('/auth/login', methods=['POST'])
def login():
    """ Given a registered users' email and password and generates a valid token for the user to remain authenticated """
    return dumps(auth.auth_login(request.form.get('email'), request.form.get('password')))

@APP.route('/auth/logout', methods=['POST'])
def logout():
    """ Given an active token, invalidates the taken to log the user out. If a valid token is given, and the user is successfully logged out, it returns true, otherwise false. """
    return dumps(auth.auth_logout(request.form.get('token')))

@APP.route('/auth/register', methods=['POST'])
def register():
    """ Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session. A handle is generated that is the concatentation of a lowercase-only first name and last name. If the handle is already taken, a number is added to the end of the handle to make it unique. """
    return dumps(auth.auth_register(request.form.get('email'), request.form.get('password'), request.form.get('name_first'), request.form.get('name_last')))

@APP.route('/channel/details', methods=['GET'])
def details():
    ''' Given a Channel with ID channel_id that the authorised user is part of, provide basic details about the channel '''
    return dumps(channel.channel_details(request.form.get('token'), request.form.get('channel_id')))

@APP.route('/channels/create', methods=['POST'])
def create():
    ''' Creates a new channel with that name that is either a public or private channel '''
    return dumps(channel.channels_create(request.form.get('token'), request.form.get('name'), request.form.get('is_public')))

if __name__ == '__main__':
    APP.run(debug=True)

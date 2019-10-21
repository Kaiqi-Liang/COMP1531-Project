"""Flask server"""
import sys
from json import dumps
from flask_cors import CORS
from flask_mail import Mail, Message
from flask import Flask, request
import random

from backend import auth
from backend import channel
from backend.database import get_data


APP = Flask(__name__)
APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'my.gmail@gmail.com',
    MAIL_PASSWORD = ""
)
CORS(APP)


@APP.route('/send-mail/')
def send_mail():
    mail = Mail(APP)
    try:
        msg = Message("Send Mail Test!",
            sender="my.gmail@gmail.com",
            recipients=["person.sending.to@gmail.com"])
        msg.body = "Hello! This is a test body"
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return (str(e))


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


@APP.route('/auth/passwordreset/request', methods=['POST'])
def passwordreset_request():
    """ Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email. """
    email = request.form.get('email')
    if email == "":
        raise ValueError("No email")

    users = get_data()['users']
    #Given an email address check if the user is a registered user
    for user in users:
        if user['email'] == email:
            reset_code = reset_code + str(random.randint(10000, 999999))
            user['reset'] = reset_code

    #send them an email
    mail = Mail(APP)
    try:
        msg = Message("Send Mail Test!",
            sender="my.gmail@gmail.com",
            recipients=["person.sending.to@gmail.com"])
        #secret code (generated randomly)
        msg.body = body + str(random.randint(10000, 999999))
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return (str(e))

    return dumps({})


@APP.route('/channel/details', methods=['GET'])
def details():
    ''' Given a Channel with ID channel_id that the authorised user is part of, provide basic details about the channel '''
    return dumps(channel.channel_details(request.form.get('token'), request.form.get('channel_id')))

@APP.route('/channels/create', methods=['POST'])
def create():
    ''' Creates a new channel with that name that is either a public or private channel '''
    return dumps(channel.channels_create(request.form.get('token'), request.form.get('name'), request.form.get('is_public')))


if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000), debug=True)

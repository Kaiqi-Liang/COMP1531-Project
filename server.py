""" Flask server """
import os
import sys
import random
from json import dumps
from flask import Flask, request, send_from_directory
from flask_cors import CORS
from flask_mail import Mail, Message

from backend import auth
from backend import channel
from backend import message
from backend import user
from backend import admin
from backend import standup
from backend import search
from backend.database import get_data, clear, save, load
from backend.helpers.exception import defaultHandler

APP = Flask(__name__, static_url_path='/static/')
CORS(APP)
APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='kaiqi.liang9989@gmail.com',
    MAIL_PASSWORD="1234567890-zxcvbnm,./"
)
APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)


def send_mail(email, reset_code):
    """ Send an email """
    mail = Mail(APP)
    msg = Message("Authentication", sender="kaiqi.liang9989@gmail.com", recipients=[email])
    msg.body = reset_code
    mail.send(msg)


@APP.route('/static/<path:path>')
def send_img(path):
    """ Send an image """
    return send_from_directory('', path)



# AUTH

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
    for usr in get_data()['user']:
        if usr['email'] == email:
            reset_code = str(random.randint(100000, 999999))
            usr['reset'] = reset_code
            send_mail(email, reset_code)
    return dumps({})


@APP.route('/auth/passwordreset/reset', methods=['POST'])
def passwordreset_reset():
    """ Given a reset code for a user, set that user's new password to the password provided """
    return dumps(auth.auth_passwordreset_reset(request.form.get('reset_code'), request.form.get('new_password')))



# CHANNEL

@APP.route('/channel/invite', methods=['POST'])
def invite():
    """ Invites a user (with user id u_id) to join a channel with ID channel_id. Once invited the user is added to the channel immediately """
    return dumps(channel.channel_invite(request.form.get('token'), request.form.get('channel_id'), request.form.get('u_id')))


@APP.route('/channel/details', methods=['GET'])
def details():
    """ Given a Channel with ID channel_id that the authorised user is part of, provide basic details about the channel """
    return dumps(channel.channel_details(request.args.get('token'), request.args.get('channel_id')))


@APP.route('/channel/messages', methods=['GET'])
def messages():
    """ Given a Channel with ID channel_id that the authorised user is part of, return up to 50 messages between index "start" and "start + 50". Message with index 0 is the most recent message in the channel. This function returns a new index "end" which is the value of "start + 50", or, if this function has returned the least recent messages in the channel, returns -1 in "end" to indicate there are no more messages to load after this return """
    return dumps(channel.channel_messages(request.args.get('token'), request.args.get('channel_id'), request.args.get('start')))


@APP.route('/channels/list', methods=['GET'])
def list():
    """ Provide a list of all channels (and their associated details) that the authorised user is part of """
    return dumps(channel.channels_list(request.args.get('token')))


@APP.route('/channels/listall', methods=['GET'])
def listall():
    """ Provide a list of all channels (and their associated details) """
    return dumps(channel.channels_listall(request.args.get('token')))


@APP.route('/channels/create', methods=['POST'])
def create():
    """ Creates a new channel with that name that is either a public or private channel """
    return dumps(channel.channels_create(request.form.get('token'), request.form.get('name'), request.form.get('is_public')))


@APP.route('/channel/leave', methods=['POST'])
def leave():
    ''' Given a channel ID, the user removed as a member of this channel '''
    return dumps(channel.channel_leave(request.form.get('token'), request.form.get('channel_id')))


@APP.route('/channel/join', methods=['POST'])
def join():
    ''' Given a channel_id of a channel that the authorised user can join, adds them to that channel '''
    return dumps(channel.channel_join(request.form.get('token'), request.form.get('channel_id')))


@APP.route('/channel/addowner', methods=['POST'])
def addowner():
    """ Make user with user id u_id an owner of this channel """
    return dumps(channel.channel_addowner(request.form.get('token'), request.form.get('channel_id'), request.form.get('u_id')))


@APP.route('/channel/removeowner', methods=['POST'])
def removeowner():
    """ Remove user with user id u_id an owner of this channel """
    return dumps(channel.channel_removeowner(request.form.get('token'), request.form.get('channel_id'), request.form.get('u_id')))



# MESSAGE

@APP.route('/message/sendlater', methods=['POST'])
def sendlater():
    """ Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future """
    return dumps(message.message_sendlater(request.form.get('token'), request.form.get('channel_id'), request.form.get('message'), request.form.get('time_sent')))

@APP.route('/message/send', methods=['POST'])
def send_message():
    """ Send a message from authorised_user to the channel specified by channel_id """
    return dumps(message.message_send(request.form.get('token'), request.form.get('channel_id'), request.form.get('message')))


@APP.route('/message/remove', methods=['DELETE'])
def remove():
    """ Given a message_id for a message, this message is removed from the channel """
    return dumps(message.message_remove(request.form.get('token'), request.form.get('message_id')))


@APP.route('/message/edit', methods=['PUT'])
def edit():
    """ Given a message, update it's text with new text. If the new message is an empty string, the message is deleted """
    return dumps(message.message_edit(request.form.get('token'), request.form.get('message_id'), request.form.get('message')))


@APP.route('/message/react', methods=['POST'])
def react():
    """ Given a message within a channel the authorised user is part of, add a "react" to that particular message """
    return dumps(message.message_react(request.form.get('token'), request.form.get('message_id'), request.form.get('react_id')))


@APP.route('/message/unreact', methods=['POST'])
def unreact():
    """ Given a message within a channel the authorised user is part of, remove a "react" to that particular message """
    return dumps(message.message_unreact(request.form.get('token'), request.form.get('message_id'), request.form.get('react_id')))


@APP.route('/message/pin', methods=['POST'])
def pin():
    """ Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend """
    return dumps(message.message_pin(request.form.get('token'), request.form.get('message_id')))


@APP.route('/message/unpin', methods=['POST'])
def unpin():
    """ Given a message within a channel, remove it's mark as unpinned """
    return dumps(message.message_unpin(request.form.get('token'), request.form.get('message_id')))



# USER

@APP.route('/users/all', methods=['GET'])
def users():
    """ Get all the users information """
    return dumps(user.users_all(request.args.get('token')))


@APP.route('/user/profile', methods=['GET'])
def profile():
    """ For a valid user, returns information about their email, first name, last name, and handle """
    return dumps(user.user_profile(request.args.get('token'), request.args.get('u_id')))


@APP.route('/user/profile/setname', methods=['PUT'])
def setname():
    """ Update the authorised user's first and last name """
    return dumps(user.user_profile_setname(request.form.get('token'), request.form.get('name_first'), request.form.get('name_last')))


@APP.route('/user/profile/setemail', methods=['PUT'])
def setemail():
    """ Update the authorised user's email addredss """
    return dumps(user.user_profile_setemail(request.form.get('token'), request.form.get('email')))


@APP.route('/user/profile/sethandle', methods=['PUT'])
def sethandle():
    """ Update the authorised user's handle """
    return dumps(user.user_profile_sethandle(request.form.get('token'), request.form.get('handle_str')))


@APP.route('/user/profiles/uploadphoto', methods=['POST'])
def uploadphoto():
    """ Given a URL of an image on the internet, crops the image within bounds (x_start, y_start) and (x_end, y_end). Position (0,0) is the top left. """
    return dumps(user.user_profiles_uploadphoto(request.form.get('token'), request.form.get('img_url'), request.form.get('x_start'), request.form.get('y_start'), request.form.get('x_end'), request.form.get('y_end'), request.host))



# STANDUP

@APP.route('/standup/active', methods=['GET'])
def active():
    """ For a given channel, return whether a standup is active in it, and what time the standup finishes. If no standup is active, then time_finish returns None """
    return dumps(standup.standup_active(request.args.get('token'), request.args.get('channel_id')))


@APP.route('/standup/start', methods=['POST'])
def start():
    """ For a given channel, start the standup period whereby for the next "length" seconds if someone calls "standup_send" with a message, it is buffered during the X second window then at the end of the X second window a message will be added to the message queue in the channel from the user who started the standup. X is an integer that denotes the number of seconds that the standup occurs for """
    return dumps(standup.standup_start(request.form.get('token'), request.form.get('channel_id'), request.form.get('length')))


@APP.route('/standup/send', methods=['POST'])
def send():
    """ Sending a message to get buffered in the standup queue, assuming a standup is currently active """
    return dumps(standup.standup_send(request.form.get('token'), request.form.get('channel_id'), request.form.get('message')))



# OTHER

@APP.route('/search', methods=['GET'])
def search_messages():
    """ Given a query string, return a collection of messages in all of the channels that the user has joined that match the query """
    return dumps(search.search(request.args.get('token'), request.args.get('query_str')))


@APP.route('/admin/userpermission/change', methods=['POST'])
def userpermission_change():
    """ Set a user's permissions """
    return dumps(admin.admin_userpermission_change(request.form.get('token'), request.form.get('u_id'), request.form.get('permission_id')))


if __name__ == '__main__':
    if os.path.exists('export.json'):
        load()
    else:
        clear()
    save()
    APP.run(host='0.0.0.0', port=(sys.argv[1] if len(sys.argv) > 1 else 5000))

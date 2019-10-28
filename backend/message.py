""" Message functions """
from time import time
from threading import Timer

from backend.database import get_data, get_channel, get_message, get_permission, get_message_channel
from backend.helpers.token import get_user_from_token
from backend.helpers.helpers import check_user_in_channel
from backend.helpers.exception import ValueError, AccessError

def message_sendlater(token, channel_id, message, time_sent):
    time_sent = int(time_sent) / 1000
    timeout = int(time_sent) - int(time())
    if timeout < 0:
        raise ValueError("Time sent is a time in the past")
    send = Timer(timeout, message_send, (token, channel_id, message))
    send.start()


def message_send(token, channel_id, message):
    channel_id = int(channel_id)
    message_id = 0
    u_id = get_user_from_token(token)
    if len(message) > 1000:
        raise ValueError('Message is more than 1000 characters')

    message_channel = get_channel(channel_id)
    for channel in get_data()['channel']:
        message_id += len(channel['messages'])

    if message_channel is None:
        raise ValueError('Channel ID is not a valid channel')

    for member in message_channel['members']:
        if member['u_id'] == u_id:
            message_channel['messages'].append({'message_id': message_id, 'u_id': u_id, 'message': message, 'time_created': time(), 'reacts': [], 'is_pinned': False})
            message = get_message(message_id)
            message['reacts'].append({'react_id': 1, 'u_ids': [], 'is_this_user_reacted': False})
            return {'message_id': message_id}
    raise AccessError("the authorised user has not joined the channel they are trying to post to")


def message_remove(token, message_id):
    message_id = int(message_id)
    mess = get_message(message_id)

    channel_list = get_data()['channel']
    user_id = get_user_from_token(token)
    # value error: message with message_id does not exist
    if mess is None:
        raise ValueError("Message no longer exists")

    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                owners_channel = channel

    # access error: authorised user did not send the message and are not an admin or owner of slackr
    if mess['u_id'] != user_id:
        if get_permission(user_id) == 3:
            raise AccessError("Don't have permission to remove message")

        for owner in owners_channel['owners']:
            if owner['u_id'] == u_id:
                remove = True

        if not remove:
            raise AccessError("Don't have permission to remove message")

    # remove the message
    owners_channel['messages'].remove(mess)
    return {}


def message_edit(token, message_id, message):
    message_id = int(message_id)
    mess = get_message(message_id)

    channel_list = get_data()['channel']
    user_id = get_user_from_token(token)
    # value error: message with message_id does not exist
    if mess is None:
        raise ValueError("Message no longer exists")

    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                owners_channel = channel

    # access error: authorised user did not send the message and are not an admin or owner of slackr
    if mess['u_id'] != user_id:
        if get_permission(user_id) == 3:
            raise AccessError("Don't have permission to remove message")

        for owner in owners_channel['owners']:
            if owner['u_id'] == u_id:
                remove = True

        if not remove:
            raise AccessError("Don't have permission to remove message")

    # edit the message
    mess['message'] = message
    # leave the time_created and u_id the same
    return {}


def message_react(token, message_id, react_id):
    message_id = int(message_id)
    react_id = int(react_id)
    channel_list = get_data()['channel']
    mess = get_message(message_id)

    # value error: message_id is not valid
    if mess is None:
        raise ValueError("message_id is not valid")
    # value error: react_id is not a valid react id
    if react_id != 1:
        raise ValueError("react_id is not a valid React ID")
    # value error: user has already reacted to the message
    for react in mess['reacts']:
        if react['react_id'] == react_id:
            if react['is_this_user_reacted']:
                raise ValueError("Message already contains a react_id from user")

    # add the react to the message
    for react in mess['reacts']:
        if react['react_id'] == react_id:
            react['is_this_user_reacted']
            react['u_ids'].append(get_user_from_token(token))
    return {}


def message_unreact(token, message_id, react_id):
    message_id = int(message_id)
    react_id = int(react_id)
    channel_list = get_data()['channel']
    mess = get_message(message_id)
    print(mess)

    # value error: message_id is not valid
    if mess is None:
        raise ValueError("message_id is not valid")
    # value error: react_id is not a valid react id
    if react_id != 1:
        raise ValueError("react_id is not a valid React ID")
    # value error: user has already reacted to the message
    for react in mess['reacts']:
        if react['react_id'] == react_id:
            if not react['is_this_user_reacted']:
                raise ValueError("Message already contains a react_id from user")

    # remove the react to the message
    for react in mess['reacts']:
        if react['react_id'] == react_id:
            react['is_this_user_reacted'] = False
            react['u_ids'].remove(get_user_from_token(token))
    return {}


def message_pin(token, message_id):
    message_id = int(message_id)
    mess = get_message(message_id)

    # get initial data
    channel_list = get_data()['channel']
    user_id = get_user_from_token(token)

    # value error: message_id is not valid
    if mess is None:
        raise ValueError("message_id is not valid")
    # value error: message is already pinned
    if mess['is_pinned']:
        raise ValueError("Message is already pinned")
    # access error: authorised user is not apart of the channel
    channel = get_message_channel(message_id)
    if not check_user_in_channel(user_id, channel):
        raise AccessError("User is not a member of the channel")
    # value error: authorised user is not an admin
    if get_permission(user_id) == 3: #(assumption: owner of the slackr has permission)
        raise ValueError("User is not an admin")

    # pin the message
    mess['is_pinned'] = True
    return {}


def message_unpin(token, message_id):
    message_id = int(message_id)
    mess = get_message(message_id)

    # get initial data
    channel_list = get_data()['channel']
    user_id = get_user_from_token(token)

    # value error: message_id is not valid
    if mess is None:
        raise ValueError("message_id is not valid")
    # value error: message is already pinned
    if not mess['is_pinned']:
        raise ValueError("Message is already pinned")
    # access error: authorised user is not apart of the channel
    channel = get_message_channel(message_id)
    if not check_user_in_channel(user_id, channel):
        raise AccessError("User is not a member of the channel")
    # value error: authorised user is not an admin
    if get_permission(user_id) == 3: #(assumption: owner of the slackr has permission)
        raise ValueError("User is not an admin")

    # unpin the message
    mess['is_pinned'] = False
    return {}

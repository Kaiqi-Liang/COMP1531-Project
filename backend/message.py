""" Message functions """
from time import time
from threading import Timer

from backend.database import get_data, get_channel, get_message, get_permission
from backend.helpers.token import get_user_from_token
from backend.helpers.helpers import check_user_in_channel, get_message_channel, is_owner
from backend.helpers.exception import ValueError, AccessError

def message_sendlater(token, channel_id, message, time_sent):
    time_sent = float(time_sent)
    timeout = time_sent - time()
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
    message = get_message(message_id)
    u_id = get_user_from_token(token)
    channel = get_message_channel(message_id)
    if channel is None:
        return {}

    # message with message_id does not exist
    if message is None:
        raise ValueError("Message no longer exists")

    if message['u_id'] != u_id:
        if not is_owner(u_id, channel) and get_permission(u_id) == 3:
            raise AccessError("Don't have permission to remove message")

    # remove the message
    channel['messages'].remove(message)
    return {}


def message_edit(token, message_id, message):
    message_id = int(message_id)
    msg = get_message(message_id)
    u_id = get_user_from_token(token)
    channel = get_message_channel(message_id)
    if channel is None:
        return {}

    # message with message_id does not exist
    if msg is None:
        return {}

    if msg['u_id'] != u_id:
        if not is_owner(u_id, channel) and get_permission(u_id) == 3:
            raise AccessError("Don't have permission to edit message")

    if message == '':
        message_remove(token, message_id)
    # edit the message
    msg['message'] = message
    # assumption: leave the time_created and u_id the same
    return {}


def message_react(token, message_id, react_id):
    message_id = int(message_id)
    react_id = int(react_id)

    u_id = get_user_from_token(token)
    channel = get_message_channel(message_id)
    # value error: message_id is not a valid message within a channel that the authorised user has joined
    if not check_user_in_channel(u_id, channel):
        raise ValueError("the authorised user is not in the channel")

    msg = get_message(message_id)
    # value error: message_id is not valid
    if msg is None:
        raise ValueError("message_id is not valid")
    # value error: react_id is not a valid react id
    if react_id != 1:
        raise ValueError("react_id is not a valid React ID")
    # value error: user has already reacted to the message
    for react in msg['reacts']:
        if react['react_id'] == react_id:
            if react['is_this_user_reacted']:
                raise ValueError("Message already contains a react_id from user")

    # add the react to the message
    for react in msg['reacts']:
        if react['react_id'] == react_id:
            react['is_this_user_reacted'] = True
            react['u_ids'].append(get_user_from_token(token))
    return {}


def message_unreact(token, message_id, react_id):
    message_id = int(message_id)
    react_id = int(react_id)

    u_id = get_user_from_token(token)
    channel = get_message_channel(message_id)
    # value error: message_id is not a valid message within a channel that the authorised user has joined
    if not check_user_in_channel(u_id, channel):
        raise ValueError("the authorised user is not in the channel")

    msg = get_message(message_id)
    # value error: message_id is not valid
    if msg is None:
        raise ValueError("message_id is not valid")
    # value error: react_id is not a valid react id
    if react_id != 1:
        raise ValueError("react_id is not a valid React ID")
    # value error: user has already reacted to the message
    for react in msg['reacts']:
        if react['react_id'] == react_id:
            if not react['is_this_user_reacted']:
                raise ValueError("Message already contains a react_id from user")

    # remove the react to the message
    for react in msg['reacts']:
        if react['react_id'] == react_id:
            react['is_this_user_reacted'] = False
            react['u_ids'].remove(u_id)
    return {}


def message_pin(token, message_id):
    message_id = int(message_id)
    msg = get_message(message_id)
    u_id = get_user_from_token(token)
    channel = get_message_channel(message_id)
    if channel is None:
        return {}

    # value error: message_id is not valid
    if msg is None:
        raise ValueError("message_id is not valid")
    # value error: message is already pinned
    if msg['is_pinned']:
        raise ValueError("Message is already pinned")
    # access error: authorised user is not apart of the channel
    if not check_user_in_channel(u_id, channel):
        raise AccessError("User is not a member of the channel")
    # value error: authorised user is not an admin
    if get_permission(u_id) == 3 and not is_owner(u_id, channel):
        # assumption: owner of the slackr has permission
        raise ValueError("User is neither an admin nor an owner of the channel")

    # pin the message
    msg['is_pinned'] = True
    return {}


def message_unpin(token, message_id):
    message_id = int(message_id)
    msg = get_message(message_id)
    u_id = get_user_from_token(token)
    channel = get_message_channel(message_id)
    if channel is None:
        return {}

    # value error: message_id is not valid
    if msg is None:
        raise ValueError("message_id is not valid")
    # value error: message is already unpinned
    if not msg['is_pinned']:
        raise ValueError("Message is already unpinned")
    # access error: authorised user is not apart of the channel
    if not check_user_in_channel(u_id, channel):
        raise AccessError("User is not a member of the channel")
    # value error: authorised user is not an admin
    if get_permission(u_id) == 3 and not is_owner(u_id, channel):
        # assumption: owner of the slackr has permission
        raise ValueError("User is neither an admin nor an owner of the channel")

    # unpin the message
    msg['is_pinned'] = False
    return {}

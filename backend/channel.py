""" Local packages """
from backend.database import get_data
from backend.helpers.token import get_user_from_token
from backend.helpers.exception import ValueError, AccessError
from backend.helpers.helpers import *


def channel_invite(token, channel_id, u_id):
    raise ValueError


def channel_details(token, channel_id):
    u_id = get_user_from_token(token)
    for channel in get_data()['channel']:
        if channel['channel_id'] == channel_id and u_id in channel['members']:
            return {'name': channel['name'], 'owner_members': channel['owners'], 'all_members': channel['members']}

        if channel['channel_id'] == channel_id and u_id not in channel['members']:
            raise AccessError("Authorised user is not a member of channel with channel_id")

    raise ValueError("Channel ID is not a valid channel")


def channel_messages(token, channel_id, start):
    u_id = get_user_from_token(token)
    for channel in get_data()['channel']:
        if channel['channel_id'] == channel_id and u_id in channel['members']:
            if start >= len(channel['messages']):
                raise ValueError("start is greater than or equal to the total number of messages in the channel")

            messages = []
            for message in channel['messages']:
                if message['message_id'] < start:
                    continue

                messages.append(message)

                if len(messages) == 50:
                    break

            end = messages[-1]['message_id']
            return {'messages': messages, 'start': start, 'end': end}

        if channel['channel_id'] == channel_id and u_id not in channel['members']:
            raise AccessError("Authorised user is not a member of channel with channel_id")

    raise ValueError("Channel ID is not a valid channel")


def channel_leave(token, channel_id):
    channel = is_valid_channel(channel_id)
    if channel == None:
        raise ValueError("Channel ID is not a valid channel")
    u_id = get_user_from_token(token)
    channel['members'].remove(u_id)

def channel_join(token, channel_id):
    channel = is_valid_channel(channel_id)
    if channel == None:
        raise ValueError("Channel ID is not a valid channel")
    u_id = get_user_from_token(token)

    


def channel_addowner(token, channel_id, u_id):
    raise ValueError


def channel_removeowner(token, channel_id, u_id):
    raise ValueError


def channels_list(token):
    u_id = get_user_from_token(token)
    channels = []
    for channel in get_data()['channel']:
        if u_id in channel['members']:
            channels.append({'channel_id': channel['channel_id'], 'name': channel['name']})
    return {'channels': channels}


def channels_listall(token):
    u_id = get_user_from_token(token)
    channels = []
    for channel in get_data()['channel']:
            channels.append({'channel_id': channel['channel_id'], 'name': channel['name']})
    return {'channels': channels}

def channels_create(token, name, is_public):
    if len(name) > 20:
        raise ValueError('Name is more than 20 characters long')
    channels = get_data()['channel']
    channel_id = len(channels) + 1
    channels.append({
        'name': name,
        'channel_id': channel_id,
        'is_public': is_public,
        'owners': [],
        'members': []
    })

    u_id = get_user_from_token(token)
    for channel in channels:
        if channel_id == channel['channel_id']:
            channel['owners'].append(u_id)
            channel['members'].append(u_id)

    return {'channel_id': channel_id}

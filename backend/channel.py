""" Local packages """
from backend.database import get_data
from backend.helpers.token import get_user_from_token
from backend.helpers.exception import ValueError, AccessError


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
            return {'name': channel['name'], 'owner_members': channel['owners'], 'all_members': channel['members']}

        if channel['channel_id'] == channel_id and u_id not in channel['members']:
            raise AccessError("Authorised user is not a member of channel with channel_id")

    raise ValueError("Channel ID is not a valid channel")


def channel_leave(token, channel_id):
    raise ValueError


def channel_join(token, channel_id):
    raise ValueError


def channel_addowner(token, channel_id, u_id):
    raise ValueError


def channel_removeowner(token, channel_id, u_id):
    raise ValueError


def channels_list(token):
    u_id = get_user_from_token
    channels = []
    for channel in get_data()['channel']:
        if u_id in channel['members']:
            channels.append({'channel_id': channel['channel_id'], 'name': channel['name']})
    return {'channels': channels}


def channels_listall(token):
    u_id = get_user_from_token
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

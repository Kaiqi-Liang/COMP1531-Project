""" Local packages """
from backend.database import get_data
from backend.helpers.token import get_user_from_token
from backend.helpers.exception import ValueError, AccessError


def channel_invite(token, channel_id, u_id):
    #invite user to join a channel
    for user in u_id:
        invited = True
    #once invited user is added to channel immediately
        if invited:
            channel_join(u_id)

    if channel_id['channel_id'] != channel_id and u_id not in channel['members']:
        raise ValueError("Does not refer to a valid channel that the authorised user is part of")
    if u_id not in channel['name']:
        raise ValueError("Does not refer to a valid user")
    if u_id not in channel['members']:
        raise AccessError("the authorised user is not already a member of the channel")


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
    raise ValueError


def channel_join(token, channel_id):
    raise ValueError


def channel_addowner(token, channel_id, u_id):
    #Make user with user id u_id an owner of this channel
    channel['owners'].append(u_id)

    if channel['channel_id'] != channel_id:
        raise ValueError("Channel Id is not a valid channel")
    if u_id in channel['owners']:
        raise ValueError("User is already an owner of the channel")
    if 
        raise AccessError("User is not an owner of the slackr or of this channel")


def channel_removeowner(token, channel_id, u_id):
    channel['owners'].remove(u_id)

    if channel['channel_id'] != channel_id:
        raise ValueError("Channel Id is not a valid channel")
    if u_id not in channel['owners']:
        raise ValueError("User is already an owner of the channel")
    if 
        raise AccessError("User is not an owner of the slackr or of this channel")

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

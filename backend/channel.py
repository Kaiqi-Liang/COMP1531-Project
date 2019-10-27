""" Local packages """
from backend.database import get_data, get_user, get_channel
from backend.helpers.token import get_user_from_token
from backend.helpers.exception import ValueError, AccessError
from backend.helpers.helpers import *

''' Permission id globals '''
OWNER = 1
ADMIN = 2
MEMBER = 3


def channel_invite(token, channel_id, u_id):
    u_id = int(u_id)
    user = get_user(get_user_from_token(token))
    if user == None:
        raise ValueError("u_id does not refer to a valid user")

    channel = get_channel(channel_id)
    if channel == None:
        raise ValueError("channel_id does not refer to a valid channel that the authorised user is part of.")

    members = channel['members']
    for member in members:
        if user['u_id'] == member['u_id']:
            invite = get_user(u_id)
            channel['members'].append({'u_id': u_id, 'name_first': invite['name_first'], 'name_last': invite['name_last']})
            return {}

    raise AccessError("the authorised user is not already a member of the channel")


def channel_details(token, channel_id):
    channel = get_channel(channel_id)
    if channel == None:
        raise ValueError("Channel ID is not a valid channel")

    if not channel['is_public']:
        u_id = get_user_from_token(token)
        members = channel['members']
        for member in members:
            if u_id == member['u_id']:
                return {'name': channel['name'], 'owner_members': channel['owners'], 'all_members': channel['members']}
        raise AccessError("channel_details authorisation error")

    else:
        return {'name': channel['name'], 'owner_members': channel['owners'], 'all_members': channel['members']}



def channel_messages(token, channel_id, start):
    start = int(start)
    channel_id = int(channel_id)
    channel = get_channel(channel_id)
    if channel == None:
        raise ValueError("Channel ID is not a valid channel")

    u_id = get_user_from_token(token)
    members = channel['members']
    for user in members:
        if u_id == user['u_id']:
            if start > len(channel['messages']):
                raise ValueError("start is greater than or equal to the total number of messages in the channel")

            messages = []
            for message in channel['messages']:
                if message['message_id'] < start:
                    continue

                messages.append(message)

                if len(messages) == 50:
                    break

            if len(messages) == 0:
                return {'messages': messages, 'start': start, 'end': -1}
            else:
                end = messages[-1]['message_id']
                return {'messages': messages, 'start': start, 'end': end}

    raise AccessError("Authorised user is not a member of channel with channel_id")


def channel_leave(token, channel_id):
    channel = get_channel(channel_id)
    if channel == None:
        raise ValueError("Channel ID is not a valid channel")

    u_id = get_user_from_token(token)
    members = channel['members']
    owners = channel['owners']
    for member in members:
        if u_id == member['u_id']:
            members.remove(member)
    for owner in owners:
        if u_id == owner['u_id']:
            owners.remove(owner)
    if len(owners) == 0 and len(members) == 0:
        get_data()['channel'].remove(channel)
    return {}


def channel_join(token, channel_id):
    users = get_data()['user']

    channel = is_valid_channel(channel_id)
    if channel == None:
        raise ValueError("Channel ID is not a valid channel")
    u_id = get_user_from_token(token)
    user = get_user(u_id)

    # If user is already in channel, ignore
    if check_in_channel(token, user['u_id']):
        return {}

    member_info = {
        'u_id': user['u_id'],
        'name_first': user['name_first'],
        'name_last': user['name_last']
    }

    # If channel is public
    if channel['is_public']:
        channel['members'].append(member_info)
    else:
        # If user is not an admin/owner (assumptions)
        if not check_permission(u_id, OWNER) and not check_permission(u_id, ADMIN):
            raise AccessError("User is not admin: unable to join private channel")
        else:
            # User is an admin/owner and can join channel
            channel['owners'].append(member_info)
            channel['members'].append(member_info)

    return {}


def channel_addowner(token, channel_id, u_id):
    #Make user with user id u_id an owner of this channel
    channel = is_valid_channel(channel_id)
    if channel == None:
        raise ValueError("Channel ID is not a valid channel")
    if u_id in channel['owners']:
        raise ValueError("User is already an owner of the channel")
    else:
        raise AccessError("User is not an owner of the slackr or of this channel")

    channel['owners'].append(u_id)


def channel_removeowner(token, channel_id, u_id):
    #Remove user with user id u_id an owner of this channel
    channel = is_valid_channel(channel_id)
    if channel == None:
        raise ValueError("Channel ID is not a valid channel")
    if u_id not in channel['owners']:
        raise ValueError("User is already an owner of the channel")
    else:
        raise AccessError("User is not an owner of the slackr or of this channel")

    channel['owners'].remove(u_id)


def channels_list(token):
    u_id = get_user_from_token(token)
    channels = []
    for channel in get_data()['channel']:
        members = channel['members']
        for member in members:
            if u_id == member['u_id']:
                channels.append({'channel_id': channel['channel_id'], 'name': channel['name']})
    return {'channels': channels}


def channels_listall(token):
    u_id = get_user_from_token(token)
    channels = []
    for channel in get_data()['channel']:
        if channel['is_public']:
            channels.append({'channel_id': channel['channel_id'], 'name': channel['name']})
    return {'channels': channels}


def channels_create(token, name, is_public):
    if is_public == 'true':
        is_public = True
    elif is_public == 'false':
        is_public = False
    if len(name) > 20:
        raise ValueError('Name is more than 20 characters long')
    channels = get_data()['channel']
    channel_id = len(channels) + 1
    channels.append({
        'name': name,
        'channel_id': channel_id,
        'is_public': is_public,
        'owners': [],
        'members': [],
        'messages': []
    })

    channel = get_channel(channel_id)
    u_id = get_user_from_token(token)
    user = get_user(u_id)
    if channel and user:
        channel['owners'].append({'u_id': u_id, 'name_first': user['name_first'], 'name_last': user['name_last']})
        channel['members'].append({'u_id': u_id, 'name_first': user['name_first'], 'name_last': user['name_last']})

    return {'channel_id': channel_id}

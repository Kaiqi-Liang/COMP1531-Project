""" Channel functions """
from backend.database import get_data, get_user, get_channel, get_permission
from backend.helpers.token import get_user_from_token
from backend.helpers.helpers import check_user_in_channel, is_owner
from backend.helpers.exception import ValueError, AccessError

def channel_invite(token, channel_id, u_id):
    user = get_user(u_id)
    if user is None:
        raise ValueError("u_id does not refer to a valid user")

    channel = get_channel(channel_id)
    if channel is None:
        raise ValueError("channel_id does not refer to a valid channel that the authorised user is part of.")

    if check_user_in_channel(u_id, channel):
        return {}

    if not check_user_in_channel(get_user_from_token(token), channel):
        raise AccessError("the authorised user is not already a member of the channel")

    if get_permission(u_id) == 1 or get_permission(u_id) == 2:
        channel['owners'].append({'u_id': u_id, 'name_first': user['name_first'], 'name_last': user['name_last'], 'profile_img_url': user['profile_img_url']})

    channel['members'].append({'u_id': u_id, 'name_first': user['name_first'], 'name_last': user['name_last'], 'profile_img_url': user['profile_img_url']})
    return {}


def channel_details(token, channel_id):
    channel = get_channel(channel_id)
    if channel is None:
        raise ValueError("Channel ID is not a valid channel")

    u_id = get_user_from_token(token)
    if not channel['is_public']:
        if check_user_in_channel(u_id, channel) or get_permission(u_id) in [1, 2]:
            return {'name': channel['name'], 'owner_members': channel['owners'], 'all_members': channel['members']}
        raise AccessError("Authorised user is not a member of channel with channel_id")
    return {'name': channel['name'], 'owner_members': channel['owners'], 'all_members': channel['members']}


def channel_messages(token, channel_id, start):
    start = int(start)
    pg_threshold = 50
    channel_id = int(channel_id)
    u_id = get_user_from_token(token)
    channel = get_channel(channel_id)
    if channel is None:
        raise ValueError("Channel ID is not a valid channel")

    if start > len(channel['messages']):
        raise ValueError("start is greater than or equal to the total number of messages in the channel")

    # if channel is private and the user is neither in the channel nor an owner or admin of slackr
    if not channel['is_public'] and not check_user_in_channel(u_id, channel) and get_permission(u_id) == 3:
        raise AccessError("Authorised user is not a member of channel with channel_id")

    messages = []
    for message in channel['messages']:
        message['reacts'][0]['is_this_user_reacted'] = u_id in message['reacts'][0]['u_ids']

    not_displayed = list(reversed(channel['messages']))[start:]
    messages.extend(not_displayed[:min(pg_threshold, len(not_displayed))])

    end = -1 if len(messages) == len(not_displayed) else start + pg_threshold

    return {'messages': messages, 'start': start, 'end': end}


def channel_leave(token, channel_id):
    channel = get_channel(channel_id)
    if channel is None:
        raise ValueError("Channel ID is not a valid channel")

    u_id = get_user_from_token(token)
    if not check_user_in_channel(u_id, channel):
        raise AccessError("Authorised user is not a member of channel with channel_id")

    members = channel['members']
    owners = channel['owners']
    if is_owner(u_id, channel):
        # assumption: cannot leave the channel if user is the only owner of the channel
        if len(owners) == 1 and len(members) > 1:
            return {}

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
    channel = get_channel(channel_id)
    if channel is None:
        raise ValueError("Channel ID is not a valid channel")
    u_id = get_user_from_token(token)
    user = get_user(u_id)

    # If user is already in channel, ignore
    if check_user_in_channel(user['u_id'], channel):
        return {}

    owner_info = {
        'u_id': user['u_id'],
        'name_first': user['name_first'],
        'name_last': user['name_last']
    }

    member_info = {
        'u_id': user['u_id'],
        'name_first': user['name_first'],
        'name_last': user['name_last'],
        'profile_img_url': user['profile_img_url']
    }

    p_id = get_permission(u_id)
    admin_or_owner = [1, 2]
    # If channel is public
    if channel['is_public']:
        if p_id in admin_or_owner:
            channel['owners'].append(owner_info)
        channel['members'].append(member_info)
    else:
        # If user is not an admin
        if not p_id in admin_or_owner:
            # assumptions: if user is not an owner
            raise AccessError("channel_id refers to a channel that is private")

        # User is an admin/owner and can join channel
        channel['members'].append(member_info)
        channel['owners'].append(owner_info)

    return {}


def channel_addowner(token, channel_id, u_id):
    user_id = get_user_from_token(token)
    channel = get_channel(channel_id)
    if channel is None:
        raise ValueError("Channel ID is not a valid channel")
    if is_owner(u_id, channel):
        raise ValueError("User is already an owner of the channel")
    if not is_owner(user_id, channel):
        raise AccessError("User is not an owner of the slackr or of this channel")

    user = get_user(u_id)
    channel['owners'].append({'u_id': user['u_id'], 'name_first': user['name_first'], 'name_last': user['name_last'], 'profile_img_url': user['profile_img_url']})
    return {}


def channel_removeowner(token, channel_id, u_id):
    u_id = int(u_id)
    user_id = get_user_from_token(token)
    channel = get_channel(channel_id)
    if channel is None:
        raise ValueError("Channel ID is not a valid channel")
    if not is_owner(u_id, channel):
        raise ValueError("When user with user id u_id is not an owner of the channel")
    if not is_owner(user_id, channel) and user_id not in get_data()['slackr']['owner']:
        raise AccessError("User is not an owner of the slackr or of this channel")

    permissions = get_data()['slackr']
    if len(channel['owners']) != 1 and u_id not in permissions['admin'] and u_id not in permissions['owner']:
        user = get_user(u_id)
        channel['owners'].remove({'u_id': user['u_id'], 'name_first': user['name_first'], 'name_last': user['name_last'], 'profile_img_url': user['profile_img_url']})
    return {}


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
    channels = []
    for channel in get_data()['channel']:
        if not channel['is_public'] and get_permission(get_user_from_token(token)) == 3:
            continue
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
        channel['owners'].append({'u_id': u_id, 'name_first': user['name_first'], 'name_last': user['name_last'], 'profile_img_url': user['profile_img_url']})
        channel['members'].append({'u_id': u_id, 'name_first': user['name_first'], 'name_last': user['name_last'], 'profile_img_url': user['profile_img_url']})

    return {'channel_id': channel_id}

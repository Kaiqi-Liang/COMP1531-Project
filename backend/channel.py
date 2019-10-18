''' Local packages '''
from backend.database import get_data
from backend.helpers.token import generate_token, get_user_from_token

def channel_invite(token, channel_id, u_id):
    raise ValueError

def channel_details(token, channel_id):
    raise ValueError
    raise AccessError

def channel_messages(token, channel_id, start):
    raise ValueError

def channel_leave(token, channel_id):
    raise ValueError

def channel_join(token, channel_id):
    raise ValueError

def channel_addowner(token, channel_id, u_id):
    raise ValueError

def channel_removeowner(token, channel_id, u_id):
    raise ValueError

def channels_list(token):
    pass

def channels_listall(token):
    pass

def channels_create(token, name, is_public):
    if len(name) > 20:
        raise ValueError
    channels = get_data()['channel']
    channel_id = len(channels + 1)
    channels.append({
        'channel_id': channel_id,
        'is_public': is_public,
        'owners': []
        'members': []
    })

    u_id = get_user_from_token(token) 
    for channel in channels:
        if channel_id == channel['channel_id']:
            channel['owners'].append(u_id)
            channel['members'].append(u_id)

    return {'channel_id': channel_id}

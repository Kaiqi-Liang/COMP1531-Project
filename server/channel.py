def channel_invite(token, channel_id, u_id):
    raise ValueError

def channels_create(token, name, is_public):
    if len(name) > 20:
        raise ValueError

def channel_details(token, channel_id):
    raise ValueError
    raise AccessError


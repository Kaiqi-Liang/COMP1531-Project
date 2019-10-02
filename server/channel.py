from access_error import AccessError

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

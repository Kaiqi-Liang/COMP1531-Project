DATA = {
    'user': [],
    'channel': [],
    'slackr': []
}

'''
DATA = {
    'user':
        [
            {
                'u_id': u_id,
                'email': 'email',
                'password': hash,
                'name_first': 'first',
                'name_last': 'last',
                'handle': 'firstlast',
                'permission_id': p_id,
                'tokens': ['token'],
                'reset': ''
            }
        ],
    'channel':
        [
            {
                'channel_id': channel_id,
                'name': 'name',
                'is_public': True,
                'owners': [
                                {
                                    'u_id': u_id,
                                    'name_first': 'first',
                                    'name_last': 'last'
                                }
                          ],
                'members': [
                                {
                                    'u_id': u_id,
                                    'name_first': 'first',
                                    'name_last': 'last'
                                }
                          ],
                'messages': [
                                {
                                    'message_id': message_id,
                                    'u_id': u_id,
                                    'message': 'message',
                                    'time_created': time,
                                    'reacts': [
                                                  {
                                                       'react_id': 1,
                                                       'u_ids, [u_id],
                                                       'is_this_user_reacted': True
                                                  }
                                              ],
                                    'is_pinned': True
                                }
                            ]
            }
        ],
    'slackr':
        [
            {
                OWNER: [u_id],
                ADMIN: [u_id],
                MEMBER: [u_id]
            }
        ]
'''

def get_data():
    ''' get global variable i.e. database'''
    global DATA
    return DATA

def get_user(u_id):
    for user in get_data()['user']:
        if int(u_id) == user['u_id']:
            return user
    return None

def get_channel(channel_id):
    for channel in get_data()['channel']:
        if int(channel_id) == channel['channel_id']:
            return channel
    return None

''' Return message dict'''
def get_message(message_id):
    channel_list = get_data()['channel']
    for channel in channel_list:
        for mess in channel['messages']:
            if mess['message_id'] == int(message_id):
                return mess
    return None 

''' Get user permission_id '''
def get_permission(user_id):
    users = get_data()['user']
    for user in users:
        if int(user_id) == user['u_id']:
            return user['permission_id']
    return None

def get_message_channel(message_id):
    channels = get_data()['channel']
    for channel in channels:
        for message in channel['messages']:
            if int(message_id) == message['message_id']:
                return channel
    return None
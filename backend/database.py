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
                                                       'react_id': react_id,
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
        if u_id == user['u_id']:
            return user
    return None

def get_channel(channel_id):
    for channel in get_data()['channel']:
        if channel_id == channel['channel_id']:
            return channel
    return None

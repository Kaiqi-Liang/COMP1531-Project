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
                'owners': [u_id],
                'members': [u_id],
                'messages': [
                                {
                                    'message_id': message_id,
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

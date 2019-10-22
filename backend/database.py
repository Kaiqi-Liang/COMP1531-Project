DATA = {
    'user': [],
    'channel': [],
    'message': []
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
                'tokens': [],
                'reset': ''
            }
        ],
    'channel':
        [
            {
                'channel_id': channel_id,
                'name': 'name',
                'is_public': True,
                'owners': [],
                'members': [],
        ],
    'message':
        [
        ]
'''

def get_data():
    ''' get global variable ie. database'''
    global DATA
    return DATA

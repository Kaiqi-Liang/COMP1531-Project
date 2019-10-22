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
                'email': email,
                'password': hash,
                'name_first': first,
                'name_last': last,
                'handle': firstlast,
                'permission_id': p_id,
                'tokens': [],
                'reset': ''
            }
        ],
    'channel':
        [
        ],
    'message':
        [
        ]
'''

def get_data():
    ''' get global variable ie. database'''
    global DATA
    return DATA

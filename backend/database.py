DATA = {
    'user': [],
#   [{'u_id': u_id1, 'email': email1, 'password': password1}, {'u_id': u_id2, 'email': email2, 'password': password2}]
    'channel': [],
    'message': []
}

def get_data():
    ''' get global variable ie. database'''
    global DATA
    return DATA

""" Token functions """
import time
import jwt

SECRET = 'SAKE'
def generate_token(u_id):
    """ Generate token given a user id """
    global SECRET
    payload = {
        'timestamp': time.time(),
        'u_id': u_id
    }
    token = jwt.encode(payload, SECRET, algorithm='HS256')
    return token.decode()

def get_user_from_token(token):
    """ Return a user id from a given token """
    global SECRET
    return jwt.decode(token, SECRET, algorithm='HS256')['u_id']

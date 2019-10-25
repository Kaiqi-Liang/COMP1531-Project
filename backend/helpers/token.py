import jwt
import time

from ..database import get_data

SECRET = 'SAKE'
def generate_token(u_id):
    global SECRET
    payload = {
        'timestamp': time.time(),
        'u_id': u_id
    }
    token = jwt.encode(payload, SECRET, algorithm='HS256')
    return token.decode()

def get_user_from_token(token):
    global SECRET
    return jwt.decode(token, SECRET, algorithm='HS256')['u_id']

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

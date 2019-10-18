import jwt

SECRET = 'SAKE'
def generate_token(u_id):
    global SECRET
    token = jwt.encode({'u_id': u_id}, SECRET, algorithm='HS256')
    return token.decode()

def get_user_from_token(token):
    global SECRET
    return jwt.decode(token, SECRET, algorithm='HS256')['u_id']

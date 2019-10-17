import jwt
import re

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from app import get_data

EMAIL = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def check_email(email):
    if(re.search(EMAIL, email)):
        return True
    else:
        return False


''' token functions '''
SECRET = 'SAKE'
def generate_token(password):
    global SECRET
    token = jwt.encode({'password': password}, SECRET, algorithm='HS256')
    return token.decode()

def get_user_from_token(token):
    global SECRET
    return jwt.decode(token, SECRET, algorithm='HS256')['password']


''' auth functions '''
def auth_login(email, password):
    if not check_email(email):
        raise ValueError("Invalid login email")

    for user in get_data()['user']:
        if user['email'] == email and user['password'] == password:
            return {'u_id': user['u_id'], 'token': generate_token(password)}
        elif user['email'] == email and user['password'] != password:
            raise ValueError("Invalid password")

    raise ValueError('Email entered does not belong to a user')
    return {}

def auth_logout(token):
    password = get_user_from_token(token)

    for user in get_data()['user']:
        if user['email'] == email and user['password'] == password:
            return {True}

    return {False}

def auth_register (email,password,name_first,name_last):
    if email == "Invalid email":
        raise ValueError("Invalid email address")
    if email == "Existing email":
        raise ValueError("Email already exists")
    if len(password) < 5:
        raise ValueError("Invalid password")
    if len(name_first) > 50:
        raise ValueError("First Name is too long")
    if len(name_last) > 50:
        raise ValueError("Last Name is too long")
    loginDict = {}
    loginDict['u_id'] = 123
    loginDict['token'] = '555'
    return loginDict

def auth_passwordreset_request (email):
    if email == "":
        raise ValueError("No email")
    return

def auth_passwordreset_reset (reset_code, new_password):
    if reset_code == "Invalid reset code":
        raise ValueError("Invalid reset code")
    if len(new_password) < 5:
        raise ValueError("Invalid password")
    return

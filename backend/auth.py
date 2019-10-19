import jwt
import re
import random 

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from server import get_data

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
    return {'Error'}


def auth_logout(token):
    password = get_user_from_token(token)

    for user in get_data()['user']:
        if user['email'] == email and user['password'] == password:
            return {True}

    return {False}

def auth_logout(token):
    password = get_user_from_token(token)

    for user in get_data()['user']:
        if user['email'] == email and user['password'] == password:
            return {True}

    return {False}

def auth_register (email,password,name_first,name_last):

    users = get_data()['user']

    # Value error: password is less than 6 characters long
    if len(password) < 6:
        raise ValueError("Password entered is less than 6 characters long")
    # Value error: name_first 
    if len(name_first) >= 50 or len(name_first) <= 1:
        raise ValueError("First name is not within the correct length range")
    # Value error: name_last
    if len(name_last) >= 50 or len(name_last) <= 1:
        raise ValueError("Last name is not within the correct length range")
    # Value error: invalid email
    if not check_email(email):
        raise ValueError("Email entered is invalid")
    # Value error: email is already being used -> potentially redo this, just check back on how i later store emails. 
    for user in users:
        if user['email'] == email:
            raise ValueError("Email already used on a registered account")  
        
    # CREATE A NEW ACCOUNT
    # generate a u_id, this method is based on the number of users
    numberUsers = len(users)
    u_id = (numberUsers + 1)
    
    # generate a handle that is a lowercase concatenation of their first and last name 
    handle = name_first.lower() + name_last.lower()
    if len(handle) > 20:
        handle = handle[:20]
    
    for user in users:
        if handle == user['handle']:
            if len(handle) >= 19:
                # cut some out
                handle = handle[:18]
                # then add number
                handle = handle + str(random.randit(10, 100)
             else:
                # just add number 
                handle = handle + str(random.randit(10, 100)

    # generate a token
    token = generate_token(password)

    # work out permission_id
    if len(users) is 0:
        p_id = 1
    else:
        p_id = 3

    # add this data to the DATA members list
    users.append({
        'name_first': name_first,
        'name_last' : name_last,
        'u_id' : u_id,
        'permission_id' : p_id,
        'email' : email,
        'handle': handle
    })

    return {
        'u_id' : u_id,
        'token' : token
    }

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

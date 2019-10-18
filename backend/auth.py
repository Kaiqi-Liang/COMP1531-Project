''' Local packages '''
from backend.database import get_data
from backend.helpers.token import generate_token, get_user_from_token
from backend.helpers.helpers import check_email

''' Std lib packages '''
import hashlib

def auth_login(email, password):
    if not check_email(email):
        raise ValueError("Invalid login email")

    for user in get_data()['user']:
        if user['email'] == email and user['password'] == hashlib.sha256(password.encode()).hexdigest():
            print(user['u_id'])
            return {'u_id': user['u_id'], 'token': generate_token(user['u_id'])}
        elif user['email'] == email and user['password'] != hashlib.sha256(password.encode()).hexdigest():
            raise ValueError("Invalid password")

    raise ValueError('Email entered does not belong to a user')
    return {'Error': 'Error'}

def auth_logout(token):
    u_id = get_user_from_token(token) 

    for user in get_data()['user']:
        if user['u_id'] == u_id:
            return {'is_success': True}

    return {'is_success': False}

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

    # check if the handle is already taken -> basing this on last names
    occurences = 0
    for user in users:
        if user['name_first'] == name_first and user['name_last'] == name_last:
            occurences += 1
    # deal with changing handles
    if len(handle) > 20 and occurences == 0:
        handle = handle[:20]
    elif len(handle) > 18 and occurences > 0:
        handle = handle[:18]
        handle = hande + str(occurences)
    else:
        handle = handle + str(occurences)

    # generate a token
    token = generate_token(u_id)

    # work out permission_id
    if len(users) is 0:
        p_id = 1
    else:
        p_id = 3

    # add this data to the DATA members list
    # get this checked !!!!!
    users.append({
        'name_first': name_first,
        'name_last' : name_last,
        'u_id' : u_id,
        'token' : token,
        'permission_id' : p_id,
        'email' : email,
        'handle': handle,
        'password': hashlib.sha256(password.encode()).hexdigest()
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
    if isinstance(reset_code, str): # Check if reset_code is valid i.e. a string
        raise ValueError("Invalid reset code")
    if len(new_password) < 6:
        raise ValueError("Password entered is less than 6 characters long")
    return

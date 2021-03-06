""" Auth functions """
import hashlib
import random

from backend.database import get_data
from backend.helpers.token import generate_token, get_user_from_token
from backend.helpers.helpers import check_email
from backend.helpers.exception import ValueError

def auth_login(email, password):
    if not check_email(email):
        raise ValueError("Invalid login email")

    for user in get_data()['user']:
        if user['email'] == email:
            if user['password'] == hashlib.sha256(password.encode()).hexdigest():
                token = generate_token(user['u_id'])
                user['tokens'].append(token)
                return {'u_id': user['u_id'], 'token': token}

            raise ValueError("Invalid password")

    raise ValueError('Email entered does not belong to a user')


def auth_logout(token):
    u_id = get_user_from_token(token)
    for user in get_data()['user']:
        if user['u_id'] == u_id:
            user['tokens'].remove(token)
            return {'is_success': True}

    return {'is_success': False}


def auth_register(email, password, name_first, name_last):

    users = get_data()['user']

    # Value error: password is less than 6 characters long
    if len(password) < 6:
        raise ValueError("Password entered is less than 6 characters long")
    # Value error: name_first
    if len(name_first) >= 50 or len(name_first) < 1:
        raise ValueError("First name is not within the correct length range")
    # Value error: name_last
    if len(name_last) >= 50 or len(name_last) < 1:
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
    u_id = len(users) + 1

    # generate a handle_str that is a lowercase concatenation of their first and last name
    handle_str = name_first.lower() + name_last.lower()

    if len(handle_str) > 20:
        handle_str = handle_str[:20]

    for user in users:
        if handle_str == user['handle_str']:
            if len(handle_str) >= 19:
                # cut some out
                handle_str = handle_str[:18]
            # then add number
            handle_str = handle_str + str(random.randint(10, 100))

    # generate a token

    token = generate_token(u_id)

    # work out permission_id
    if len(users) == 0:
        p_id = 1
        get_data()['slackr']['owner'].append(u_id)
        get_data()['slackr']['admin'].append(u_id)
    else:
        p_id = 3
    get_data()['slackr']['member'].append(u_id)

    # add this data to the DATA members list
    users.append({
        'name_first': name_first,
        'name_last' : name_last,
        'u_id' : u_id,
        'permission_id' : p_id,
        'email' : email,
        'handle_str': handle_str,
        'tokens': [token],
        'password': hashlib.sha256(password.encode()).hexdigest(),
        'reset': None,
        'profile_img_url': None
    })

    return {
        'u_id' : u_id,
        'token' : token
    }


def auth_passwordreset_reset(reset_code, new_password):
    users = get_data()['user']

    if not isinstance(reset_code, str): # Check if reset_code is valid i.e. a string
        raise ValueError("Invalid reset code")
    if len(new_password) < 6:
        raise ValueError("Password entered is less than 6 characters long")

    for user in users:
        if user['reset'] == reset_code:
            user['password'] = hashlib.sha256(new_password.encode()).hexdigest()
            user['reset'] = None
    return {}

""" User functions """
from random import randint
from urllib import request

from backend.database import get_data, get_user
from backend.helpers.token import get_user_from_token
from backend.helpers.helpers import check_email, check_user_in_channel, is_owner, crop_image
from backend.helpers.exception import ValueError

def users_all(token):
    users = []
    if get_user(get_user_from_token(token)) is not None:
        for user in get_data()['user']:
            users.append({'u_id': user['u_id'], 'email': user['email'], 'name_first': user['name_first'], 'name_last': user['name_last'], 'handle_str':user['handle_str'], 'profile_img_url': 'profile_img_url'})
        return {'users': users}
    return {}


def user_profile(token, u_id):
    u_id = int(u_id)
    users = get_data()['user']
    if get_user(get_user_from_token(token)) is not None:
        user = get_user(u_id)
        if user is None:
            raise ValueError("User with u_id is not a valid user")
        return {'u_id': u_id, 'email': user['email'], 'name_first': user['name_first'], 'name_last': user['name_last'], 'handle_str':user['handle_str'], 'profile_img_url': user['profile_img_url']}
    return {}


def user_profile_setname(token, name_first, name_last):
    if len(name_first) > 50 or len(name_first) < 1:
        raise ValueError("name_first is not between 1 and 50 characters in length")
    if len(name_last) > 50 or len(name_last) < 1:
        raise ValueError("name_last is not between 1 and 50 characters in length")

    u_id = get_user_from_token(token)
    user = get_user(u_id)
    if user is not None:
        user['name_first'] = name_first
        user['name_last'] = name_last

        # change the name of the user in all the channels the user appears in
        for channel in get_data()['channel']:
            if check_user_in_channel(u_id, channel):
                for member in channel['members']:
                    if member['u_id'] == u_id:
                        member['name_first'] = name_first
                        member['name_last'] = name_last
            if is_owner(u_id, channel):
                for owner in channel['owners']:
                    if owner['u_id'] == u_id:
                        owner['name_first'] = name_first
                        owner['name_last'] = name_last
    return {}


def user_profile_setemail(token, email):
    if not check_email(email):
        raise ValueError("Invalid email address!")

    user = get_user(get_user_from_token(token))
    if user is not None:
        for users in get_data()['user']:
            if users['email'] == email:
                raise ValueError('Email address is already being used by another user')

        user['email'] = email
    return {}


def user_profile_sethandle(token, handle_str):
    u_id = get_user_from_token(token)
    user = get_user(u_id)
    users = get_data()['user']

    if len(handle_str) > 20 or len(handle_str) < 3:
        raise ValueError('Handle too long!')

    for user in users:
        if handle_str == user['handle_str']:
            if len(handle_str) >= 19:
                # cut some out
                handle_str = handle_str[:18]
            # then add number
            handle_str = handle_str + str(randint(10, 100))
    user['handle_str'] = handle_str
    return {}


def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    request.urlretrieve(img_url, photo)
    get_image(img_url, 'photo.jpg')
    crop_image('photo.jpg', int(x_start), int(y_start), int(x_end), int(y_end))

    if response.status_code != 200:
        raise ValueError("HTTP response unsuccessful!")
    elif x_start == x_end or y_start == y_end:
        raise ValueError("Invalid crop size!")
    elif x_start >= width or x_start < 0 or x_end >= width or x_end < 0:
        raise ValueError("Invalid width crop!")
    elif y_start >= height or y_start < 0 or y_end >= height or y_end < 0:
        raise ValueError("Invalid height crop!")
    return

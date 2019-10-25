""" Local packages """
from backend.database import get_data
from backend.helpers.token import get_user_from_token, get_user
from backend.helpers.helpers import * # helpers/*.py

''' pip3 packages '''
from PIL import Image # pip3 name is "Pillow"
import requests

''' Std lib packages '''
import urllib

def user_profile(token, u_id):
    u_id = int(u_id)
    users = get_data()['user']
    if get_user(get_user_from_token(token)) != None:
        for user in users:
            if u_id == user['u_id']:
                return {'email': user['email'], 'name_first': user['name_first'], 'name_last': user['name_last']}
        raise ValueError("User with u_id is not a valid user")


def user_profile_setname(token, name_first, name_last):
    if (len(name_first) > 50 or len(name_last) > 50):
         raise ValueError("Name too long!")

    users = get_data()['user']
    user = get_user(get_user_from_token(token))
    if user != None:
        user['name_first'] = name_first
        user['name_last'] = name_last
        return {}


def user_profile_setemail(token, email):
    if (email == "notvalidemail.com"):
        raise ValueError("Invalid email address!")

    users = get_data()['user']
    user = get_user(get_user_from_token(token))
    if user != None:
        for u in users:
            if u['email'] == email:
                raise ValueError('Email address is already being used by another user')

        user['email'] = email
        return {}

def user_profile_sethandle(token, handle_str):
    if len(handle_str) > 20:
        raise ValueError("Handle too long!")
    return

def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    response = requests.get(img_url)
    urllib.urlretrieve(img_url, "tmp/new_photo.jpg")
    download = Image.open("tmp/new_photo.jpg")
    width, height = download.size

    if response.status_code != 200:
        raise ValueError("HTTP response unsuccessful!")
    elif x_start == x_end or y_start == y_end:
        raise ValueError("Invalid crop size!")
    elif x_start >= width or x_start < 0 or x_end >= width or x_end < 0:
        raise ValueError("Invalid width crop!")
    elif y_start >= height or y_start < 0 or y_end >= height or y_end < 0:
        raise ValueError("Invalid height crop!")
    return

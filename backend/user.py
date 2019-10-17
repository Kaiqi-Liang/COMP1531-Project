# pip3 INSTALLS
import pytest
from PIL import Image # pip3 name is "Pillow"

# STANDARD LIBRARY IMPORTS
import requests
import urllib

# LOCAL IMPORTS
from server.helpers import * # helpers/*.py

def user_profile(token, u_id):
    if u_id == None:
        raise ValueError("u_id not found!")
    return {"someemail@gmail.com","securepassword","John","Doe","johndoe"}

def user_profile_setname(token, name_first, name_last):
    if (len(name_first) > 50 or len(name_last) > 50):
        raise ValueError("Name too long!")
    return

def user_profile_setemail(token, email):
    if (email == "notvalidemail.com"):
        raise ValueError("Invalid email address!")
    elif (email == "someemail2@gmail.com"):
        raise ValueError("Email in use!")
    return

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

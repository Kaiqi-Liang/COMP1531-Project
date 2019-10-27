''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

''' pip3 packages '''
import pytest
import requests
import urllib
from PIL import Image

''' Local packages'''
from backend.user import *
from backend.database import get_user
from backend.helpers.token import get_user_from_token
from backend.helpers import *

def test_user_profile1():
    clear()
    u_id, token = auth_register("someemail@gmail.com","securepassword","John","Doe")
    user_profile_sethandle(token,"johndoe")

    assert user_profile(token, u_id)=={"someemail@gmail.com","John","Doe","johndoe"}

def test_user_profile2():
    clear()
    u_id, token = auth_register("someemail@gmail.com","securepassword","John","Doe")
    user_profile_sethandle(token,"johndoe")

    # Set arbitrary id thats invalid ...
    invalid_u_id = 2
    with pytest.raises(ValueError, match=r"*"):
        user_profile(token, invalid_u_id)

def test_user_profile_setname1():
    clear()
    u_id, token = auth_register("someemail1@gmail.com","securepassword","John","Doe")

    user_profile_setname(token, "Johnnette", "Doette")
    user = get_user(get_user_from_token(u_id))

    assert user['name_first'] == "Doette" and user['name_last'] == "Doette"

def test_user_profile_setname2():
    clear()
    u_id, token = auth_register("someemail3@gmail.com","securepassword","Juan","Doe")

    with pytest.raises(ValueError, match=r"*"):
        # Second name exceeding 50 chars ...
        user_profile_setname(token, "Juan", "hugesecondtnamethatiscertainlylongerthanfiftycharacters")

def test_user_profile_setname3():
    clear()
    u_id, token = auth_register("someemail2@gmail.com","securepassword","John","Smith")

    with pytest.raises(ValueError, match=r"*"):
        # First name exceeding 50 chars ...
        user_profile_setname(token, "hugefirstnamethatiscertainlylongerthanfiftycharacters", "Smith")

def test_user_profile_setname4():
    u_id, token = auth_register("someemail4@gmail.com","securepassword","Juan","Smith")

    with pytest.raises(ValueError, match=r"*"):
        # Both names exceeding 50 chars ...
        user_profile_setname(token, "hugefirstnamethatiscertainlylongerthanfiftycharacters", "hugesecondtnamethatiscertainlylongerthanfiftycharacters")

def test_user_profile_setemail():
    u_id1, token1 = auth_register("someemail1@gmail.com","securepassword","John","Doe")
    u_id2, token2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

    # Valid case ...
    user_profile_setemail(token1, "someemail3@gmail.com")

    with pytest.raises(ValueError, match=r"*"):
        # This should be invalid because u_id2 is using the same email ...
        user_profile_setemail(token1, "someemail2@gmail.com")

        # This should be invalid because the email address is bonkers ...
        user_profile_setemail(token1, "notvalidemail.com")

def test_user_profile_sethandle():
    u_id1, token1 = auth_register("someemail1@gmail.com","securepassword","John","Doe")

    # Valid case ...
    user_profile_sethandle(token1, "johndoe")

    # Invalid case ...
    # Assume handles can be a max 20 characters and not minimum ...
    with pytest.raises(ValueError, match=r"*"):
        # This shouldn't work because the handle is too long ...
        user_profile_sethandle(token1, "johndoe12345678910111213")

def test_user_profile_uploadphoto():
    u_id1, token1 = auth_register("someemail1@gmail.com","securepassword","John","Doe")

    img_url = "https://yt3.ggpht.com/a/AGF-l7_fK0Hy4B4JO8ST-uGqSU69OTLHduk4Kri_fQ=s900-c-k-c0xffffffff-no-rj-mo"
    invalid_url = "https://google.com/404"

   # Valid case ...
   # Assume error is thrown when given x,y coords OUTSIDE the boundary of the img and not inside
    user_profiles_uploadphoto(token1, img_url, 0, 0, 800, 800)

    # Invalid cases ...
    with pytest.raises(ValueError, match=r"*"):
        # This call is done with an invalid url that will return a status code NOT 200
        user_profiles_uploadphoto(token1, invalid_url, 0, 0, 800, 800)


        # Theses calls are done with crop x,y coords outside the img boundary ...
        # Assume you can crop any X x Y image to x,y->x+1,y+1 and 0,0->X,Y ...
        user_profiles_uploadphoto(token1, img_url, -1, 0, 800, 800)
        user_profiles_uploadphoto(token1, img_url, 0, -1, 800, 800)
        user_profiles_uploadphoto(token1, img_url, 0, 0, 1000, 800)
        user_profiles_uploadphoto(token1, img_url, 0, 0, 800, 1000)

        # Valid crop but invalid url ...
        user_profiles_uploadphoto(token1, invalid_url, 0, 0, 800, 800)

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
from backend.auth import *
from backend.user import *
from backend.database import *
from backend.helpers.token import get_user_from_token
from backend.helpers.helpers import *
from backend.helpers.exception import ValueError, AccessError

def test_user_profile1():
	clear()
	ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
	user_profile(ret['token'],ret['u_id'])

	assert user_profile(ret['token'], ret['u_id'])=={'email':"someemail@gmail.com",'name_first':"John",'name_last':"Doe",'handle_str':"johndoe"}

def test_user_profile2():
	clear()
	ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
	user_profile(ret['token'],ret['u_id'])

	# Set arbitrary id thats invalid ...
	invalid_u_id = 2
	with pytest.raises(ValueError, match=r"*"):
		user_profile(ret['token'], invalid_u_id)

def test_user_profile_setname1():
	clear()
	ret = auth_register("someemail1@gmail.com","securepassword","John","Doe")

	user_profile_setname(ret['token'], "Johnnette", "Doette")
	user = get_user(get_user_from_token(ret['token']))

	assert user['name_first'] == "Johnnette" and user['name_last'] == "Doette"

def test_user_profile_setname2():
	clear()
	ret = auth_register("someemail3@gmail.com","securepassword","Juan","Doe")

	with pytest.raises(ValueError, match=r"*"):
		# Second name exceeding 50 chars ...
		user_profile_setname(ret['token'], "Juan", "hugesecondtnamethatiscertainlylongerthanfiftycharacters")

def test_user_profile_setname3():
	clear()
	ret = auth_register("someemail2@gmail.com","securepassword","John","Smith")

	with pytest.raises(ValueError, match=r"*"):
		# First name exceeding 50 chars ...
		user_profile_setname(ret['token'], "hugefirstnamethatiscertainlylongerthanfiftycharacters", "Smith")

def test_user_profile_setname4():
	clear()
	ret = auth_register("someemail4@gmail.com","securepassword","Juan","Smith")

	with pytest.raises(ValueError, match=r"*"):
		# Both names exceeding 50 chars ...
		user_profile_setname(ret['token'], "hugefirstnamethatiscertainlylongerthanfiftycharacters", "hugesecondtnamethatiscertainlylongerthanfiftycharacters")

def test_user_profile_setemail1():
	clear()
	ret = auth_register("someemail1@gmail.com","securepassword","John","Doe")

	# Valid case ...
	user_profile_setemail(ret['token'], "someemail3@gmail.com")
	user = get_user(get_user_from_token(ret['token']))
	assert user['email'] == "someemail3@gmail.com"

def test_user_profile_setemail2():
	clear()
	ret = auth_register("someemail1@gmail.com","securepassword","John","Doe")
	temp = auth_register("someemail2@gmail.com","securepassword","John","Doe")

	with pytest.raises(ValueError, match=r"*"):
		# This should be invalid because u_id2 is using the same email ...
		user_profile_setemail(ret['token'], "someemail2@gmail.com")


def test_user_profile_setemail3():
	clear()
	ret = auth_register("someemail1@gmail.com","securepassword","John","Doe")

	with pytest.raises(ValueError, match=r"*"):

		# This should be invalid because the email address is bonkers ...
		user_profile_setemail(ret['token'], "notvalidemail.com")

def test_user_profile_sethandle1():
	clear()
	ret = auth_register("someemail1@gmail.com","securepassword","John","Doe")

	# Valid case ...
	user_profile_sethandle(ret['token'], "johndoe1")
	user = get_user(get_user_from_token(ret['token']))

	assert user['handle_str'] == "johndoe1"


def test_user_profile_sethandle2():
	clear()
	ret = auth_register("someemail1@gmail.com","securepassword","John","Doe")

	# Invalid case ...
	# Assume handles can be a max 20 characters and not minimum ...
	with pytest.raises(ValueError, match=r"*"):
		# This shouldn't work because the handle is too long ...
		user_profile_sethandle(ret['token'], "johndoe12345678910111213")

def test_user_profile_sethandle3():
	clear()
	ret = auth_register("someemail1@gmail.com","securepassword","John","Doe")

	# Test that the same handle cannot be used again
	user_profile_sethandle(ret['token'], "johndoe")
	user = get_user(get_user_from_token(ret['token']))

	assert user['handle_str'] != "johndoe1"

# def test_user_profile_uploadphoto():
#     u_id1, token1 = auth_register("someemail1@gmail.com","securepassword","John","Doe")

#     img_url = "https://yt3.ggpht.com/a/AGF-l7_fK0Hy4B4JO8ST-uGqSU69OTLHduk4Kri_fQ=s900-c-k-c0xffffffff-no-rj-mo"
#     invalid_url = "https://google.com/404"

#    # Valid case ...
#    # Assume error is thrown when given x,y coords OUTSIDE the boundary of the img and not inside
#     user_profiles_uploadphoto(token1, img_url, 0, 0, 800, 800)

#     # Invalid cases ...
#     with pytest.raises(ValueError, match=r"*"):
#         # This call is done with an invalid url that will return a status code NOT 200
#         user_profiles_uploadphoto(token1, invalid_url, 0, 0, 800, 800)


#         # Theses calls are done with crop x,y coords outside the img boundary ...
#         # Assume you can crop any X x Y image to x,y->x+1,y+1 and 0,0->X,Y ...
#         user_profiles_uploadphoto(token1, img_url, -1, 0, 800, 800)
#         user_profiles_uploadphoto(token1, img_url, 0, -1, 800, 800)
#         user_profiles_uploadphoto(token1, img_url, 0, 0, 1000, 800)
#         user_profiles_uploadphoto(token1, img_url, 0, 0, 800, 1000)

#         # Valid crop but invalid url ...
#         user_profiles_uploadphoto(token1, invalid_url, 0, 0, 800, 800)

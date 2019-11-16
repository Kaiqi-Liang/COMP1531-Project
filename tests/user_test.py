''' pip3 packages '''
import pytest
import requests
import urllib
from PIL import Image

''' Local packages'''
from backend.user import users_all, user_profile, user_profile_setname, user_profile_setemail, user_profile_sethandle, user_profiles_uploadphoto
from backend.auth import auth_register
from backend.database import clear, get_user
from backend.channel import channels_create, channel_details
from backend.helpers.exception import ValueError, AccessError
from backend.helpers.token import generate_token

@pytest.fixture
def register_owner():
    # return { u_id, token }
    return auth_register('z5210932@unsw.edu.au', '123456', 'Sarah', 'Williams')

@pytest.fixture
def channel_create(owner_token):
    # return channel_id
    return channels_create(owner_token, 'name', 'true')['channel_id']

@pytest.fixture
def register_user():
    # return { u_id, token }
    return auth_register('kaiqi.liang9989@gmail.com', '123456', 'kaiqi', 'liang')

def test_user_all():
    clear()
    user = auth_register("someemail1@gmail.com","securepassword","John","Doe")
    result = users_all(user['token'])
    assert result['users'] == [{'u_id': 1, 'email': 'someemail1@gmail.com', 'name_first': 'John', 'name_last': 'Doe', 'handle_str': 'johndoe', 'profile_img_url': None}]

def test_user_profile1():
	clear()
	ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
	user_profile(ret['token'],ret['u_id'])

	assert user_profile(ret['token'], ret['u_id'])== {'email':"someemail@gmail.com",'name_first':"John",'name_last':"Doe",'handle_str':"johndoe", 'profile_img_url': None, 'u_id' : ret['u_id']}

def test_user_profile2():
	clear()
	ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
	user_profile(ret['token'],ret['u_id'])

	# Set arbitrary id thats invalid ...
	invalid_u_id = 2
	with pytest.raises(ValueError, match=r"*"):
		user_profile(ret['token'], invalid_u_id)

# user with token doesn't exist
def test_user_profile3():
    clear()
    owner_dict = register_owner()
    assert user_profile(generate_token(100), owner_dict['u_id']) == {}

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

# check that the name has changed in the channel members and owners lists 
def test_user_profile_setname5():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_profile_setname(owner_token, "sarah", "williams")
    
    assert channel_details(owner_token, channel_id) == {'name': 'name', 'owner_members': [{'u_id': owner_user, 'name_first': 'sarah', 'name_last': 'williams', 'profile_img_url': None}], 'all_members' : [{'u_id': owner_user, 'name_first': 'sarah', 'name_last': 'williams', 'profile_img_url': None}]}

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
	with pytest.raises(ValueError):
		# This shouldn't work because the handle is too long ...
		user_profile_sethandle(ret['token'], "johndoe12345678910111213")

def test_user_profile_sethandle3():
	# Test that the same handle cannot be used again
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    user_dict = register_user()
    
    user_profile_sethandle(owner_token, "BestCoder")
    with pytest.raises(ValueError):
        user_profile_sethandle(user_dict['token'], "BestCoder")

def test_user_profile_uploadphoto():
    clear()
    user = auth_register("someemail1@gmail.com","securepassword","John","Doe")

    img_url = "https://yt3.ggpht.com/a/AGF-l7_fK0Hy4B4JO8ST-uGqSU69OTLHduk4Kri_fQ=s900-c-k-c0xffffffff-no-rj-mo"
    invalid_url = "https://google.com/404"
    base_url = "localhost:5000"
    png_url = "https://www.fnordware.com/superpng/pnggrad16rgb.png"

   # Valid case ...
   # Assume error is thrown when given x,y coords OUTSIDE the boundary of the img and not inside
    user_profiles_uploadphoto(user['token'], img_url, 0, 0, 800, 800, base_url)

    # Invalid cases ...
    with pytest.raises(ValueError, match=r"*"):
        # This call is done with an invalid url that will return a status code NOT 200
        user_profiles_uploadphoto(user['token'], invalid_url, 0, 0, 800, 800, base_url)
        user_profiles_uploadphoto(user['token'], png_url, 0, 0, 800, 800, base_url)

        # Theses calls are done with crop x,y coords outside the img boundary ...
        # Assume you can crop any X x Y image to x,y->x+1,y+1 and 0,0->X,Y ...
        user_profiles_uploadphoto(user['token'], img_url, -1, 0, 800, 800, base_url)
        user_profiles_uploadphoto(user['token'], img_url, 0, -1, 800, 800, base_url)
        user_profiles_uploadphoto(user['token'], img_url, 0, 0, 1000, 800, base_url)
        user_profiles_uploadphoto(user['token'], img_url, 0, 0, 800, 1000, base_url)

        # Valid crop but invalid url ...
        user_profiles_uploadphoto(user['token'], invalid_url, 0, 0, 800, 800, base_url)

# user w token doesn't exist
def test_user_profile_uploadphoto2():
    clear()
    img_url = "https://yt3.ggpht.com/a/AGF-l7_fK0Hy4B4JO8ST-uGqSU69OTLHduk4Kri_fQ=s900-c-k-c0xffffffff-no-rj-mo"
    invalid_url = "https://google.com/404"
    base_url = "localhost:5000"
    png_url = "https://www.fnordware.com/superpng/pnggrad16rgb.png"
    assert user_profiles_uploadphoto(generate_token(100), img_url, 0, 0, 800, 800, base_url) == {}
          


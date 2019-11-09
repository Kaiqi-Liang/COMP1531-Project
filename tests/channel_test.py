''' pip3 packages '''
import pytest

''' Local packages '''
from backend.channel import *
from backend.auth import auth_register
from backend.database import clear
from backend.helpers.exception import AccessError, ValueError

@pytest.fixture
def register_owner():
    # return { u_id, token }
    owner_dict = auth_register('z5210932@unsw.edu.au', '123456', 'Kaiqi', 'Liang')
    return owner_dict
    
@pytest.fixture
def register_user():
    # return { u_id, token }
    return auth_register('kaiqi.liang9989@gmail.com', '123456', 'kaiqi', 'liang')

@pytest.fixture
def channel_create(owner_token):
    # return channel_id
    return channels_create(owner_token, 'name', True)['channel_id']

# working
# TESTING FOR CHANNEL_INVITE
# normal functioning
def test_invite():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()

    channel_invite(owner_token, channel_id, user_dict['u_id'])
    assert channel_details(user_dict['token'], channel_id) == {'name': 'name', 'owner_members': [{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}], 'all_members' : [{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': user_dict['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}]}
    
# not a valid channel
def test_invite1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    
    with pytest.raises(ValueError):
        # invalid channel id
        channel_invite(owner_token, -1, user_dict['u_id'])

#u_id does not refer to a valid user 
# currently not working as the code is not set up properly 
def test_invite2():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    with pytest.raises(ValueError):
        # invalid user id
        channel_invite(owner_token, channel_id, 123)

# access error: authorised user is not already a member of the channel
def test_invite3():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    with pytest.raises(AccessError):
        channel_invite(user_dict['token'], channel_id, user_dict['u_id'])
    
def test_details():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    # check if the owner is in the channel after the channel is first created
    assert channel_details(owner_token, channel_id) == {'name':'name', 'owner_members': [{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}], 'all_members': [{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}]}

    with pytest.raises(ValueError):
        # channel does not exist
        channel_details(owner_token, -1)

'''
# not working        
def test_details1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    with pytest.raises(AccessError, match=r"*"):
        # user is not a member of channel
        channel_details(user_dict['token'], channel_id)
'''

def test_message():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    # no messages in the channel at the moment
    assert channel_messages(owner_token, channel_id, 0) == {'messages': [], 'start': 0, 'end': -1}
    with pytest.raises(ValueError):
        # channel does not exist
        channel_messages(owner_token, -1, 0)
        # start is greater than the total number of messages
        channel_messages(owner_token, channel_id, 1)

'''
# not working
def test_message1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    with pytest.raises(AccessError):
        # user is not a member of channel
        channel_messages(user_dict['token'], channel_id, 0)
'''

def test_leave():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    with pytest.raises(ValueError):
        # channel does not exist
        channel_leave(owner_token, -1)

    # owner leaves the channel
    channel_leave(owner_token, channel_id)

    with pytest.raises(ValueError):
        # channel does not exist anymore after the owner leaves the channel
        channel_leave(owner_token, channel_id)


def test_join():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    # user joins a public channel created by the owner
    channel_join(user_dict['token'], channel_id)
    assert channel_details(user_dict['token'], channel_id) == {'name': 'name', 'owner_members': [{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}], 'all_members':[{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': user_dict['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}]}

    with pytest.raises(ValueError):
        # channel does not exist
        channel_join(owner_token, -1)

'''
# not working
def test_join1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    # owner creates a private channel for user to join
    channel_id = channels_create(owner_token, 'private', False)['channel_id']
    with pytest.raises(AccessError):
        channel_join(user_dict['token'], channel_id)
'''


def test_addowner():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    # make user the owner of the channel
    channel_invite(owner_token, channel_id, user_dict['u_id'])
    channel_addowner(owner_token, channel_id, user_dict['u_id'])  
    assert channel_details(user_dict['token'], channel_id) == {'name': 'name', 'owner_members': [{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': user_dict['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}], 'all_members':[{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': user_dict['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}]}

    with pytest.raises(ValueError):
        # channel does not exist
        channel_addowner(owner_token, -1, user_dict['u_id'])
        # user is already an owner
        channel_addowner(rowner_token, channel_id, user_dict['u_id'])

'''
# not working      
def test_addowner1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    channel_invite(owner_token, channel_id, user_dict['u_id'])
    channel_addowner(owner_token, channel_id, user_dict['u_id']) 
    # remove user as an owner
    channel_removeowner(owner_token, -1, user_dict['u_id'])
    with pytest.raises(AccessError):
        # user has no permission to add owner
        channel_addowner(user_dict['token'], channel_id, owner_user)
'''

def test_removeowner():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    # make user the owner of the channel then remove it
    channel_invite(owner_token, channel_id, user_dict['u_id'])
    channel_addowner(owner_token, channel_id, user_dict['u_id'])
    channel_removeowner(owner_token, channel_id, user_dict['u_id'])
    assert channel_details(user_dict['token'], channel_id) == { 'name':'name','owner_members': [{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}], 'all_members' : [{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': user_dict['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}] }

    with pytest.raises(ValueError):
        # channel does not exist
        channel_removeowner(owner_token, -1, user_dict['u_id'])
        # user is not an owner
        channel_removeowner(user_dict['token'], channel_id, owner_user)
'''        
# not working    
def test_removeowner1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    channel_removeowner(owner_token, -1, user_dict['u_id'])
    with pytest.raises(AccessError):
        # not an owner
        channel_removeowner(user_dict['token'], channel_id, owner_user)
'''

def test_list():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
   # channel_id = channel_create(owner_token)
    user_dict = register_user()
    # user is not part of any channels
    assert channels_list(owner_user) == []
    # owner can see the channel created
    assert channels_list(owner_token) == [{'id': channel_id, 'name': 'name'}]

    # user creates a private channel
    channel_id = channels_create(user_dict['token'], 'private', False)['channel_id']
    # user can see this private channel
    assert channels_list(user_dict['token']) == [{'id': channel_id, 'name': 'private'}]

    # owner leaves the channel
    channel_leave(owner_token, channel_id)
    # owner can not see any channels
    assert channels_listall(owner_token) == []


def test_listall():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    #channel_id = channel_create(owner_token)
    user_dict = register_user()
    # there is no channels at this point
    assert channels_listall(user_dict['token']) == []
    assert channels_listall(owner_token) == []

    # owner creates a public channel
    channel_id = channels_create(owner_token, 'public', True)['channel_id']
    # user can see this public channel
    assert channels_listall(user_dict['token']) == [{'id': channel_id, 'name': 'public'}]

    # owner creates a private channel
    channel_id = channels_create(owner_token, 'private', False)['channel_id']
    # owner can see this private channel
    assert channels_listall(owner_token) == [{'id': channel_id, 'name': 'private'}]
    # user can not see the private channel
    assert channels_listall(user_dict['token']) == []


def test_create():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    # owner creates a channel
    channel_id = channels_create(owner_token, 'name', True)['channel_id']
    # a chanel has been created
    assert channels_list(owner_token) == [{'id': channel_id, 'name': 'name'}]

    with pytest.raises(ValueError):
        # name is more than 20 characters long
        channels_create('token','012345678901234567890',True)

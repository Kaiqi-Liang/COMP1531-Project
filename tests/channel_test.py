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

def test_invite():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    channel_id = channel_create(owner_token)
    user_dict = register_user()
    
    with pytest.raises(ValueError):
        # invalid channel id
        channel_invite(owner_token, -1, user_dict['u_id'])
        # invalid user id
        channel_invite(owner_token, channel_id, 'user_id')

    # invite user to the channel
    channel_invite(owner_token, channel_id, user_dict['u_id'])
    assert channel_details(user_dict['token'], channel_id) == {'name': 'name', 'owner_members': [{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}], 'all_members' : [{'u_id': owner_user, 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': user_dict['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}]}

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

def test_listall():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    #channel_id = channel_create(owner_token)
    user_dict = register_user()
    # there is no channels at this point
    assert channels_listall(user_dict['token']) == {'channels': []}
    assert channels_listall(owner_token) == {'channels': []}

    # owner creates a public channel
    channel_id = channels_create(owner_token, 'public', True)['channel_id']
    # user can see this public channel
    assert channels_listall(user_dict['token']) == {'channels': [{'channel_id': channel_id, 'name': 'public'}]}

    # owner creates a private channel
    channel_id = channels_create(owner_token, 'private', False)['channel_id']
    # owner can see this private channel
    assert channels_listall(owner_token) == {'channels': [{'channel_id': 1, 'name': 'public'}]}
    # user can not see the private channel
    assert channels_listall(user_dict['token']) =={'channels': [{'channel_id': 1, 'name': 'public'}]}


def test_create():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    owner_user = owner_dict['u_id']
    # owner creates a channel
    channel_id = channels_create(owner_token, 'name', True)['channel_id']
    # a chanel has been created
    assert channels_list(owner_token) =={'channels': [{'channel_id': channel_id, 'name': 'name'}]}

    with pytest.raises(ValueError):
        # name is more than 20 characters long
        channels_create('token','012345678901234567890',True)

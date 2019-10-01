import pytest
from channel import *
from access_error import AccessError

@pytest.fixture
def register():
    # return { u_id, token }
    return auth_register('z5210932@unsw.edu.au', '12345', 'Kaiqi', 'Liang')

@pytest.fixture
def channel_create(register):
    return channels_create(register['token'], 'name', True)['channel_id']

def test_invite(register):
    user_id =  auth_register('lkq137055338@gmail.com', '12345', 'kaiqi', 'liang')['u_id']
    channel_id = channels_create(register['token'], 'channel', True)['channel_id']
    # success
    channel_invite(register['token'], channel_id, u_id)
    with pytest.raises(ValueError):
        # invalid channel id
        channel_invite(register['token'], 'channel_id', user_id)
        # invalid user id
        channel_invite(register['token'], channel_id, 'user_id')

def test_details(channel_create):
    with pytest.raises(ValueError):
        # channel does not exist
        channel_detail('token', 'channel_id')
    with pytest.raises(AccessError):
        channel_detail('token', channel_create)

def test_create(register):
    channels_create(register, 'name', True)
    with pytest.raises(ValueError):
        # name is more than 20 characters long
        channels_create('token','012345678901234567890',True)

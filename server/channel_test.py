import pytest
from channel import *
from access_error import AccessError

@pytest.fixture
def register_owner():
    # return { u_id, token }
    return auth_register('z5210932@unsw.edu.au', '12345', 'Kaiqi', 'Liang')

@pytest.fixture
def register_user():
    # return { u_id, token }
    return auth_register('lkq137055338@gmail.com', '12345', 'kaiqi', 'liang')

@pytest.fixture
def channel_create(register_owner):
    # return channel_id
    return channels_create(register, 'name', True)['channel_id']


def test_invite(register_owner, channel_create, register_user):
    # success
    channel_invite(register_owner['token'], channel_create, register_user['u_id'])

    with pytest.raises(ValueError):
        # invalid channel id
        channel_invite(register_owner['token'], 'channel_id', register_user['u_id'])
        # invalid user id
        channel_invite(register_owner['token'], channel_create, 'user_id')


def test_details(register_owner, channel_create, register_user):
    # success
    assert channel_detail(register_owner['token'], channel_create) == { 'name', [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}], [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}] }

    with pytest.raises(ValueError):
        # channel does not exist
        channel_detail(register_owner['token'], 'channel_id')
    with pytest.raises(AccessError):
        # user is not a member of channel
        channel_detail(register_user['token'], channel_create)

    # user has been invited to the channel
    channel_invite(register_owner['token'], channel_create, register_user['u_id'])
    assert channel_detail(register_user['token'], channel_create) == { 'name', [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}], [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': register_user['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}] }


def test_message(register_owner, channel_create):
    channel_message(register_owner['token'], channel_create, 0)


def test_create(register):
    channels_create(register, 'name', True)
    with pytest.raises(ValueError):
        # name is more than 20 characters long
        channels_create('token','012345678901234567890',True)

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
    return channels_create(register_owner['token'], 'name', True)['channel_id']


def test_invite(register_owner, channel_create, register_user):
    with pytest.raises(ValueError):
        # invalid channel id
        channel_invite(register_owner['token'], -1, register_user['u_id'])
        # invalid user id
        channel_invite(register_owner['token'], channel_create, 'user_id')

    # invite user to the channel
    channel_invite(register_owner['token'], channel_create, register_user['u_id'])
    assert channel_detail(register_user['token'], channel_create) == { 'name', [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}], [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': register_user['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}] }


def test_details(register_owner, channel_create, register_user):
    # check if the owner is in the channel after the channel is first created
    assert channel_detail(register_owner['token'], channel_create) == { 'name', [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}], [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}] }

    with pytest.raises(ValueError):
        # channel does not exist
        channel_detail(register_owner['token'], -1)

    with pytest.raises(AccessError):
        # user is not a member of channel
        channel_detail(register_user['token'], channel_create)


def test_message(register_owner, channel_create, register_user):
    # no messages in the channel at the moment 
    assert channel_message(register_owner['token'], channel_create, 0) == { 'messages': [], 'start': 0, 'end': 0 }
    with pytest.raises(ValueError):
        # channel does not exist
        channel_message(register_owner['token'], -1, 0)
        # start is greater than the total number of messages
        channel_message(register_owner['token'], channel_create, 1)

    with pytest.raises(AccessError):
        # user is not a member of channel
        channel_message(register_user['token'], channel_create, 0)


def test_leave(register_owner, channel_create):
    with pytest.raises(ValueError):
        # channel does not exist
        channel_leave(register_owner['token'], -1)

    # owner leaves the channel
    channel_leave(register_owner['token'], channel_create)

    with pytest.raises(ValueError):
        # channel does not exist anymore after the owner leaves the channel
        channel_leave(register_owner['token'], channel_create)


def test_join(register_owner, channel_create, register_user):
    # user joins a public channel created by the owner
    channel_join(register_user['token'], channel_create)
    assert channel_detail(register_user['token'], channel_create) == { 'name', [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}], [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': register_user['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}] }

    with pytest.raises(ValueError):
        # channel does not exist
        channel_join(register_owner['token'], -1)

    # owner creates a private channel for user to join
    channel_id = channels_create(register_owner['token'], 'private', False)['channel_id']
    with pytest.raises(AccessError):
        channel_join(register_user['token'], channel_id)


def test_addowner(register_owner, channel_create, register_user):
    # make user the owner of the channel
    channel_invite(register_owner['token'], channel_create, register_user['u_id'])
    channel_addowner(register_owner['token'], channel_create, register_user['u_id'])
    assert channel_detail(register_user['token'], channel_create) == { 'name', [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': register_user['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}], [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': register_user['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}] }

    with pytest.raises(ValueError):
        # channel does not exist
        channel_addowner(register_owner['token'], -1, register_user['u_id'])
        # user is already an owner
        channel_addowner(register_owner['token'], channel_create, register_user['u_id'])

    channel_removeowner(register_owner['token'], -1, register_user['u_id'])
    with pytest.raises(AccessError):
        # not an owner
        channel_addowner(register_user['token'], channel_create, register_owner['u_id'])


def test_removeowner(register_owner, channel_create, register_user):
    # make user the owner of the channel then remove it
    channel_invite(register_owner['token'], channel_create, register_user['u_id'])
    channel_addowner(register_owner['token'], channel_create, register_user['u_id'])
    channel_removeowner(register_owner['token'], channel_create, register_user['u_id'])
    assert channel_detail(register_user['token'], channel_create) == { 'name', [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}], [{'u_id': register_own['u_id'], 'name_first': 'Kaiqi', 'name_last': 'Liang'}, {'u_id': register_user['u_id'], 'name_first': 'kaiqi', 'name_last': 'liang'}] }

    with pytest.raises(ValueError):
        # channel does not exist
        channel_removeowner(register_owner['token'], -1, register_user['u_id'])
        # user is not an owner
        channel_removeowner(register_user['token'], channel_create, register_owner['u_id'])

    channel_removeowner(register_owner['token'], -1, register_user['u_id'])
    with pytest.raises(AccessError):
        # not an owner
        channel_removeowner(register_user['token'], channel_create, register_owner['u_id'])


def test_list(register_owner, channel_create, register_user):
    # user is not part of any channels
    assert channels_list(register_user['token']) == []
    # owner can see the channel created
    assert channels_list(register_owner['token']) == [{'id': channel_create, 'name': 'name'}]

    # user creates a private channel
    channel_id = channels_create(register_user['token'], 'private', False)['channel_id']
    # user can see this private channel
    assert channels_list(register_user['token']) == [{'id': channel_id, 'name': 'private'}]

    # owner leaves the channel
    channel_leave(register_owner['token'], channel_create)
    # owner can not see any channels
    assert channels_listall(register_owner['token']) == []


def test_listall(register_owner, register_user):
    # there is no channels at this point
    assert channels_listall(register_user['token']) == []
    assert channels_listall(register_onwer['token']) == []

    # owner creates a public channel
    channel_id = channels_create(register_owner['token'], 'public', True)['channel_id']
    # user can see this public channel
    assert channels_listall(register_user['token']) == [{'id': channel_id, 'name': 'public'}]

    # owner creates a private channel
    channel_id = channels_create(register_owner['token'], 'private', False)['channel_id']
    # owner can see this private channel
    assert channels_listall(register_owner['token']) == [{'id': channel_id, 'name': 'private'}]
    # user can not see the private channel
    assert channels_listall(register_user['token']) == []


def test_create(register_owner):
    # owner creates a channel
    channel_id = channels_create(register_owner['token'], 'name', True)
    # a chanel has been created
    assert channels_list(register_owner['token']) == [{'id': channel_create, 'name': 'name'}]

    with pytest.raises(ValueError):
        # name is more than 20 characters long
        channels_create('token','012345678901234567890',True)

''' pip3 packages '''
import pytest

''' Local packages '''
from backend.search import search
from backend.auth import auth_register, auth_login
from backend.channel import channels_create, channel_leave
from backend.message import message_send
from backend.database import clear

@pytest.fixture
def register_owner():
    # return { u_id, token }
    return auth_register('z5210932@unsw.edu.au', '123456', 'Kaiqi', 'Liang')
    
@pytest.fixture
def register_user():
    # return { u_id, token }
    return auth_register('kaiqi.liang9989@gmail.com', '123456', 'kaiqi', 'liang')

@pytest.fixture
def channel_create(owner_token):
    # return channel_id
    return channels_create(owner_token, 'name', True)['channel_id']

@pytest.fixture
def private_create(owner_token):
    # return channel_id
    return channels_create(owner_token, 'private', False)['channel_id']

def test_success():
    clear()
    user = register_user()
    token = user['token']
    channel_id = channel_create(token)
    message_id = message_send(token, channel_id, 'hi')

    result = search(token, 'hi')['messages'][0]
    assert result['message_id'] == 0
    assert result['u_id'] == 1
    assert result['message'] == 'hi'
    assert result['reacts'] == [{'react_id': 1, 'u_ids': [], 'is_this_user_reacted': False}]
    assert result['is_pinned'] == False

def test_substring():
    clear()
    user = register_user()
    token = user['token']
    channel_id = channel_create(token)
    message_id = message_send(token, channel_id, 'hi')

    result = search(token, 'i')['messages'][0]
    assert result['message_id'] == 0
    assert result['u_id'] == 1
    assert result['message'] == 'hi'
    assert result['reacts'] == [{'react_id': 1, 'u_ids': [], 'is_this_user_reacted': False}]
    assert result['is_pinned'] == False

def test_fail():
    clear()
    user = register_user()
    token = user['token']
    channel_id = channel_create(token)
    message_id = message_send(token, channel_id, 'hi')

    assert search(token, 'hello') == {'messages': []}

def test_not_in_channel():
    clear()
    user = register_user()
    token = user['token']
    channel_id1 = channel_create(token)
    channel_id2 = private_create(token)
    message_id1 = message_send(token, channel_id1, 'hi')
    message_id2 = message_send(token, channel_id2, 'hi')

    # leave channel1 after sending a message
    channel_leave(token, channel_id1)
    result = search(token, 'hi')['messages'][0]

    assert result['message_id'] == 1
    assert result['u_id'] == 1
    assert result['message'] == 'hi'
    assert result['reacts'] == [{'react_id': 1, 'u_ids': [], 'is_this_user_reacted': False}]
    assert result['is_pinned'] == False

def test_private():
    clear()
    user1 = register_owner()
    token1 = user1['token']
    user2 = register_user()
    token2 = user2['token']
    channel_id1 = channel_create(token1)
    channel_id2 = private_create(token1)
    message_id1 = message_send(token1, channel_id1, 'hi')
    message_id2 = message_send(token1, channel_id2, 'hello')

    assert search(token2, 'h')['messages'] == []

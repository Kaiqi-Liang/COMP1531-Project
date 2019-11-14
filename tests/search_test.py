''' pip3 packages '''
import pytest

''' Local packages '''
from backend.search import search
from backend.auth import auth_register, auth_login
from backend.channel import channels_create
from backend.message import message_send
from backend.database import clear

@pytest.fixture
def register_user():
    # return { u_id, token }
    return auth_register('kaiqi.liang9989@gmail.com', '123456', 'kaiqi', 'liang')

@pytest.fixture
def channel_create(owner_token):
    # return channel_id
    return channels_create(owner_token, 'name', True)['channel_id']

def test_success():
    clear()
    user = register_user()
    token = user['token']
    channel_id = channel_create(token)
    message_id = message_send(token, channel_id, 'hi')

    result = search(token, 'hi')['messages'][0]
    assert result['message_id'] == message_id['message_id']
    assert result['u_id'] == user['u_id']
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
    assert result['message_id'] == message_id['message_id']
    assert result['u_id'] == user['u_id']
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

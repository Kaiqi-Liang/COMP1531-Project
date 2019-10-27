''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

''' pip3 packages '''
import pytest
import datetime

''' Local packages '''
from backend.message import *
from backend.auth import auth_register
from backend.auth import auth_login
from backend.channel import channel_join, channels_create, channel_invite
from backend.database import *
from backend.helpers import *
from backend.admin_userpermission_change import *

# FUNCTION SETUP

@pytest.fixture
def register_owner():
    owner_dict = auth_register("sarah@gmail.com", "123456", "Sarah", "Williams")
    # return { u_id, token }
    return owner_dict

@pytest.fixture
def register_user():
    return auth_register("emma@gmail.com", "123456", "Emma", "Mayall")
    # return { u_id, token }

@pytest.fixture
def register_not_in_channel():
    return auth_register("random@random.com", "123456", "first name", "last name")

@pytest.fixture
def create_channel(owner_token):
    #token = register_owner['token']
    # return channel_id
    return channels_create(owner_token, "Test channel", True)

@pytest.fixture
def join_user(register_owner, register_user, create_channel):
    token = register_user['token']
    channel_join(register_owner['token'], create_channel, register_user['u_id'])
    # nothing to return

@pytest.fixture
def message_valid():
    return "Hello World"

@pytest.fixture
def message_invalid():
    return "Cranial exterior: Frontal bone: forms the  forehead, roofs of the orbits. Parietal bones: paired, form the greater portion of the sides and roof of the cranial cavity. Temporal bones: paired, form the lateral aspects of the cranium. Occipital bones:  forms the posterior part and most of the base of the cranium. Sphenoid bone: middle part of the base of the skull. Key part of the cranial floor, holds bones together (butterfly shape). Ethmoid bone: anterior part of the cranial floor, supporting structure of the nasal cavity. Foramen magnum: large hole on the inferior part of the bone. Occipital condyles: oval processes on either side of the foramen magnum, allows you to nod. External acoustic meatus: ear canal which directs sound waves into the ear. Mastoid process: rounded projection of the mastoid portion of the temporal bone (behind the ear). Cranial interior:Anterior cranial fossa: depression in the floor of the cranial base, housing the frontal lobes. Middle cranial fossa: depression in the middle region of the cranial base, and is deeper and wider than the anterior cranial fossa"

@pytest.fixture
def time_valid():
    return datetime(2019, 12, 3, 5, 30, 30, 0)

@pytest.fixture
def time_invalid():
    return (2005, 5, 5, 20, 0, 0, 0)

@pytest.fixture
def valid_reactid():
    return 1

@pytest.fixture
def invalid_reactid():
    return 0


# FUNCTION TESTING

#TESTING FOR SEND LATER 
#normal functioning
def test_message_sendlater(register_owner, create_channel, message_valid, time_valid):  
    clear()
    m_id = message_sendlater(register_owner['token'], create_channel, message_valid, time_valid) 
    mess = get_message(m_id)
    assert mess['time_created'] == time_valid
# channel id not valid
def test_message_sendlater1(register_owner, create_channel, message_valid, time_valid):
    clear()
    with pytest.raises(ValueError, match=r"*"):
        message_sendlater(register_owner['token'], -1, message_valid, time_valid)
#message is invalid
def test_message_sendlater2(register_owner, create_channel, message_invalid, time_valid):
    clear()
    with pytest.raises(ValueError, match=r"*"):
        message_sendlater(register_owner['token'], create_channel, message_invalid, time_valid)
#time is invalid
def test_message_sendlater3(register_owner, create_channel, message_valid, time_invalid):
    clear()
    with pytest.raises(ValueError, match=r"*"):
        message_sendlater(register_owner['token'], create_channel, message_valid, time_invalid)
# authorised user is not apart of the channel
def test_message_sendlater4():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    user_dict = register_user()
    time = int(datetime.datetime(2019, 12, 3, 5, 30, 30, 0))
    with pytest.raises(AccessError, match=r"*"):
        message_sendlater(user_dict['token'], channel_id, "Hello World", time)

# TEST FOR MESSAGE_SEND
# normal functioning
def test_message_send():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_dict = create_channel(owner_token)
    channel_id = channel_dict['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Hello World")['message_id'] 
    assert get_message(m_id) != None
# invalid message
def test_message_send1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    message = message_invalid()
    with pytest.raises(ValueError, match=r"*"):
        message_send(owner_token, channel_id, message)
# authorised user is not apart of the channel
def test_message_send2():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    user_dict = register_user()
    with pytest.raises(AccessError, match=r"*"):
        message_send(user_dict['token'], channel_id, "Hello world")
       
# TESTS FOR MESSAGE_REMOVE
# functioning properly
def test_message_remove():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Hello World")['message_id']
    message_remove(owner_token, m_id)
    # assert based on the message_id not existing
    assert get_message(m_id) == None 
# message based on id no longer exists -> call remove twice
def test_message_remove1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Hello World")['message_id']
    message_remove(owner_token, m_id)
    with pytest.raises(ValueError,match=r"*"):
        message_remove(owner_token, m_id)
# message was not sent by authorised user and user is not admin 
def test_message_remove2():
    clear()
    owner_dict = register_owner()
    user_dict = register_user()
    owner_token = owner_dict['token']
    user_token = user_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    channel_join(user_token, channel_id)
    
    m_id = message_send(owner_token, channel_id, "Hello World")['message_id']
    with pytest.raises(AccessError, match=r"*"):
        message_remove(user_token, m_id)
       
# TESTS FOR MESSAGE_EDIT
# normal functioning
def test_message_edit():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Hello World")['message_id']
    message_edit(owner_token, m_id, "Edited message")
    mess = get_message(m_id)
    assert mess['message'] == "Edited message"
#access error 
def test_message_edit1():
    clear()
    owner_dict = register_owner()
    user_dict = register_user()
    owner_token = owner_dict['token']
    user_token = user_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    channel_join(user_token, channel_id)
    
    m_id = message_send(owner_token, channel_id, "Hello World")['message_id']
    with pytest.raises(AccessError, match=r"*"):
        message_edit(user_token, m_id, "Can not edit")   
        
# TESTS FOR MESSAGE_REACT
# normal functioning
def test_message_react():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Test react")['message_id']

    message_react(owner_token, m_id, 1)
    mess = get_message(m_id)
    for react in mess['reacts']:
        if valid_reactid == react['react_id']:
            if register_owner['u_id'] in react['u_ids']:
             assert True

# message_id is not a valid message
def test_message_react1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    with pytest.raises(ValueError, match=r"*"):
        message_react(owner_token, -100, 1)
        
# react_id is not valid
def test_message_react2():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Test react")['message_id']
    with pytest.raises(ValueError, match=r"*"):
        message_react(owner_token, m_id, 0)
    
# message already contains an active react
def test_message_react3():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Test react")['message_id']
    message_react(owner_token, m_id, 1)
    with pytest.raises(ValueError, match=r"*"):
        message_react(owner_token, m_id, 1)

# TESTS FOR MESSAGE_UNREACT
# normal functioning 
def test_message_unreact():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Test react")['message_id']
    message_react(owner_token, m_id, 1)
    message_unreact(owner_token, m_id, 1)
    mess = get_message(m_id)
    
    for react in mess['reacts']:
        if 1 == react['react_id']:
            for users in react['u_ids']:
                if owner_dict['u_id'] == users['u_id']:
                    assert True
# message_id is not a valid message
def test_message_unreact1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    with pytest.raises(ValueError, match=r"*"):
        message_unreact(owner_token, -100, 1)
# react_id is not valid
def test_message_unreact2():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Test unreact")['message_id']

    message_react(owner_token, m_id, 1)
    with pytest.raises(ValueError, match=r"*"):
        message_unreact(owner_token, m_id, 0)
# message does not contain an active react -> dont call react before i test unreact
def test_message_unreact3():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Test unreact")['message_id']
    with pytest.raises(ValueError, match=r"*"):
        message_unreact(owner_token, m_id, 1)

# TESTS FOR MESSAGE_PIN
# normal functioning
def test_message_pin():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Test pin")['message_id']
    message_pin(owner_token, m_id)
    mess = get_message(m_id)
    assert mess['is_pinned'] == True
# message id is not valid
def test_message_pin1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    with pytest.raises(ValueError, match=r"*"):
        message_pin(owner_token, -100)
# autorised user is not admin
def test_message_pin2():
    # SETUP
    clear()
    owner_dict = register_owner()
    user_dict = register_user()
    owner_token = owner_dict['token']
    user_token = user_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    channel_join(user_token, channel_id)
    
    m_id = message_send(owner_token, channel_id, "Test pin")['message_id']
    
    with pytest.raises(ValueError, match=r"*"):
        message_pin(user_token, m_id)
        
# message is already pinned -> run pin twice
def test_message_pin3():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    m_id = message_send(owner_token, channel_id, "Test pin")['message_id']
    message_pin(owner_token, m_id)
    with pytest.raises(ValueError, match=r"*"):
        message_pin(owner_token, m_id)   
# authorised user is not member of the channel
def test_message_pin4():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    not_register = register_not_in_channel()
    not_register_token = not_register['token']
    not_register_uid = not_register['u_id']

    m_id = message_send(owner_token, channel_id, "Test unpin")['message_id']
    with pytest.raises(AccessError, match=r"*"):
        message_pin(not_register_token, m_id)
    
# TEST FOR MESSAGE_UNPIN
# normal functioning
def test_message_unpin():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
   
    m_id = message_send(owner_token, channel_id, "Test unpin")['message_id']
    message_pin(owner_token, m_id)
    # now need to unpin
    message_unpin(owner_token, m_id)
    mess = get_message(m_id)
    assert mess['is_pinned'] == False
# message_id is not valid
def test_message_unpin1():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    m_id = message_send(owner_token, channel_id, "Test unpin")['message_id']
    
    with pytest.raises(ValueError, match=r"*"):
        message_unpin(owner_token, -100)
# autorised user is not admin 
def test_message_unpin2():
    clear()
    owner_dict = register_owner()
    user_dict = register_user()
    owner_token = owner_dict['token']
    user_token = user_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    channel_join(user_token, channel_id)
    
    m_id = message_send(owner_token, channel_id, "Test unpin")['message_id']
    
    message_pin(owner_token, m_id)
    with pytest.raises(ValueError, match=r"*"):
        message_unpin(user_token, m_id)      
# message is already unpinned -> don't run pin
def test_message_unpin3():
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    
    m_id = message_send(owner_token, channel_id, "Test pin")['message_id']
    with pytest.raises(ValueError, match=r"*"):
        message_unpin(owner_token, m_id) 
# authorised user is not member of the channel
def test_message_unpin4(): 
    clear()
    owner_dict = register_owner()
    owner_token = owner_dict['token']
    channel_id = create_channel(owner_token)['channel_id']
    not_register = register_not_in_channel()
    not_register_token = not_register['token']
    not_register_uid = not_register['u_id']

    m_id = message_send(owner_token, channel_id, "Test unpin")['message_id']
    message_pin(owner_token, m_id)
    with pytest.raises(AccessError, match=r"*"):
        message_unpin(not_register_token, m_id)



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
from backend.database import get_message

# FUNCTION SETUP

@pytest.fixture
def register_owner():
    return auth_register("sarah@gmail.com", "123456", "Sarah", "Williams")
    # return { u_id, token }

@pytest.fixture
def register_user():
    return auth_register("emma@gmail.com", "123456", "Emma", "Mayall")
    # return { u_id, token }

@pytest.fixture
def register_not_in_channel():
    return auth_regiser("random@random.com", "123456", "first name", "last name")

@pytest.fixture
def create_channel(register_owner):
    token = register_owner['token']
    # return channel_id
    return channels_create(token, "Test channel", False)

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
   m_id = message_sendlater(register_owner['token'], create_channel, message_valid, time_valid) 
   mess = get_message(m_id)
   assert mess['time_created'] == time_valid
# channel id not valid
def test_message_sendlater1(register_owner, create_channel, message_valid, time_valid):
    with pytest.raises(ValueError, match=r"*"):
        message_sendlater(register_owner['token'], -1, message_valid, time_valid)
#message is invalid
def test_message_sendlater2(register_owner, create_channel, message_invalid, time_valid):
    with pytest.raises(ValueError, match=r"*"):
        message_sendlater(register_owner['token'], create_channel, message_invalid, time_valid)
#time is invalid
def test_message_sendlater3(register_owner, create_channel, message_valid, time_invalid):
    with pytest.raises(ValueError, match=r"*"):
        message_sendlater(register_owner['token'], create_channel, message_valid, time_invalid)
# authorised user is not apart of the channel
def test_message_sendlater4(register_not_in_channel, create_channel, message_valid, time_valid):
    with pytest.raises(AccessError, match=r"*"):
        message_sendlater(register_not_in_channel['token'], create_channel, message_valid, time_valid)

# TEST FOR MESSAGE_SEND
# normal functioning
def test_message_send(register_owner, create_channel, message_valid): 
    m_id = message_send(register_owner['token'], create_channel, message_valid) 
    for message in create_channel['messages']:
        if message['message_id'] == m_id:
            assert True
    
    assert False
# invalid message
def test_message_send1(register_owner, create_channel, message_invalid):
    with pytest.raises(ValueError, match=r"*"):
        message_send(register_owner['token'], create_channel, message_invalid)
# authorised user is not apart of the channel
def test_message_send2(register_not_in_channel, create_channel, message_valid):
    with pytest.raises(AccessError, match=r"*"):
        message_send(register_not_in_channel['token'], create_channel, message_valid)
       
# TESTS FOR MESSAGE_REMOVE
# functioning properly
def test_message_remove(register_owner, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Hello world")
    message_remove(register_owner['token'], m_id)
    # assert based on the message_id not existing
    assert get_message(m_id) == None 
# message based on id no longer exists -> call remove twice
def test_message_remove1(register_owner, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Hello world")
    message_remove(register_owner['token'], m_id)
    with pytest.raises(ValueError,match=r"*"):
        message_remove(register_owner['token'], m_id)
# message was not sent by authorised user and user is not admin 
def test_message_remove2(register_owner, register_user, create_channel):
     m_id = message_send(register_owner['token'], create_channel, "Hello world")
     with pytest.raises(AccessError, match=r"*"):
        message_remove(register_user['token'], m_id)
       
# TESTS FOR MESSAGE_EDIT
# normal functioning
def test_message_edit(register_owner, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Hello World")
    message_edit(register_owner['token'], m_id, "Edited message")
    mess = get_message(m_id)
    assert mess['message'] == "Edited message"
#access error
def test_message_edit1(register_owner, register_user, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Hello World")
    with pytest.raises(AccessError, match=r"*"):
        message_edit(register_user['token'], m_id, "Can not edit")   
        
# TESTS FOR MESSAGE_REACT
# normal functioning 
def test_message_react(register_owner, valid_reactid, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Hello")
    message_react(register_owner['token'], m_id, valid_reactid)
    mess = get_message(m_id)
    for react in mess['reacts']:
        if valid_reactid == react['react_id']:
            if register_owner['u_id'] in react['u_ids']:
             assert True
    
    assert False
# message_id is not a valid message
def test_message_react1(register_owner, valid_reactid):
    with pytest.raises(ValueError, match=r"*"):
        message_react(register_owner['token'], -100, valid_reactid)
# react_id is not valid
def test_message_react2(register_owner, create_channel, invalid_reactid, valid_reactid):
    m_id = message_send(register_owner['token'], create_channel, "Hello")
    with pytest.raises(ValueError, match=r"*"):
        message_react(register_owner['token'], m_id, invalid_reactid)
# message already contains an active react
def test_message_react3(register_owner, create_chanel, valid_reactid):
    m_id = message_send(register_owner['token'], create_channel, "Hello")
    message_react(register_owner['token'], m_id, valid_reactid)
    with pytest.raises(ValueError, match=r"*"):
        message_react(register_owner['token'], mi_id, valid_reactid)

# TESTS FOR MESSAGE_UNREACT
# normal functioning  
def test_message_unreact(register_owner, valid_reactid, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Hello")
    message_react(register_owner['token'], m_id, valid_reactid)
    
    mess_unreact(register_owner['token'], m_id, valid_reactid)
    mess = get_message(m_id)
    
    for react in mess['reacts']:
        if valid_reactid == react['react_id']:
            if register_owner['u_id'] not in react['u_ids']:
                assert True
    assert False 

# message_id is not a valid message
def test_message_unreact1(register_owner, valid_reactid):
    m_id = message_send(register_owner['token'], create_channel, "Hello")
    message_react(register_owner['token'], m_id, valid_reactid)
    with pytest.raises(ValueError, match=r"*"):
        message_unreact(register_owner['token'], -100, valid_reactid)
# react_id is not valid
def test_message_unreact2(register_owner, create_channel, invalid_reactid, valid_reactid):
    m_id = message_send(register_owner['token'], create_channel, "Hello")
    message_react(register_owner['token'], m_id, valid_reactid)
    with pytest.raises(ValueError, match=r"*"):
        message_unreact(register_owner['token'], m_id, invalid_reactid)
# message does not contain an active react -> dont call react before i test unreact
def test_message_unreact3(register_owner, create_channel, valid_reactid):
    m_id = message_send(register_owner['token'], create_channel, "Test")
    with pytest.raises(ValueError, match=r"*"):
        message_unreact(register_owner['token'], m_id, valid_reactid)

# TESTS FOR MESSAGE_PIN
# normal functioning
def test_message_pin(register_owner, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Test pin")
    message_pin(register_owner['token'], m_id)
    mess = get_message(m_id)
    assert mess['is_pinned'] == True
# message id is not valid
def test_message_pin1(register_owner, create_channel):
    with pytest.raises(ValueError, match=r"*"):
        message_pin(register_owner['token'], -100)
# autorised user is not admin
def test_message_pin2(register_owner, register_user, create_channel):
    m_id = message_send(register_ower['token'], create_channel, "Test pin")
    with pytest.raises(ValueError, match=r"*"):
        message_pin(register_user['token'], m_id)
# message is already pinned -> run pin twice
def test_message_pin3(register_owner, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Test pin")
    message_pin(register_owner['token'], m_id)
    with pytest.raises(ValueError, match=r"*"):
        message_pin(register_owner['token'], m_id)   
# authorised user is not member of the channel
def test_message_pin4(register_owner, register_not_in_channel, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Test pin")
    with pytest.raises(ValueError, match=r"*"):
        message_pin(register_not_in_channel['token'], m_id)
    
# TEST FOR MESSAGE_UNPIN
# normal functioning
def test_message_unpin(register_owner, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Test unpin")
    message_pin(register_owner['token'], m_id)
    # now need to unpin
    message_unpin(register_owner['token'], m_id)
    mess = get_message(m_id)
    assert mess['is_pinned'] == False
# message_id is not valid
def test_message_unpin1(register_owner, create_channel):
    with pytest.raises(ValueError, match=r"*"):
        message_unpin(register_owner['token'], -100)
# autorised user is not admin
def test_message_unpin2(register_owner, register_user, create_channel):
    m_id = message_send(register_ower['token'], create_channel, "Test pin")
    message_pin(register_owner['token'], m_id)
    with pytest.raises(ValueError, match=r"*"):
        message_unpin(register_user['token'], m_id)
# message is already pinned -> don't run pin
def test_message_unpin3(register_owner, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Test pin")
    with pytest.raises(ValueError, match=r"*"):
        message_unpin(register_owner['token'], m_id) 
# authorised user is not member of the channel
def test_message_unpin4(register_owner, register_not_in_channel, create_channel):
    m_id = message_send(register_owner['token'], create_channel, "Test pin")
    message_pin(register_owner['token'], m_id)
    with pytest.raises(ValueError, match=r"*"):
        message_pin(register_not_in_channel['token'], m_id)



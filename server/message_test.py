from message import *
import pytest
import datetime
from access_error import AccessError

# FUNCTION SETUP 

@pytest.fixture
def register_owner():
    authRegisterDict1 = auth_register("sarah@gmail.com", "123", "Sarah", "Williams")
    # return { u_id, token }
    return authRegisterDict1
    
@pytest.fixture
def register_user():
    authRegisterDict2 = auth_register("emma@gmail.com", "456", "Emma", "Mayall")
    # return { u_id, token }
    return authRegisterDict2
    
@pytest.fixture
def create_channel(register_owner):
    token = register_owner['token']
    # return channel_id
    return channels_create(token, "Test channel", False)['channel_id']
 
@pytest.fixture
def join_user(register_user):
    token = register_user['token']
    channelId = create_channel(register_owner['token'])
    channel_join(token, channelId)
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
def messages_list(register_owner, register_user):
    messages = [{'message_id' : 1, 'u_id' : register_owner['u_id'], 'message': "Hello",   'time_created' : datetime(2019, 5, 3, 7, 0, 0, 0), 'is_unread': False}, 
    {'message_id' : 2, 'u_id' : register_user['u_id'], 'message' : "How are you?", 'time_created' : datetime(2019, 5, 3, 7, 30, 0, 0), 'is_unread': False},
     {'message_id' : 3, 'u_id' : register_owner['u_id'], 'message' : "I'm good thanks", 'time_created' : datetime(2019, 5, 3, 8, 0, 0, 0), 'is_unread': False}]
    return messages

@pytest.fixture
def messages_list2(register_owner, register_user):
    messages2 = [{'message_id' : 4, 'u_id' : register_user['u_id'], 'message' : "Valid Message", 'time_created' : datetime(2019, 7, 4, 7, 0, 0, 0), 'is_unread': False},
    {'message_id' : 5, 'u_id' : register_owner['u_id'], 'message' : "Valid Message", 'time_created' : datetime(2019, 7, 4, 7, 30, 0, 0), 'is_unread': False}, 
    {'message_id' : 6, 'u_id' : register_user['u_id'], 'message' : "Valid Message", 'time_created' : datetime(2019, 7, 4, 8, 0, 0, 0), 'is_unread': False}, 
    {'message_id' : 7, 'u_id' : register_user['u_id'], 'message' : "Valid Message", 'time_created' : datetime(2019, 7, 4, 9, 0, 0, 0), 'is_unread': False}]
    return messages2
    
@pytest.fixture
def valid_reactId():
    return 1

@pytest.fixture
def invalid_reactId():
    return 0


# FUNCTION TESTING 

# testing for message_sendlater
def test_message_sendlater(register_owner, register_user, create_channel, message_valid, message_invalid, time_valid, time_invalid):
    
    # success
    message_sendlater(register_owner['token'], create_channel, message_valid, time_valid) 
    assert channel_messages(register_owner['token'], create_channel, 0) == {'messages' : [{'message_id' : 50, 'u_id' : register_owner['u_id'], 'message' : "Hello World", 'time_created' : datetime(2019, 12, 3, 5, 30, 30, 0), 'is_unread': True}], 'start' : 0, 'end' : -1}
               
    with pytest.raises(ValueError):
        # channel based on Id doesn't exist
        message_sendlater(register_owner['token'], -1, message_valid, time_valid)
        message_sendlater(register_user['token'], -1, message_valid, time_valid)
        # message > 1000 characters
        message_sendlater(register_owner['token'], create_channel, message_invalid, time_valid)
        message_sendlater(register_user['token'], create_channel, message_invalid, time_valid)
        # time sent is in the past
        message_sendlater(register_owner['token'], create_channel, message_valid, time_invalid)
        message_sendlater(register_user['token'], create_channel, message_valud, time_inalid)
      
     
# testing for message_send      
def test_message_send(register_owner, register_user, create_channel, message_valid, message_invalid):
   
    # success
    message_sendlater(register_owner['token'], create_channel, message_valid) 
    assert channel_messages(register_owner['token'], create_channel, 0) == {'messages' : [{'message_id' : 50, 'u_id' : register_owner['u_id'], 'message' : "Hello World", 'time_created' : datetime.now(), 'is_unread': False}], 'start' : 0, 'end' : -1}
    
    with pytest.raises(ValueError):
        # message > 1000 characters
        message_send(register_owner['token'], create_channel, message_invalid)
        message_send(register_user['token'], create_channel, message_invalid)

# testing for message_remove     
def test_message_remove(register_owner, register_user, messages_list, messages_list2):
    
    # success 
    # message sent by the user (logged in person), not the owner of channel
    delete_message = messages_list2[0]
    message_remove(register_user['token'], delete_message['message_id'])
    assert messages_list2 == [ {'message_id' : 5, 'u_id' : register_owner['u_id'], 'message' : "Valid Message", 'time_created' : datetime(2019, 7, 4, 7, 30, 0, 0), 'is_unread': False}, 
    {'message_id' : 6, 'u_id' : register_user['u_id'], 'message' : "Valid Message",  'time_created' : datetime(2019, 7, 4, 8, 0, 0, 0), 'is_unread': False}, 
    {'message_id' : 7, 'u_id' : register_user['u_id'], 'message' : "Valid Message", 'time_created' : datetime(2019, 7, 4, 9, 0, 0, 0), 'is_unread': False}]
    
    # message sent by the user, who is not an admin
    delete_message = messages_list2[1]
    message_remove(register_user['token'], delete_message['message_id'])
    assert messages_list2 == [{'message_id' : 5, 'u_id' : register_owner['u_id'], 'message' : "Valid Message", 'time_created' : datetime(2019, 7, 4, 7, 30, 0, 0), 'is_unread': False}, 
    {'message_id' : 7, 'u_id' : register_user['u_id'], 'message' : "Valid Message", 'time_created' : datetime(2019, 7, 4, 9, 0, 0, 0), 'is_unread': False} ]
    
    # message not sent by the user, who is an owner ofthe channel
    delete_message = messages_list2[1]
    message_remove(register_owner['token'], delete_message['message_id'])
    assert messages_list2 == [{'message_id' : 5, 'u_id' : register_owner['u_id'], 'message' : "Valid Message", 'time_created' : datetime(2019, 7, 4, 7, 30, 0, 0), 'is_unread': False}]
    
    # message not sent by the user, who is an admin
    admin_userpermission_change(register_owner['token'], register_owner['u_id'], 2)
    delete_message = messages_list[1]
    message_remove(register_owner['token'], delete_message['message_id'])
    assert messages_list == [{'message_id' : 1, 'u_id' : register_owner['u_id'], 'message' : "Hello", 'time_created' : datetime(2019, 5, 3, 7, 0, 0, 0), 'is_unread': False},
     {'message_id' : 3, 'u_id' : register_owner['u_id'], 'message' : "I'm good thanks", 'time_created' : datetime(2019, 5, 3, 8, 0, 0, 0), 'is_unread': False}] 
 
    delete_message = messages_list[0]

    with pytest.raises(ValueError):
        # message based on id does not exist
        # this should raise an error as message has already been removed above
        message_remove(register_owner['token'], 2) 
           
    with pytest.raises(AccessError):
        # message was sent by logged in user, message was sent by owner / admin
        message_remove(register_owner['token'], delete_message['message_id'])
 
# testing for message_edit      
def test_message_edit(messages_list, register_owner, register_user):
    
    # success
    # message sent by user (logged in person), not an owner or admin
    message = messages_list[1]
    message_edit(register_user['token'], message['message_id'], "Edit own")
    
    assert messages_list == [{'message_id' : 1, 'u_id' : register_owner['u_id'], 'message' : "Hello", 'time_created' : datetime(2019, 5, 3, 7, 0, 0, 0), 'is_unread': False}, 
    {'message_id' : 2, 'u_id' : register_user['u_id'], 'message' : "Edit own", 'time_created' : datetime(2019, 5, 3, 7, 30, 0, 0), 'is_unread': False}, 
    {'message_id' : 3, 'u_id' : register_owner['u_id'], 'message' : "I'm good thanks", 'time_created' : datetime(2019, 5, 3, 8, 0, 0, 0), 'is_unread': False}]
    
    
    # message not sent by user, is an owner
    message = messages_list[1]
    message_edit(register_owner['token'], message['message_id'], "Edit others")
    
    assert messages_list == [{'message_id' : 1, 'u_id' : register_owner['u_id'], 'message' : "Hello", 'time_created' : datetime(2019, 5, 3, 7, 0, 0, 0), 'is_unread': False}, 
    {'message_id' : 2, 'u_id' : register_user['u_id'], 'message' : "Edit others", 'time_created' : datetime(2019, 5, 3, 7, 30, 0, 0), 'is_unread': False}, 
    {'message_id' : 3, 'u_id' : register_owner['u_id'], 'message' : "I'm good thanks", 'time_created' : datetime(2019, 5, 3, 8, 0, 0, 0), 'is_unread': False}]
    
    # message not sent by the user, is an admin
    message = messages_list[1]
    admin_userpermission_change(register_owner['token'], register_owner['u_id'], 2)
    message_edit(register_owner['token'], message['message_id'], "Edit by admin")
    
    assert messages_list == [{'message_id' : 1, 'u_id' : register_owner['u_id'], 'message' : "Hello", 'time_created' : datetime(2019, 5, 3, 7, 0, 0, 0), 'is_unread': False}, 
    {'message_id' : 2, 'u_id' : register_user['u_id'], 'message' : "Edit by admin", 'time_created' : datetime(2019, 5, 3, 7, 30, 0, 0), 'is_unread': False}, 
    {'message_id' : 3, 'u_id' : register_owner['u_id'], 'message' : "I'm good thanks", 'time_created' : datetime(2019, 5, 3, 8, 0, 0, 0), 'is_unread': False}]
    
    with pytest.raises(ValueError):
        # message sent by user and user is an owner/admin
        message = messages_list[0]
        message_edit(register_owner['token'], message['message_id'], "Not allowed Edit")
    
# testing for message_react
def test_message_react(register_user, register_owner, messages_list, valid_reactId, invalid_reactId):

    # success
    message = messages_list[0]
    message_react(register_user['token'], message['message_id'], valid_reactId)
    message = messages_list[1]
    message_react(register_owner['token'], message['message_id'], valid_reactId)
    
    message1 = messages_list[2]
    message2 = messages_list[0]
    
    with pytest.raises(ValueError):
        # message_id is not a valid message
        message_unpin(register_owner['token'], -1, valid_reactId)
        # react id is not valid
        message_react(register_user['token'], message1['message_id'], invalid_reactId)
        message_react(register_owner['token'], message1['message_id'], invalid_reactId)
        # message already has a react 
        # as the above tests have reacted to a message, use this messages to now
        # raise an exception
        message_react(register_user['token'], message2['message_id'], valid_reactId)
        message_react(register_owner['token'], message2['message_id'], valid_reactId)
    
# testing for message_unreact    
def test_message_unreact(register_user, messages_list, valid_reactId, invalid_reactId):

    # success
    message = messages_list[0]
    message_unreact(register_user['token'], message['message_id'], valid_reactId)
    message = messages_list[1]
    message_unreact(register_ower['token'], message['message_id'], valid_reactId)
    
    message = messages_list[2]
    message1 = messages_list[0]
    
    with pytest.raises(ValueError):
        # message_id is not a valid message
        message_unpin(register_owner['token'], -1, valid_reactId)
        # react id is not valid
        message_unreact(register_user['token'], message['message_id'], invalid_reactId)
        message_unreact(register_owner['token'], message['message_id'], invalid_reactId)
        # message doesn't have a react
        # the above tests have removed a react from messages so use these messages 
        message_unreact(register_user['token'], message1['message_id'], valid_reactId)
        message_unreact(register_owner['token'], message1['message_id'], valid_reactId)

# testing for message_pin
def test_message_pin(register_user, register_owner, messages_list, create_channel):

    # success
    message = messages_list[0]
    admin_userpermission_change(register_owner['token'], register_owner['u_id'], 2)
    message_pin(register_owner['token'], message['message_id'])
   
    message = messages_list[1]
    message1 = messages_list[0]
    with pytest.raises(ValueError):
        # message_id is not a valid message
        message_unpin(register_owner['token'], -1)
        # authorised user is not an admin
        message_pin(register_user['token'], message['message_id'])
        # message is already pinned
        message_pin(register_owner['token'], message1['message_id'])
    
    # send a message to channel and store its message_id
    message_send(register_owner['token'], create_channel, "Test message")
    message_sent = channel_message['messages']
    messageId = message_sent['message_id']
    # remove the user from the channel 
    channel_leave(register_user['token'], create_channel)
    
    with pytest.raises(AccessError):
        # user is not a member of the channel the message is within
        message_pin(register_user['token'], messageId)
        
# testing for message_unpin      
def test_message_unpin(register_user, register_owner, messages_list, create_channel):       
        
    # success
    message = messages_list[0]
    admin_userpermission_change(register_owner['token'], register_owner['u_id'], 2)
    message_unpin(register_owner['token'], message['message_id'])
    
    message = messages_list[1]
    message1 = messages_list[0]
   
    with pytest.raises(ValueError):
        # message_id is not a valid message
        message_unpin(register_owner['token'], -1)
        # authorised user is not an admin
        message_unpin(register_user['token'], message['message_id'])
        # message is already unpinned
        message_unpin(register_owner['token'], message1['message_id'])
        
    # send a message to channel and store its message_id
    message_send(register_owner['token'], create_channel, "Test message")
    message_sent = channel_message['messages']
    messageId = message_sent['message_id']
    # remove the user from the channel 
    channel_leave(register_user['token'], create_channel)
    
    with pytest.raises(AccessError):
        # user is not a member of the channel the message is within
        message_unpin(register_user['token'], messageId)
    


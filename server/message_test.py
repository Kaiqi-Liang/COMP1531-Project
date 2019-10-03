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
    channel = channels_create(token, "Test channel 1", True)
    # return channel_id
    return channel


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
    return datetime(2019, 12, 3, 05, 30, 30, 0)

@pytest.fixture
def time_invalid():
    return (2005, 5, 5, 20, 0, 0, 0) 



# FUNCTION TESTING 
''' need to pass in the fixture that I have set up -- this is where i may need
to make mor as I go long ''' 

# testing for message_sendlater
#potentially break this up into smaller functions
def test_message_sendlater(register_owner, create_channel, message_valid, message_invalid, time_valid, time_invalid):
    
    # success
    message_sendlater(register_owner['token'], create_channel, message_valid, time_valid)
    
    with pytest.raises(ValueError):
        # channel doesn't exist -> don't know yet if can test
        # message > 1000 characters
        message_sendlater(register_owner['token'], create_channel, message_invalid, time_valid)
        # time sent is in the past
        message_sendlater(register_owner['token'], create_channel, message_valid, time_invalid)
        
        
def test_message_send(register_owner, create_channel, message_valid, message_invalid)
    
    # success
    # send message as owner
    message_sendlater(register_owner['token'], create_channel, message_valid)
    # send message as user 
    message_sendlater(register_user['token'], create_channel, message_valid)
    
    with pytest.raises(ValueError):
        # message > 1000 characters
        message_send(register_owner['token'], create_channel, message_invalid)
    

        



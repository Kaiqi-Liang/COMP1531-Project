from message import *
import pytest
import datetime

''' SETUP FOR TESTING '''

''' tokens, type: string'''
@pytest.fixture
def token1():
    return "123"

@pytest.fixture
def token2():
    return "456"
    
@pytest.fixture
def token3():
    return "789"

''' message_id, type: integer '''
@pytest.fixture
def messageid1():
    return 01

@pytest.fixture
def messageid2():
    return 02
    
''' channel id's, type: integer '''
@pytest.fixture
def channelid1():
    return 11
    
@pytest.fixture
def channelid2():
    return 22
    
@pytest.fixture
def channelid3():
    return 33
    
''' messages, type: list of dictionaries where each dictionary contains types 
    { u_id, message, time_created, is_unread } '''
@pytest.fixture
def messages1():
    messagesList = [{'u_id': 100, 'message': 'Hello World', 'time_created': 
                    datetime(2019, 3, 1, 7, 0, 0, 0), 'is_unread': 0},{'u_id': 2
                    'message': 'Second message', 'time_created': 
                    datetime(2019, 10, 8, 7, 7, 0, 0), 'is_unread': 1} ]
    return messagesList

@pytest.fixture
def messages2():
    messagesList = [{'u_id': 5, 'message': 'Good morning!', 'time_created': 
                    datetime(2019, 8, 10, 8, 0, 0, 0), 'is_unread': 0},{'u_id': 6
                    'message': 'Hello, how are you?', 'time_created': 
                    datetime(2019, 8, 10, 9, 7, 0, 0), 'is_unread': 0}, 
                    {'u_id': 5, 'message': 'Doing well, big day ahead', 'time_created'
                    : datetime(2019, 8, 10, 9, 30, 0, 0), 'is_unread': 1}]
    return messagesList


''' this message will raise an exception because of its length ''' 
@pytest.fixture
def messages3():
    messagesList = [{'u_id': 30, 'message': 'Cranial exterior: Frontal bone: forms the  forehead, roofs of the orbits. Parietal bones: paired, form the greater portion of the sides and roof of the cranial cavity. Temporal bones: paired, form the lateral aspects of the cranium. Occipital bones:  forms the posterior part and most of the base of the cranium. Sphenoid bone: middle part of the base of the skull. Key part of the cranial floor, holds bones together (butterfly shape). Ethmoid bone: anterior part of the cranial floor, supporting structure of the nasal cavity. Foramen magnum: large hole on the inferior part of the bone. Occipital condyles: oval processes on either side of the foramen magnum, allows you to nod. External acoustic meatus: ear canal which directs sound waves into the ear. Mastoid process: rounded projection of the mastoid portion of the temporal bone (behind the ear). Cranial interior:Anterior cranial fossa: depression in the floor of the cranial base, housing the frontal lobes. Middle cranial fossa: depression in the middle region of the cranial base, and is deeper and wider than the anterior cranial fossa', 'time_created': 
                    datetime(2019, 10, 8, 8, 0, 0, 0), 'is_unread': 1}]
                    
    return messagesList


''' time_sent, type: datetime '''
''' datetime(year, month, day, hour, minute, second, microsecond) '''
@pytest.fixture
def time1():
    dt1 = datetime(2019, 12, 3, 05, 30, 30, 0)
    return dt1
   
''' in the past and so should raise an exception ''' 
@pytest.fixture
def time2():
    dt2 = datetime(2019, 5, 2, 14, 14, 14, 0)
    return dt2
 
@pytest.fixture
def time3():
    dt3 = datetime(2020, 3, 4, 20, 0, 0, 0)
    return dt3

''' in the past and so should raise an exception ''' 
@pytest.fixture
def time4():
    dt4 = datetime(2005, 5, 5, 20, 0, 0, 0)
    return dt4
        
''' react_id, type: integer '''
@pytest.fixture
def react1():
    return 1
    
@pytest.fixture
def react2():
    return 2
 
@pytest.fixture   
def react3():
    return 3

'''  ---TESTING FUNCTIONS -- '''
'''still unsure about how to test a lot of these and whether they can be tested '''


''' testing for message_sendlater '''
'''def message_sendlater(token, channel_id, message, time_sent):'''

def test_laterNormal(): 

''' function raises an exception when the channel doesn't exist '''
def test_laterNoChannel():
    with pytest.raises(Exception):
        message_sendlater(token1, 0, messages1, time1)
        message_sendlater(token2, 55, messages2, time3)
        message_sendlater(token2, 3, messages1, time1)
        
''' function raises an exception when message exceeds 1000 characters '''
def test_laterExceedes():
    with pytest.raises(Exception):
        message_sendlater(token1, channelid1, messages3, time1)
        message_sendlater(token2, channelid2, messages3, time3)
        message_sendlater(token3, channelid3, messages3, time3)

''' function raises an eception when scheduled time is in the past ''' 
def test_laterPast():
    with pytest.raises(Exception):
        message_sendlater(token1, channelid1, messages1, time2)
        message_sendlater(token2, channelid2, messages3, time2)
        message_sendlater(token3, channelid3, messages3, time4)

''' testing for message_send '''
'''def message_send(token, channel_id, message):'''
def test_sendNormal():

''' function raises an exception when message exceeds 1000 characters '''
def test_sendExceedes():
    with pytest.raises(Exception):
        message_send(token1, channelid1, messages3)
        message_send(token2, channelid2, messages3)
        message_send(token3, channelid3, messages3)

''' testing for  message_remove'''
'''def message_remove(token, message_id):'''
def test_removeNormal():

''' raises an exception when message id does not exist ''' 
def test_removeNotExist():
    with pytest.raises(Exception):
        message_remove(token1, 03)
        message_remove(token2, 04)
        message_remove(token3, 05) 

''' raises an exception if user does not have permission to remove row '''
''' don't know how to test this yet as need to check how permission id works '''  
def test_removePermission():
    with pytest.raises(Exception):
        

''' testing for message_edit  '''
'''def message_edit(token, message_id, message):'''
def test_editNormal():

''' raises an exception when the user is not the poster of the message '''
def test_editNotPoster():

def test_editNVUser():

def test_editNVAdmin():



''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

''' Local packages '''
from server import get_data   # server.py

def message_sendlater(token, channel_id, message, time_sent):
    pass

def message_send(token, channel_id, message):
    pass

# extra function -> move this to helpers probably 
def check_message_exists(message_id):

    channel_list = get_data()['channel']
    for channel in channel_list:
        for mess in channel['messages']:
            if mess['message_id'] == message_id:
                return True
    
    return False 


def message_remove(token, message_id):

    users = getdata()['users']
    channel_list = getdata()['channel']

    # get the permission_id of the authorised user, to use in testing  
    user_id = get_user_from_token(token)
    for user in users:
        if user_id == user['u_id']:
            permission = user['permission_id']
            
    # value error: message with message_id does not exist     
    if not check_message_exists(message_id):
        raise ValueError("Message no longer exists")
    # access error: authorised user did not send the message and are not an admin or owner
    for channel in channel_list :
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                if message['u_id'] != user_id and permission == 3:
                    raise AccessError("Don't have permission to remove message")
    
    # remove the message
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                channel['messages'].remove(message)
    

def message_edit(token, message_id, message):
    
    # get initial data
    channel_list = get_data()['channel']
    users = getdata()['users']
    # below, it returns the u_id 
    user_id = get_user_from_token(token)
    for user in users:
        if user_id == user['u_id']:
            permission = user['permission_id']
    
    # access error: authorised user did not send the message and user is not an admin or owner
    for channel in channel_list :
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                if message['u_id'] != user_id and permission == 3:
                    raise AccessError("Don't have permission to remove message")
     
    # edit the message
    for channel in channe_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                 mess['message'] = message
     # leave the time_created and u_id the same 
            
def message_react(token, message_id, react_id):
    
    channel_list = getdata()['channel']
    # value error: message is not apart of a channel that the user is in 
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                if not check_in_channel(token, channel['id']):
                    raise ValueError("User is not part of channel")
    # value error: react_id is not a valid react id 
    for channel in channel_list:
        for mess in channel['messages']:
            if react_id not in mess['reacts']['react_id']:  # check back to see if this is valid 
                raise ValueError("react_id is not valid")
    # value error: user has already reacted to the message -> this isn't right, need to do it based off message 
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                for react in mess['reacts']:
                    if react_id == react['react_id']:
                        if is_this_user_reacted == True:
                            raise ValueError("Message already contains a react_id from user")

    
    # add the react to the message
    for channel in chanel_list:
        for m in message_list:
            if m['message_id'] == message_id:
                for r_id in m['reacts']:
                    if r_id['react_id'] == react_id:
                        r_id['is_this_user_reacted']  = True
                        r_id['u_ids'].append(get_user_from_token(token))

def message_unreact(token, message_id, react_id):
    
    message_list = getdata()['message']
    react_list = getdata()['reacts']
    
    # value error: message is not in a channel the user is a valid member of
    # value error: react_id is not valid
    if react_id not in react_list['react_id']:
        raise ValueError("react_id is not valid")
    # value error: message does not contain the active react_id from user 
    
    # unreact to the message
    for m in message_list:
        if m['message_id'] == message_id:
            for r_id in m['reacts']:
                if r_id['react_id'] == react_id:
                    r_id['is_this_user_reacted']  = False
                    r_id['u_ids'].remove(get_user_from_token(token))

def message_pin(token, message_id):
    
    # set up data 
    # get initial data
    channel_list = get_data()['channel']
    users = getdata()['users']
    # below, it returns the u_id 
    user_id = get_user_from_token(token)  
    for user in users:
        if user_id == user['u_id']:
            permission = user['permission_id']
    
    # value error: message_id is not valid
    if not check_message_exists(message_id):
        raise ValueError("message_id is not valid")
    # value error: authorised user is not an admin
    if permission != 2:
        raise ValueError("Not an admin")
    # value error: message is already pinned
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                if mess['is_pinned'] == True:
                    raise ValueError("Message is already pinned")
    # access error: authorised user is not apart of the channel -> come back to after channels are set up 
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                if not check_in_channel(token, channel['id']):
                    raise AccessError("User is not a member of the channel")
    
    # pin the message
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                mess['is_pinned'] = True
    
def message_unpin(token, message_id):
    
    # set up data 
    # get initial data
    channel_list = get_data()['channel']
    users = getdata()['users']
    # below, it returns the u_id 
    user_id = get_user_from_token(token)  
    for user in users:
        if user_id == user['u_id']:
            permission = user['permission_id']
    
    # value error: message_id is not valid
    if not check_message_exists(message_id):
        raise ValueError("message_id is not valid")
    # value error: authorised user is not an admin
    if permission != 2:
        raise ValueError("Not an admin")
    # value error: message is already pinned
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                if mess['is_pinned'] == False:
                    raise ValueError("Message is already pinned")
    # access error: authorised user is not apart of the channel -> come back to after channels are set up 
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                if not check_in_channel(token, channel['id']):
                    raise AccessError("User is not a member of the channel") 
    
     # unpin the message
     for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                mess['is_pinned'] = True
    
    

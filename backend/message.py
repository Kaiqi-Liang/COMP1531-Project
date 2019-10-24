''' Local packages '''
from server import get_data   # server.py

def message_sendlater(token, channel_id, message, time_sent):
    pass


def message_send(token, channel_id, message):
    if len(message) > 1000:
        raise ValueError
    channel = is_valid_channel(channel_id)
    channel['message'].append(message)

 
def message_remove(token, message_id):

    channel_list = getdata()['channel']

    # get the permission_id of the authorised user, to use in testing  
    user_id = get_user_from_token(token)
            
    # value error: message with message_id does not exist     
    if not check_message_exists(message_id):
        raise ValueError("Message no longer exists")
    # access error: authorised user did not send the message and are not an admin or owner
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                if mess['u_id'] != user_id and get_permission(user_id) == 3:
                    raise AccessError("Don't have permission to remove message")
    
    # remove the message
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                channel['messages'].remove(mess)
    

def message_edit(token, message_id, message):
    
    # get initial data
    channel_list = get_data()['channel']
    user_id = get_user_from_token(token)
    
    # access error: authorised user did not send the message and user is not an admin or owner
    for channel in channel_list :
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                if mess['u_id'] != user_id and get_permission(user_id) == 3:
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
            if react_id not in mess['reacts']['react_id']:  
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
        for mess in message_list:
            if mess['message_id'] == message_id:
                for r_id in mess['reacts']:
                    if r_id['react_id'] == react_id:
                        r_id['is_this_user_reacted']  = True
                        r_id['u_ids'].append(get_user_from_token(token))

def message_unreact(token, message_id, react_id):
    
    channel_list = getdata()['channel']

    
    # value error: message is not in a channel the user is a valid member of
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                if not check_in_channel(token, channel['id']):
                    raise ValueError("User is not part of channel")
    # value error: react_id is not valid
    for channel in channel_list:
        for mess in channel['messages']:
            if react_id not in mess['reacts']['react_id']:  
                raise ValueError("react_id is not valid")
    # value error: message does not contain the active react_id from user 
    for channel in channel_list:
        for mess in channel['messages']:
            if message_id == mess['message_id']:
                for react in mess['reacts']:
                    if react_id == react['react_id']:
                        if is_this_user_reacted == False:
                            raise ValueError("Message already contains a react_id from user")
    
    # unreact to the message
    for channel in chanel_list:
        for mess in message_list:
            if mess['message_id'] == message_id:
                for r_id in mess['reacts']:
                    if r_id['react_id'] == react_id:
                        r_id['is_this_user_reacted']  = False
                        r_id['u_ids'].remove(get_user_from_token(token))

def message_pin(token, message_id):
     
    # get initial data
    channel_list = get_data()['channel']
    user_id = get_user_from_token(token)  

    # value error: message_id is not valid
    if not check_message_exists(message_id):
        raise ValueError("message_id is not valid")
    # value error: authorised user is not an admin
    if get_permission(user_id) != 2:
        raise ValueError("User is not an admin")
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
    user_id = get_user_from_token(token)  

    
    # value error: message_id is not valid
    if not check_message_exists(message_id):
        raise ValueError("message_id is not valid")
    # value error: authorised user is not an admin
    if get_permission(user_id) != 2:
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
    
    

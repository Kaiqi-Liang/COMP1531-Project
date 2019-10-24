''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from backend.database import get_data

''' regex import'''
import re

''' USER '''
''' Check user with u_id to see if they have permission p_id'''
def check_permission(u_id, p_id):
    slackr = get_data()['slackr']
    return True if u_id in slackr[p_id] else False

''' CHANNEL'''
''' Check if user is in channel '''
def check_in_channel(token, channel_id):
    channels = get_data()['channel']
    for channel in channels:
        if channel['channel_id'] == channel_id:
            return True
    return False

''' If channel_id is valid, return channel. Else return None'''
def is_valid_channel(channel_id):
    for channel in get_data()['channel']:
        if channel['channel_id'] == channel_id:
            return channel
    return None


''' AUTH '''
''' Check if an email is valid '''
def check_email(email):
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' # regex for email address
    if(re.search(email_regex, email)):
        return True
    return False
    
''' MESSAGES'''
''' Check message exists '''
def check_message_exists(message_id):

    channel_list = get_data()['channel']
    for channel in channel_list:
        for mess in channel['messages']:
            if mess['message_id'] == message_id:
                return True
    
    return False 
    
''' Get user permission_id '''
def get_permission(user_id):
    
    users = getdata()['users']
    for user in users:
        if user_id == user['u_id']:
            permission = user['permission_id']
            
    return permission
    
''' Return message dict'''
def message_dict(message_id):
    
    channel_list = get_data['channel']
    
    for channel in channel_list:
        for mess in channel['messages']:
            if mess['message_id'] == message_id:
                return mess
                
''' Return a list of owners of a channel a message with message_id is in'''
def owners_channel(message_id):
    channel_list = getdata()['channel']
    for channel in channel_list:
        for message in channel['messages']:
            if message['message_id'] == message_id:
                return channel['owners']
                
''' Check if a react_id is valid'''
def check_valid_react(react_id, message):

    for react in message['reacts']:
        if react['react_id'] == react_id:
            return True
    
    return False

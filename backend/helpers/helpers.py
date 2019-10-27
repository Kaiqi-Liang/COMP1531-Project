""" Helper functions """
import re
from backend.database import get_data

def check_permission(u_id, p_id):
    ''' Check user with u_id to see if they have permission p_id'''
    slackr = get_data()['slackr']
    return True if u_id in slackr[p_id] else False


def check_in_channel(u_id, channel_id):
    ''' Check if user is in channel '''
    channels = get_data()['channel']
    for channel in channels:
        if channel['channel_id'] == channel_id:
            for member in channel['members']:
                if member['u_id'] == u_id:
                    return True
            return False
    return False


def is_valid_channel(channel_id):
    ''' If channel_id is valid, return channel. Else return None'''
    for channel in get_data()['channel']:
        if channel['channel_id'] == int(channel_id):
            return channel
    return None


def check_email(email):
    ''' Check if an email is valid '''
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' # regex for email address
    if re.search(email_regex, email):
        return True
    return False


def check_message_exists(message_id):
    ''' Check message exists '''
    channel_list = get_data()['channel']
    for channel in channel_list:
        for mess in channel['messages']:
            if mess['message_id'] == message_id:
                return True
    return False


def check_user_in_channel(u_id, channel):
    """ Check if a user is in a channel """
    for member in channel['members']:
        if int(u_id) == member['u_id']:
            return True
    return False


def is_owner(u_id, channel):
    """ Check if a user is an owner of a channel """
    for owner in channel['owners']:
        if int(u_id) == owner['u_id']:
            return True
    return False

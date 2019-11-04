""" Helper functions """
import re
from backend.database import get_data

def check_email(email):
    """ Check if an email is valid """
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' # regex for email address
    if re.search(email_regex, email):
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


def get_message_channel(message_id):
    """ Get the channel that the given message is in """
    for channel in get_data()['channel']:
        for message in channel['messages']:
            if int(message_id) == message['message_id']:
                return channel
    return None

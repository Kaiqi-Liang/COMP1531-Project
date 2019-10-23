import re

def check_in_channel(token, channel_id):
    ''' Check if user is in channel '''
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

EMAIL = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' # regex for email address
def check_email(email):
    ''' Check if an email is valid '''
    if(re.search(EMAIL, email)):
        return True
    return False

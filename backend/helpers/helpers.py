import re

def check_in_channel(token, channel_id):
    ''' Check if user is in channel '''
    channels = channels_list(token)
    for channel in channels:
        if channel[id] == channel_id:
            return True
    return False

EMAIL = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' # regex for email address
def check_email(email):
    ''' Check if an email is valid '''
    if(re.search(EMAIL, email)):
        return True
    return False

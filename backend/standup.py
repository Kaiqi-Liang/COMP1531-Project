''' Standup functions '''
from datetime import datetime, timedelta

from backend.database import get_channel, get_user
from backend.helpers.token import get_user_from_token, generate_token
from backend.helpers.helpers import check_user_in_channel
from backend.helpers.exception import ValueError, AccessError
from backend.message import message_send

def standup_active(token, channel_id):
    channel_id = int(channel_id)
    channel = get_channel(channel_id)
    if channel is None:
        raise ValueError("Channel doesn't exist!")
    standup = channel['standup']
    time_current = datetime.now().timestamp()

    # If standup is finished
    if standup['finish'] < time_current:
        if standup['is_active'] == True:
            standup['is_active'] = False
            message_send(generate_token(standup['user']), channel_id, standup['queue'])
        return {'is_active' : False, 'time_finish' : None}
    else:
        return {'is_active' : True, 'time_finish' : standup['finish']}


def standup_start(token, channel_id, length):
    length = int(length)
    channel_id = int(channel_id)
    # Check if channel exists ...
    channel = get_channel(channel_id)

    if channel is None:
        raise ValueError("Channel doesn't exist!")
    
    standup = channel['standup']

    if standup['is_active'] == True:
        raise ValueError("Standup already running!")

    u_id = get_user_from_token(token)

    # Check if user is a member of the channel ...
    if not check_user_in_channel(u_id, channel):
        raise AccessError("User is not a member of channel!")

    datetime_finish = (datetime.now()+timedelta(seconds=length)).timestamp()
    standup['finish'] = datetime_finish
    standup['user'] = u_id
    standup['is_active'] = True
    return {'time_finish': datetime_finish}


def standup_send(token, channel_id, message):
    channel_id = int(channel_id)
    # Check if channel exists ...
    channel = get_channel(channel_id)

    if channel is None:
        raise ValueError("Channel doesn't exist!")

    standup = channel['standup']
    standup_message = standup['queue']
    u_id = get_user_from_token(token)
    user = get_user(u_id)
    
    # Check if user is a member of the channel ...
    if not check_user_in_channel(u_id, channel):
        raise AccessError("User is not a member of channel!")

    # Check if message is more than 1000 characters ...
    if len(message) > 1000:
        raise ValueError("Message exceeds 1000 characters!")

    # If the arguments pass all tests, continue ...
    standup_message += user['name_first']+": "+message+"\n"

    standup['queue'] = standup_message
    return {}

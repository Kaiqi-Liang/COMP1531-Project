''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

''' Local packages '''
from backend.database import get_data, get_channelm    # backend/database.py
from backend.helpers.token import get_user_from_token
from backend.channel import * # backend/channel.py
from backend.helpers import * # backend/helpers/*.py

''' Std lib packages '''
from datetime import datetime, timedelta

def standup_start(token, channel_id):
    channel_id = int(channel_id)
    # Check if channel exists ...
    channel = get_channel(channel_id)
    if channel == None:
        raise ValueError("Channel doesn't exist!")

    u_id = get_user_from_token(token)

    # Check if user is a member of the channel ...
    if not check_in_channel(u_id, channel_id):
        raise AccessError("User is not a member of channel!")

    datetime_finish = (datetime.now()+timedelta(minutes=15)).timestamp()
    return {'time_finish': datetime_finish}

def standup_send(token, channel_id, message):
    standup_message = ""
    channel_id = int(channel_id)
    # Check if channel exists ...
    channel = get_channel(channel_id)
    if channel == None:
        raise ValueError("Channel doesn't exist!")

    u_id = get_user_from_token(token)
    user = get_user(u_id)
    # Check if user is a member of the channel ...
    if not check_in_channel(u_id, channel_id):
        raise AccessError("User is not a member of channel!")

    # Check if message is more than 1000 characters ...
    if len(message) > 1000:
        raise ValueError("Message exceeds 1000 characters!")

    # If the arguments pass all tests, continue ...
    standup_message += user['name_first']+": "+message

    channel['standup_queue'] = standup_message
    return

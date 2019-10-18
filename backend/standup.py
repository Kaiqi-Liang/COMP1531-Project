''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

''' Local packages '''
from server import get_data   # server.py
from backend.channel import * # backend/channel.py
from backend.helpers import * # backend/helpers/*.py

''' Std lib packages '''
from datetime import datetime, timedelta

def standup_start(token, channel_id):

    # Check if channel exists ...
    if channel_id == None:
        raise ValueError("Channel doesn't exist!")

    # Check if user is a member of the channel ...
    if not check_in_channel(token, channel_id):
        raise AccessError("User is not a member of channel!")

    datetime_finish = datetime.now() + timedelta(minutes=15)
    return datetime_finish

def standup_send(token, channel_id, message):

    # Check if channel exists ...
    if channel_id == None:
        raise ValueError("Channel doesn't exist!")

    # Check if user is a member of the channel ...
    if not check_in_channel(token, channel_id):
        raise AccessError("User is not a member of channel!")

    # Check if message is more than 1000 characters ...
    if len(message) > 1000:
        raise ValueError("Message exceeds 1000 characters!")

    # INSERT CHECK FOR STANDUP TIME STOP HERE ...
    return

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

def message_remove(token, message_id):
    pass

def message_edit(token, message_id, message):
    pass

def message_react(token, message_id, react_id):
    pass

def message_unreact(token, message_id, react_id):
    pass

def message_pin(token, message_id):
    pass

def message_unpin(token, message_id):
    pass

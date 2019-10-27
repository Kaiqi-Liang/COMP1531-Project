''' syspath hack for local imports '''
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

''' Local packages '''
from server import get_data   # server.py
from backend.helpers.token import get_user_from_token

def search(token, query_st):
    #Given a query string, return a collection of messages in all of the channels
    #that the user has joined that match the query
    if query_st == "":
        raise ValueError("Invalid search")
        
    u_id = get_user_from_token(token)
    return_messages = {}
    #get channels
    for channel in get_data()['channel']:
            #check if user is member of channel
            members = channel['members']
            for user in members:
                if u_id == user['u_id']:
                    #search channel messages that match query string
                    for message in channel['messages']:
                        if message.find(query_st) >= 0:
                            return_messages.append(message)
    return return_messages
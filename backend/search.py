''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

''' Local packages '''
from server import get_data   # server.py

def search(token, query_st):
    #Given a query string, return a collection of messages in all of the channels
    #that the user has joined that match the query
    users = channels['members']
    messages = channels['messages']
    for users in query_st:
        messages_match = messages.find(raw_input(""))

    if query_st == "":
        raise ValueError("Invalid search")

    return messages_match

''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

''' Local packages '''
from server import get_data   # server.py

def search(token, query_st):
    if query_st == "":
        raise ValueError("Invalid search")
    messages = {}
    return messages

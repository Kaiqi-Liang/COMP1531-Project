''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from server import get_data # server.py

def admin_userpermission_change (token, u_id, permission_id):
    if u_id == "Invalid user":
            raise ValueError("Does not refer to valid user")
    if permission_id < 1 or permission_id > 3:
            raise ValueError("Invalid permission id")
    # need to check if the user is an admin or owner!!
    return

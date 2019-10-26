''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from backend.database import get_data, get_channel, get_user # server.py

def admin_userpermission_change (token, u_id, permission_id):
        if u_id == "Invalid user":
                raise ValueError("Does not refer to valid user")
        if permission_id < 1 or permission_id > 3:
                raise ValueError("Invalid permission id")
        if  u_id not in slackr['ADMIN']:
                raise AccessError("The authorised user is not an admin or owner") 

        user = get_user(u_id)
        permission_access = user['permission_id']
        slackr[permission_access].remove(u_id)
        for user in users:
                if u_id == user['u_id']: 
                        user['permission_id'] = permission_id
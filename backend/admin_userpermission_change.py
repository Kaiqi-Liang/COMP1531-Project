''' syspath hack for local imports '''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from backend.database import get_data, get_channel, get_user # server.py
from backend.helpers.token import get_user_from_token

#Given a User by their user ID, set their permissions to new permissions 
#described by permission_id
def admin_userpermission_change (token, u_id, permission_id):
        if u_id == "Invalid user":
                raise ValueError("Does not refer to valid user")
        if permission_id < 1 or permission_id > 3:
                raise ValueError("Invalid permission id")

        auth_u_id = get_user_from_token(token)
        auth_user = get_user(auth_u_id)
        if  auth_user['permission_id'] != 1 and auth_user['permission_id'] != 2:
                raise AccessError("The authorised user is not an admin or owner") 

        for user in get_data()['user']:
                if u_id == user['u_id']: 
                        user['permission_id'] = permission_id
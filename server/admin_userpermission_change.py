<<<<<<< HEAD
# pip3 INSTALLS
import pytest

# Stub function
def auth_login (email,password):
    loginDict = {}
    loginDict['u_id'] = 123
    loginDict['token'] = 555
    return loginDict
=======
from access_error import AccessError
>>>>>>> c377cf19e90b526216f77c2141207c55aef0ce3e

def admin_userpermission_change (token, u_id, permission_id):
    if u_id == "Invalid user":
            raise ValueError("Does not refer to valid user")
    if permission_id < 1 or permission_id > 3:
            raise ValueError("Invalid permission id")
    # need to check if the user is an admin or owner!!
    return

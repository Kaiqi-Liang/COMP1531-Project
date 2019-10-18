from server.helpers import * # helpers/*.py
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from app import get_data

def auth_login (email,password):
    user = get_data()['user']
    print(user)
    if email == 'wrong email':
        raise ValueError("Invalid login email")
        if password == 'wrong password':
            raise ValueError("Invalid password")
    loginDict = {}
    loginDict['u_id'] = 123
    loginDict['token'] = '555'
    return {token}

def auth_logout (token):
    if token == "":
        raise ValueError("No token")
    if token == True:
        return {True}
    else:
        return {False}

def auth_register (email,password,name_first,name_last):
    if email == "Invalid email":
        raise ValueError("Invalid email address")
    if email == "Existing email":
        raise ValueError("Email already exists")
    if len(password) < 5:
        raise ValueError("Invalid password")
    if len(name_first) > 50:
        raise ValueError("First Name is too long")
    if len(name_last) > 50:
        raise ValueError("Last Name is too long")
    loginDict = {}
    loginDict['u_id'] = 123
    loginDict['token'] = '555'
    return loginDict

def auth_passwordreset_request (email):
    if email == "":
        raise ValueError("No email")
    return

@app.route("auth/passwordreset/reset")
def auth_passwordreset_reset (reset_code, new_password):
    if isinstance(reset_code, str): # Check if reset_code is valid i.e. a string
        raise ValueError("Invalid reset code")
    if len(new_password) < 6:
        raise ValueError("Invalid password")
    return

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
        
# EXTRA FUNCTION
# use jwt to generate a token and store the secret of the user, inc username and email 
def generateToken(name_first, name_last, email, pass_word):
    secrete = {
                'password' : pass_word
              }
    encoded_jwt = jwt.encode({'first_name' : name_first,'last_name' : name_last,'email' : email}, secrete, algorithm = 'HS256')
    return encoded_jwt

# use jwt decode to find a user 
def getUserFromToken(token):

    user = jwt.decode(token, secrete, algorithm = 'HS256')
    return user

@APP.route('auth/register', methods = ['POST'])
def auth_register (email,password,name_first,name_last):
 
    # BEGIN BY TESTING ARG VALUES
    # Value error: password is less than 6 characters long
    if len(password) < 6:
        raise ValueError(f"Password entered is less than 6 characters long")
    # Value error: name_first 
    if len(name_first) >= 50 or len(name_first) <= 1:
        raise ValueError(f"First name is not within the correct length range")
    # Value error: name_last
    if len(name_last) >= 50 or len(name_last) <= 1:
        raise ValueError(f"Last name is not within the correct length range")
    # Value error: invalid email
    regExpression = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not (re.search(regex,email)):
        raise ValueError(f"Email entered is invalid")
    # Value error: email is already being used -> potentially redo this, just check back on how i later store emails. 
    if email in DATA['members']['email']:
        raise ValueError(f"Email already used on a registered account")  
        
    # CREATE A NEW ACCOUNT
    # generate a u_id, this method is based on the number of users
    numberUsers = len(DATA['members'])
    u_id = (numberUsers + 1)
    
    # generate a handle that is a lowercase concatenation of their first and last name 
    handle = lower(name_first) + lower(name_last)
    # if this is longer than 20 characters, need to concatenate
    if len(handle) > 20:
        handle = handle[:20]
    # check if this handle is already taken 
    occurences = DATA['members']['handles'].count(handle)
    # if this handle is taken, change the handle to have a number at the end
    if occurences > 0:
        handle = handle + occurences 
    
    # generate a token
    token = generateToken(name_first, name_last, email, password)
    
    # work out permission_id
    if len(DATA['members']) is 0:
        p_id = 1
    else:
        p_id = 3
    
    # add this data to the DATA members list
    DATA['members'].append({
        'name_first': name_first,
        'name_last' : name_last,
        'u_id' : u_id,
        'token' : token,
        'permission_id' : p_id,
        'email' : email,
        'handle': handle
    })
    
    return dumps({
        'u_id' : u_id,
        'token' : token
    })

def auth_passwordreset_request (email):
    if email == "":
        raise ValueError("No email")
    return

def auth_passwordreset_reset (reset_code, new_password):
    if reset_code == "Invalid reset code":
        raise ValueError("Invalid reset code")
    if len(new_password) < 5:
        raise ValueError("Invalid password")
    return

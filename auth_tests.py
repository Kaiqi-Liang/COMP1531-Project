import pytest

#Stub Functions
def auth_login (email,password):
        if email == 'wrong email':
                raise ValueError("Invalid login email")
        if password == 'wrong password':
                raise ValueError("Invalid password")
        loginDict = {}
        loginDict['u_id'] = 123
        loginDict['token'] = 555

def auth_logout (token):
    raise ValueError

def auth_register (email,password,name_first,name_last):
    raise ValueError

def auth_passwordreset_request (email):
    raise ValueError

def auth_passwordreset_reset (reset_code, new_password):
    raise ValueError

#pytests
def test_login1 ():
        loginDict = {}
        loginDict = auth_login("emmarosemayall@gmail.com", "123456")
        pass

def test_login2 ():
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_login("wrong email", "123456")
        pass

def test_login3 ():
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_login("emmarosemayall@gmail.com", "wrong password")

'''   
def test_logout ():
        pass
        #assumption the token taken is the same as returned
        #returns an empty dictionary

def test_register1 ():
        #Setup begin
        authRegisterDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
        token = authRegisterDict['token']
        #Setup end

        auth_register("emmarosemayall@gmail.com", )

        with pytest.raises(ValueError, match=r"*"):
                auth_register("bademail")
                #Email entered is not a valid email. 
                #Email address is already being used by another user
                #Password entered is not a valid password
                #name_first is more than 50 characters
                #name_last is more than 50 characters
        pass

def test_passwordreset_request ():
        pass
        #Check if the user is registered and then test if the function was successful. Make your own assumptions

def test_passwordreset_reset ():
        pass
'''
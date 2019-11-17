''' pip3 packages '''
import pytest

''' Local packages '''
from backend.auth import auth_login, auth_logout, auth_register, auth_passwordreset_reset
from backend.database import clear
from backend.helpers.exception import ValueError, AccessError

def test_login1():
    clear()
    loginDict = {}
    auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    loginDict = auth_login("emmarosemayall@gmail.com", "123456")
    uid = loginDict['u_id']
    token = loginDict['token']
    assert uid != "" and token != ""

def test_login2():
    # test for invalid email
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_login("wrong email", "123456")

def test_login3():
    # test for invalid password
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_login("emmarosemayall@gmail.com", "wrong password")

def test_logout1():
    clear()
    user_dict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    assert auth_logout(user_dict['token'])['is_success'] == True

def test_register1():
    # test for when everything is valid
    clear()
    loginDict = {}
    loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayalllonglastname")
    loginDict2 = auth_register("emmarosemayal@gmail.com", "123456", "Emma", "Mayalllonglastnamememe")
    uid = loginDict['u_id']
    token = loginDict['token']
    assert uid != "" and token != ""

def test_register2():
    # test for invalid email
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_register("Invalid email", "123456", "Emma", "Mayall")

def test_register3 ():
    # test for email existing
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_register("Existing email", "123456", "Emma", "Mayall")

def test_register4():
    # test for invalid password
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_register("emmarosemayall@gmail.com", "1234", "Emma", "Mayall")

def test_register5():
    # test for first name length greater than 50
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Mayall")

def test_register6():
    # test for last name length greater than 50
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayallllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")

'''def test_passwordreset_request1():
        auth_passwordreset_request ("emmarosemayall@gmail.com")

def test_passwordreset_request2():
        # test for no email
        with pytest.raises(ValueError, match=r"*"):
                auth_passwordreset_request ("") 

def test_passwordreset_reset1():
        # test for valid reset
        auth_passwordreset_reset("xyz", "123456")
'''

def test_passwordreset_reset1():
    #test for invalid reset code
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_passwordreset_reset ("Invalid reset code", "123456")

def test_passwordreset_reset2():
    #test for invalid password
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_passwordreset_reset ("xyz", "1234")

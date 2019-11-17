''' pip3 packages '''
import pytest

''' Local packages '''
from backend.auth import auth_login, auth_logout, auth_register, auth_passwordreset_reset
from backend.database import clear
from backend.helpers.token import generate_token
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
    clear()
    loginDict = {}
    auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    # test for invalid email
    with pytest.raises(ValueError, match=r"*"):
        loginDict = auth_login("wrong email", "123456")

def test_login3():
    clear()
    auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    # test for invalid password
    with pytest.raises(ValueError, match=r"*"):
        loginDict = auth_login("emmarosemayall@gmail.com", "wrong password")

def test_login4():
    clear()
    with pytest.raises(ValueError):
        # email does not belong to any user
        auth_login("sarahilwil@gmail.com", 1234456)
        
def test_logout1():
    clear()
    user_dict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    assert auth_logout(user_dict['token'])['is_success'] == True

def test_logout2():
    clear()
    assert auth_logout(generate_token(100)) == {'is_success': False}
    
def test_register1():
    # test for when everything is valid
    clear()
    loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayalllonglastname")
    loginDict2 = auth_register("emmarosemayal@gmail.com", "123456", "Emma", "Mayalllonglastnamememe")
    uid = loginDict['u_id']
    token = loginDict['token']
    assert uid != "" and token != ""

def test_register2():
    clear()
    # test for invalid email
    with pytest.raises(ValueError, match=r"*"):
        loginDict = auth_register("Invalid email", "123456", "Emma", "Mayall")

def test_register3 ():
    clear()
    auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    # test for email existing
    with pytest.raises(ValueError, match=r"*"):
        loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")

def test_register4():
    clear()
    # test for invalid password
    with pytest.raises(ValueError, match=r"*"):
        loginDict = auth_register("emmarosemayall@gmail.com", "1234", "Emma", "Mayall")

def test_register5():
    clear()
    # test for first name length greater than 50
    with pytest.raises(ValueError, match=r"*"):
        loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Mayall")

def test_register6():
    clear()
    # test for last name length greater than 50
    with pytest.raises(ValueError, match=r"*"):
        loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayallllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")


def test_passwordreset_reset2():
    #test for invalid reset code
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_passwordreset_reset (1234, "123456")

def test_passwordreset_reset3():
    #test for invalid password
    with pytest.raises(ValueError, match=r"*"):
        loginDict = {}
        loginDict = auth_passwordreset_reset ("xyz", "1234")

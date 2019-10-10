# pip3 INSTALLS
import pytest
from auth import *

def test_login1 ():
        loginDict = {}
        loginDict = auth_login("emmarosemayall@gmail.com", "123456")
        uid = loginDict['u_id']
        token = loginDict['token']
        assert uid != "" and token != ""

def test_login2 ():
        # test for invalid email
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_login("wrong email", "123456")

def test_login3 ():
        # test for invalid password
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_login("emmarosemayall@gmail.com", "wrong password")

def test_logout1 ():
        auth_logout ("111")
        pass

def test_logout2 ():
        # test for no token
        with pytest.raises(ValueError, match=r"*"):
                auth_logout ("")

def test_register1 ():
        # test for when everything is valid
        loginDict = {}
        loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
        uid = loginDict['u_id']
        token = loginDict['token']
        assert uid != "" and token != ""

def test_register2 ():
        # test for invalid email
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_register("Invalid email", "123456", "Emma", "Mayall")

def test_register3 ():
        # test for email existing
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_register("Existing email", "123456", "Emma", "Mayall")

def test_register4 ():
        # test for invalid password
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_register("emmarosemayall@gmail.com", "1234", "Emma", "Mayall")

def test_register5 ():
        # test for first name length greater than 50
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Mayall")

def test_register6 ():
        # test for last name length greater than 50
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayallllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")

def test_passwordreset_request1 ():
        auth_passwordreset_request ("emmarosemayall@gmail.com")
        pass

def test_passwordreset_request2 ():
        # test for no email
        with pytest.raises(ValueError, match=r"*"):
                auth_passwordreset_request ("")

def test_passwordreset_reset1 ():
        # test for valid reset
        auth_passwordreset_reset ("xyz", "123456")
        pass

def test_passwordreset_reset2 ():
        #test for invalid reset code
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_passwordreset_reset ("Invalid reset code", "123456")

def test_passwordreset_reset3 ():
        #test for invalid password
        with pytest.raises(ValueError, match=r"*"):
                loginDict = {}
                loginDict = auth_passwordreset_reset ("xyz", "1234")

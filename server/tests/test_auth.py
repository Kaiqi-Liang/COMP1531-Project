# pip3 INSTALLS
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
        return loginDict

def auth_logout (token):
        if token == "":
                raise ValueError("No token")
        return

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
        loginDict['token'] = 555
        return loginDict

def auth_passwordreset_request (email):
        if email == "":
                raise ValueError("No email")
        return

def auth_passwordreset_reset (reset_code, new_password):
        if reset_code == "Invalid reset code":
                raise ValueError("Invalid reset code")
        if len(password) < 5:
                raise ValueError("Invalid password")
        return

#pytests
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

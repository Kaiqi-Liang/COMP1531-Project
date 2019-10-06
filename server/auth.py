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


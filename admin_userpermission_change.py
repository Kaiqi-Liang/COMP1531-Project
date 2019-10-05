import pytest

# Stub function
def auth_login (email,password):
    loginDict = {}
    loginDict['u_id'] = 123
    loginDict['token'] = 555
    return loginDict

def admin_userpermission_change (token, u_id, permission_id):
    if u_id == "Invalid user":
            raise ValueError("Does not refer to valid user")
    if permission_id < 1 or permission_id > 3:
            raise ValueError("Invalid permission id")
    # need to check if the user is an admin or owner!!
    return

# Tests
def test_admin_userpermission_change1():
    # setup begin
    loginDict = auth_login("emmarosemayall@gmail.com", "1233456")
    token = loginDict["token"]
    uid = loginDict["u_id"]
    #setup end

    #test for when we have a valid permission id
    admin_userpermission_change (token, uid, 1)
    pass

def test_admin_userpermission_change2():
    # setup begin
    loginDict = auth_login("emmarosemayall@gmail.com", "1233456")
    token = loginDict["token"]
    uid = loginDict["u_id"]
    #setup end

    #test for when we have an invalid permission id
    with pytest.raises(ValueError, match=r"*"):
        admin_userpermission_change (token, uid, 5)

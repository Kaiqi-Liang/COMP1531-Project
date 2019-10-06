import pytest
from auth import auth_login
from admin_userpermission_change import admin_userpermission_change

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

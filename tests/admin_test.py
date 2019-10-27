''' pip3 packages '''
import pytest

''' Local packages '''
from backend.auth import auth_register
from backend.auth import auth_login
from backend.admin import admin_userpermission_change
from backend.database import clear
from backend.helpers.exception import ValueError, AccessError

def test_admin_userpermission_change1():
    # setup begin
    clear()
    loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    token = loginDict["token"]
    uid = loginDict["u_id"]
    #setup end

    #test for when we have a valid permission id
    admin_userpermission_change(token, uid, 2)

def test_admin_userpermission_change2():
    # setup begin
    clear()
    loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    token = loginDict["token"]
    uid = loginDict["u_id"]
    #setup end

    #test for when we have an invalid permission id
    with pytest.raises(ValueError, match=r"*"):
        admin_userpermission_change(token, uid, 5)
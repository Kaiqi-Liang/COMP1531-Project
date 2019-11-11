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
    # setup end

    with pytest.raises(AccessError, match=r"*"):
        # there is only one user who is the owner of slackr
        admin_userpermission_change(token, uid, 2)

def test_admin_userpermission_change2():
    # setup begin
    clear()
    loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    token = loginDict["token"]
    uid = loginDict["u_id"]
    # setup end

    #test for when we have an invalid permission id
    with pytest.raises(ValueError, match=r"*"):
        admin_userpermission_change(token, uid, 5)

def test_admin_userpermission_change3():
    # setup begin
    clear()
    loginDict1 = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    token1 = loginDict1["token"]
    uid1 = loginDict1["u_id"]

    loginDict2 = auth_register("kaiqi.liang9989@gmail.com", "123456", "Kaiqi", "Liang")
    token2 = loginDict2["token"]
    uid2 = loginDict2["u_id"]
    # setup end

    # user1 makes user2 an owner of the slackr 
    admin_userpermission_change(token1, uid2, 1)
    # user2 makes user1 an admin of the slackr since now user1 is an owner it has permission to do so
    admin_userpermission_change(token2, uid1, 2)

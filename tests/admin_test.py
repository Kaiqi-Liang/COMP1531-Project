''' pip3 packages '''
import pytest

''' Local packages '''
from backend.auth import auth_register
from backend.auth import auth_login
from backend.admin import admin_userpermission_change
from backend.database import clear
from backend.helpers.exception import ValueError, AccessError

@pytest.fixture
def register_admin():
    admin_dict = auth_register("sarah@gmail.com", "123456", "Sarah", "Williams")
    # return { u_id, token }
    return admin_dict

@pytest.fixture
def register_user():
    return auth_register("emma@gmail.com", "123456", "Emma", "Mayall")

@pytest.fixture
def register_user2():
    return auth_register("sarahwilliams@gmail.com", "1234455", "sara", "william")

# user w id does not refer to a valid user
def test_admin_userpermission_change():
    clear()
    admin_dict = register_admin()
    with pytest.raises(ValueError):
        admin_userpermission_change(admin_dict['token'], 100, 1)
        
# permission id is invalid
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
 
# user is not admin or owner
def test_admin_user_permission_change3():
    clear()
    admin_dict = register_admin()
    user_dict = register_user()
    with pytest.raises(AccessError):
        admin_userpermission_change(user_dict['token'], admin_dict['u_id'], 3)
        
# permission id is being changed to what it already is    
def test_admin_userpermission_change5():
    clear()
    admin_dict = register_admin()
    user_dict = register_user()  
    assert admin_userpermission_change(admin_dict['token'], user_dict['u_id'], 3) == {}
     
# valid case
def test_admin_userpermission_change4():
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

# the user w token is an admin (permission 2)
def test_admin_userpermission_change6():
    # set up
    clear()
    admin_dict = register_admin()
    user_dict = register_user() 
    admin_userpermission_change(admin_dict['token'], user_dict['u_id'], 2)
    
    with pytest.raises(AccessError):
        admin_userpermission_change(user_dict['token'], admin_dict['u_id'], 3)

# user is admin and changes another admin to a member
def test_admin_userpermission_change7():
    clear()
    admin_dict = register_admin()
    user_dict = register_user()
    user_dict2 = register_user2()
    admin_userpermission_change(admin_dict['token'], user_dict['u_id'], 2)
    admin_userpermission_change(admin_dict['token'], user_dict2['u_id'], 2)
    
    # admin changes an admin to member
    admin_userpermission_change(user_dict['token'], user_dict2['u_id'], 3)

# admin changes a member to an admin
def test_admin_userpermission_change8():
    clear()
    admin_dict = register_admin()
    user_dict = register_user()
    user_dict2 = register_user2()
    admin_userpermission_change(admin_dict['token'], user_dict['u_id'], 2)
    
    admin_userpermission_change(user_dict['token'], user_dict2['u_id'], 2)

# user that is an owner changing itself
def test_admin_userpermission_change9():
    clear()
    admin_dict = register_admin()  
    assert admin_userpermission_change(admin_dict['token'], admin_dict['u_id'], 3) == {} 

# change permission twice
def test_admin_userpermission_change10():
    clear()
    admin_dict = register_admin()  
    user_dict = register_user()
    # change user to an admin
    admin_userpermission_change(admin_dict['token'], user_dict['u_id'], 1)

    # user change original owner to admin
    admin_userpermission_change(user_dict['token'], admin_dict['u_id'], 2)

    # user change original owner's permission again to owner
    admin_userpermission_change(user_dict['token'], admin_dict['u_id'], 3)

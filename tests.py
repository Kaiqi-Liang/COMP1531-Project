import pytest
from user import *
from access_error import AccessError


def user_profile(token, u_id):
    if u_id == -1:
        raise ValueError("u_id not found!")
    else:
        return {"someemail@gmail.com","securepassword","John","Doe","johndoe"}

def test_user_profile():
    u_id, token = auth_register("someemail@gmail.com","securepassword","John","Doe")
    user_profile_sethandle(token,"johndoe")

    # Set arbitrary id thats invalid ...
    invalid_u_id = -1

    # correct case ...
    assert user_profile(token, u_id)=={"someemail@gmail.com","securepassword","John","Doe","johndoe"}

    # incorrect case ...
    with pytest.raises(ValueError, match=r"*"):
        user_profile(token, invalid_u_id)

def user_profile_setname(token, name_first, name_last):
    if (len(name_first) > 50 or len(name_last) > 50):
        raise ValueError("Name too long!")
    return

def test_user_profile_setname():
    u_id1, token1 = auth_register("someemail1@gmail.com","securepassword","John","Doe")
    u_id2, token2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")
    u_id3, token3 = auth_register("someemail3@gmail.com","securepassword","Juan","Doe")
    u_id4, token4 = auth_register("someemail4@gmail.com","securepassword","Juan","Smith")

    user_profile_setname(token1, "Johnnette", "Doette")

    with pytest.raises(ValueError, match=r"*"):
        # First name exceeding 50 chars ...
        user_profile_setname(token2, "hugefirstnamethatiscertainlylongerthanfiftycharacters", "Smith")
        # Second name exceeding 50 chars ...
        user_profile_setname(token3, "Juan", "hugesecondtnamethatiscertainlylongerthanfiftycharacters")
        # Both names exceeding 50 chars ...
        user_profile_setname(token4, "hugefirstnamethatiscertainlylongerthanfiftycharacters", "hugesecondtnamethatiscertainlylongerthanfiftycharacters")

def user_profile_setemail(token, email):
    if (email == "notvalidemail.com")
        raise ValueError("Invalid email address!")
    elif (email == "someemail2@gmail.com")
        raise ValueError("Email in use!")
    return

def test_user_profile_setemail():
    u_id1, token1 = auth_register("someemail1@gmail.com","securepassword","John","Doe")
    u_id2, token2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

    # Valid case ...
    user_profile_setemail(token1, "someemail3@gmail.com")

    with pytest.raises(ValueError, match=r"*"):
        # This should be invalid because u_id2 is using the same email ...
        user_profile_setemail(token1, "someemail2@gmail.com")

        # This should be invalid because the email address is bonkers ...
        user_profile_setemail(token1, "notvalidemail.com")
def user_profile(token, u_id):
    pass

def test_user_profile():
    u_id, token = auth_register("someemail@gmail.com","securepassword","first","last")
    user_profile_sethandle(token,"firstlast")

    # Set arbitrary id thats not in db ...
    invalid_u_id = -1

    # correct case ...
    assert user_profile(token, u_id)=={"someemail@gmail.com","securepassword","first","last","firstlast"}

    # incorrect case ...
    with pytest.raises(ValueError, match=r"*"):
        user_profile(token, invalid_u_id)

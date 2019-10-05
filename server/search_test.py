import pytest

# Stub function
def auth_login (email,password):
    loginDict = {}
    loginDict['u_id'] = 123
    loginDict['token'] = 555
    return loginDict

def search(token, query_st):
    if query_st == "":
        raise ValueError("Invalid search")
    messages = {}
    return messages

# Tests
def test_search1():
    # setup begin
    loginDict = auth_login("emmarosemayall@gmail.com", "1233456")
    token = loginDict["token"]
    #setup end

    # test for valid search
    search (token, "Hello World")
    pass

def test_search2():
    # setup begin
    loginDict = auth_login("emmarosemayall@gmail.com", "1233456")
    token = loginDict["token"]
    #setup end

    # test for no message
    with pytest.raises(ValueError, match=r"*"):
            search (token, "")


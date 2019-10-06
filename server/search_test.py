import pytest
from search import search
from auth import auth_login

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


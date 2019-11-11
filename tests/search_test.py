''' pip3 packages '''
import pytest

''' Local packages '''
from backend.search import search
from backend.auth import auth_register
from backend.auth import auth_login

def test_search1():
    # setup begin
    loginDict = auth_register("emmarosemayall@gmail.com", "123456", "Emma", "Mayall")
    token = loginDict["token"]
    #setup end

    # test for valid search
    search(token, "Hello World")
    pass

def test_search2():
    # setup begin
    loginDict = auth_login("emmarosemayall@gmail.com", "123456")
    token = loginDict["token"]
    #setup end

    # test for no message
    with pytest.raises(ValueError, match=r"*"):
        search(token, "")
'''
def test_search3():
    # setup begin
    loginDict = auth_login("emmarosemayall@gmail.com", "123456")
    token = loginDict["token"]
    #setup end

    # test for a match
    messages_search = search(token, "Hello")
    assert(len(messages_search) == 2)
'''

import pytest
from access_error import AccessError

# Stub function
def search(token, query_st):
    loginDict = {}
    loginDict['query_str'] = 123
    loginDict['token'] = 555
    return loginDict

# Tests
def test_search1():
    search ("Hello World")
    pass
    
def test_search2():
    # test for no message
    with pytest.raises(ValueError, match=r"*"):
            search ("")



    



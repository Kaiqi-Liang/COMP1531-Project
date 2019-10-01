import pytest
from channel import *
from access_error import AccessError

@fixture
auth_register("a@b", "a", "")

def test_invite():
    with pytest.raises(ValueError):
        # invalid token
        channel_invite('token',0,0)
        # empty token
        channel_invite('token',0,0)
        # invalid channel id
        channel_invite('token',0,0)
        # invalid user id
        channel_invite('token',0,0)

def test_details():
    with pytest.raises(AccessError):
        channel_detail()

def test_create():
    with pytest.raises(ValueError):
        # name is more than 20 characters long
        channels_create('token','012345678901234567890',True)
        

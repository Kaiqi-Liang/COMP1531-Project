import pytest
from channel import *

def test_invite():
    with pytest.raises(ValueError):
        channel_invite('token',0,0)
        channel_invite('',0,0)

def test_create():
    with pytest.raises(ValueError):
        channels_create('token','012345678901234567890',True)

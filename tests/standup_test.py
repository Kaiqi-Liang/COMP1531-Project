import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import config

import pytest

from server import *


def test_standup_start():

    # Create users ...
    u_id1, token1 = auth_register("someemail@gmail.com","securepassword","John","Doe")
    u_id2, token2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

    # Create channel ...
    # Assuming channels_create doesn't add the user and make them owner by default ...
    channel_id = channels_create(token1, "sample", True)

    # Add user1 to channel ...
    channel_addowner(token1, channel_id, uid1)
    channel_join(token1, channel_id)

    # Valid case ...
    standup_start(token1, channel_id)

    # Invalid cases ...
    with pytest.raises(ValueError, match=r"*"):
        # Channel doesnt exist ...
        standup_start(token1, None)

    with pytest.raises(AccessError, match=r"*"):
        # User2 is not a member of channel ...
        standup_start(token2, channel_id)

def test_standup_send():

    # Create users ...
    u_id1, token1 = auth_register("someemail@gmail.com","securepassword","John","Doe")
    u_id2, token2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

    # Create channel ...
    # Assume channels_create doesn't add the user and make them owner by default ...
    channel_id = channels_create(token1, "sample", True)

    # Add user1 to channel ...
    channel_addowner(token1, channel_id, uid1)
    channel_join(token1, channel_id)

    # Start standup
    standup_start(token1, channel_id)

    # Valid case ...
    standup_send(token1, channel_id, "A message")

    # Invalid cases ...
    with pytest.raises(ValueError, match=r"*"):
        # Channel doesnt exist ...
        standup_send(token1, None, "A message")

        # Message too long ...
        standup_send(token1, channel_id, "a"*1001)

    with pytest.raises(AccessError, match=r"*"):
        # User2 is not a member of channel ...
        standup_send(token2, channel_id, "A message")

        # WRITE TEST FOR WHEN STANDUP FINISHES !!!

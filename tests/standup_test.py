''' Local packages '''
from backend.helpers.exception import ValueError, AccessError
from backend.database import clear
from backend.standup import standup_start, standup_active, standup_send
from backend.auth import auth_register
from backend.channel import channels_create

''' pip3 packages '''
import pytest


def test_standup_active1():
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
    # Create channel ...
    # Assuming channels_create adds the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)
    standup_start(ret['token'],)


def test_standup_start1():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")

    # Create channel ...
    # Assuming channels_create adds the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)

    # Valid case ...
    assert (standup_start(ret['token'], channel_ret['channel_id'])['time_finish'] - (datetime.now()+timedelta(minutes=15)).timestamp()) < 1


def test_standup_start():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")

    # Create channel ...
    # Assuming channels_create doesn't add the user and make them owner by default ...
    invalid_channel_id = 2
    # Invalid cases ...
    with pytest.raises(ValueError, match=r"*"):
        # Channel doesnt exist ...
        standup_start(ret['token'], invalid_channel_id)


def test_standup_start():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
    ret2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

    # Create channel ...
    # Assuming channels_create doesn't add the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)

    with pytest.raises(AccessError, match=r"*"):
        # User2 is not a member of channel ...
        standup_start(ret2['token'], channel_ret['channel_id'])


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

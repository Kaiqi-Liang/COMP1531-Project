''' Local packages '''
from backend.helpers.exception import ValueError, AccessError
from backend.database import clear
from backend.standup import standup_start, standup_active, standup_send
from backend.auth import auth_register
from backend.channel import channels_create

import time # for testing standup duration
from datetime import datetime, timedelta

''' pip3 packages '''
import pytest

def test_standup_active1():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
    # Create channel ...
    # Assuming channels_create adds the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)
    standup_start(ret['token'],channel_ret['channel_id'],5)
    standup_active_ret = standup_active(ret['token'],channel_ret['channel_id'])
    assert (standup_active_ret['is_active'] == True)


def test_standup_active2():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
    # Create channel ...
    # Assuming channels_create adds the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)
    invalid_channel_id = 2

    # test invalid channel_id
    with pytest.raises(ValueError, match=r"*"):
        # Channel doesnt exist ...
        standup_active(ret['token'], invalid_channel_id)

def test_standup_active3():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
    # Create channel ...
    # Assuming channels_create adds the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)
    standup_start(ret['token'],channel_ret['channel_id'],0)
    time.sleep(1)
    standup_active_ret = standup_active(ret['token'],channel_ret['channel_id'])
    assert (standup_active_ret['is_active'] == False)

def test_standup_active4():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
    # Create channel ...
    # Assuming channels_create adds the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)
    standup_start(ret['token'],channel_ret['channel_id'],0)
    time.sleep(1)
    standup_active_ret = standup_active(ret['token'],channel_ret['channel_id'])
    standup_active_ret2 = standup_active(ret['token'],channel_ret['channel_id'])
    assert (standup_active_ret['is_active'] == False)


def test_standup_start1():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")

    # Create channel ...
    # Assuming channels_create adds the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)

    standup_ret = standup_start(ret['token'], channel_ret['channel_id'], 5)
    # Valid case ...
    assert (standup_ret['time_finish'] - (datetime.now()+timedelta(seconds = 5)).timestamp()) < 1


def test_standup_start2():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")

    # Create channel ...
    # Assuming channels_create doesn't add the user and make them owner by default ...
    invalid_channel_id = 2
    # Invalid cases ...
    with pytest.raises(ValueError, match=r"*"):
        # Channel doesnt exist ...
        standup_start(ret['token'], invalid_channel_id, 5)

def test_standup_start3():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")

    # Create channel ...
    # Assuming channels_create adds the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)
    standup_start(ret['token'], channel_ret['channel_id'], 10)

    # Invalid cases ...
    with pytest.raises(ValueError, match=r"*"):
        # Standup is still active
        standup_start(ret['token'], channel_ret['channel_id'], 10)


def test_standup_start4():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
    ret2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

    # Create channel ...
    # Assuming channels_create doesn't add the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)

    with pytest.raises(AccessError, match=r"*"):
        # User2 is not a member of channel ...
        standup_start(ret2['token'], channel_ret['channel_id'], 5)

def test_standup_send1():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")

    # Create channel ...
    # Assuming channels_create doesn't add the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)

    # Start standup
    standup_start(ret['token'], channel_ret['channel_id'], 5)

    # Valid case ...
    assert standup_send(ret['token'], channel_ret['channel_id'], "A message") == {}

def test_standup_send2():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")

    # Create channel ...
    # Assuming channels_create doesn't add the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)

    # Start standup
    standup_start(ret['token'], channel_ret['channel_id'], 5)

    invalid_channel_id = 2
    # Invalid cases ...
    with pytest.raises(ValueError, match=r"*"):
        # Channel doesnt exist ...
        standup_send(ret['token'], invalid_channel_id, "A message")

def test_standup_send3():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
    ret2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

    # Create channel ...
    # Assuming channels_create doesn't add the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)

    # Start standup
    standup_start(ret['token'], channel_ret['channel_id'], 5)

    with pytest.raises(AccessError, match=r"*"):
        # User2 is not a member of channel ...
        standup_send(ret2['token'], channel_ret['channel_id'], "A message")

def test_standup_send4():
    clear()
    # Create users ...
    ret = auth_register("someemail@gmail.com","securepassword","John","Doe")

    # Create channel ...
    # Assuming channels_create doesn't add the user and make them owner by default ...
    channel_ret = channels_create(ret['token'], "sample", True)

    # Start standup
    standup_start(ret['token'], channel_ret['channel_id'], 5)

    # Invalid cases ...
    with pytest.raises(ValueError, match=r"*"):
        # Channel doesnt exist ...
        standup_send(ret['token'], channel_ret['channel_id'], "a"*1001)


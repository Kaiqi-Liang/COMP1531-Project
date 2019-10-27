''' Local packages '''
from backend.helpers.exception import ValueError, AccessError
from backend.database import *
from backend.standup import *
from backend.auth import *
from backend.channel import *

''' pip3 packages '''
import pytest


def test_standup_start1():
	clear()
	# Create users ...
	ret = auth_register("someemail@gmail.com","securepassword","John","Doe")

	# Create channel ...
	# Assuming channels_create doesn't add the user and make them owner by default ...
	channel_ret = channels_create(ret['token'], "sample", True)

	# Valid case ...
	assert (standup_start(ret['token'], channel_ret['channel_id'])['time_finish'] - (datetime.now()+timedelta(minutes=15)).timestamp()) < 1


def test_standup_start():
	clear()
	# Create users ...
	ret = auth_register("someemail@gmail.com","securepassword","John","Doe")

	# Create channel ...
	# Assuming channels_create doesn't add the user and make them owner by default ...
	channel_ret = channels_create(ret['token'], "sample", True)
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

def test_standup_send1():
	clear()
	# Create users ...
	ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
	# u_id2, token2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

	# Create channel ...
	# Assume channels_create doesn't add the user and make them owner by default ...
	channel_ret = channels_create(ret['token'], "sample", True)

	# Start standup
	standup_start(ret['token'], channel_ret['channel_id'])

	# Valid case ...
	standup_send(ret['token'], channel_ret['channel_id'], "A message")


def test_standup_send2():
	clear()
	# Create users ...
	ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
	# u_id2, token2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

	# Create channel ...
	# Assume channels_create doesn't add the user and make them owner by default ...
	channel_ret = channels_create(ret['token'], "sample", True)

	# Start standup
	standup_start(ret['token'], channel_ret['channel_id'])
	invalid_channel_id = 2
	# Invalid cases ...
	with pytest.raises(ValueError, match=r"*"):
		# Channel doesnt exist ...
		standup_send(channel_ret['channel_id'], invalid_channel_id, "A message")


def test_standup_send3():
	clear()
	# Create users ...
	ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
	# u_id2, token2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

	# Create channel ...
	# Assume channels_create doesn't add the user and make them owner by default ...
	channel_ret = channels_create(ret['token'], "sample", True)

	# Start standup
	standup_start(ret['token'], channel_ret['channel_id'])

	# Invalid cases ...
	with pytest.raises(ValueError, match=r"*"):

		# Message too long ...
		standup_send(ret['token'], channel_ret['channel_id'], "a"*1001)

def test_standup_send4():
	clear()
	# Create users ...
	ret = auth_register("someemail@gmail.com","securepassword","John","Doe")
	ret2 = auth_register("someemail2@gmail.com","securepassword","John","Smith")

	# Create channel ...
	# Assume channels_create doesn't add the user and make them owner by default ...
	channel_ret = channels_create(ret['token'], "sample", True)

	# Start standup
	standup_start(ret['token'], channel_ret['channel_id'])

	with pytest.raises(AccessError, match=r"*"):
		# User2 is not a member of channel ...
		standup_send(ret2['token'], channel_ret['channel_id'], "A message")

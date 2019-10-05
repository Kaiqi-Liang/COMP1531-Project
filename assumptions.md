assumptions:


- assume when message_remove is called the message with message_id is deleted from the messages list 
- assume when a message is edited, the time_created stays to when the message was posted, not edited 
- assume when a message is edited, the user_id remains as the original poster of the message
- assume when the pin/ unpin function is called, the message has been pinned/unpinned, and this variable will later appear in a data structure
- assume all of the messages passed into test_message_unpin are pinned already
- assume all of the messages passed into test_message_pin are not pinned
- assume all of the messages passed into test_message_react have not been reacted to 
- assume al of the messages passed into test_message_unreact have been reacted to 
- assume a not valid message based on message_id means that no message with the id exists (in tests use -1 as an example) 
- assume value of is_unread stays the same if a message is edited 
- assume the messages sent in message_send and message_sendlater are unread for testing 
- assume everytime a pytest function is run the "state" of the program is reset, e.g. message_list is restored to original 
- assume that in later iterations more tests will be added in relation to ensuring the user is in the channel of the message being handled, e.g. in message_react

* assume user names are case sensitive, meaning that 'A' and 'a' are different users
* assume if there is only one member in a channel who is the owner, the channel will not exist if the owner leaves the channel
* assume user created in the fixture is not an admin
* assume user should be able to see the private channels they created
* assume user has to be invited first to be added as an owner
* assume everytime a pytest function is run the "state" of the program is reset i.e. all users are wiped


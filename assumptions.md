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
- assume that I am unable to test access errors in pin and unpin as I cannot access the channel of the message with message_id, this later should become possible throughout implementation (with a beter understanding of structures being used and functions) 
- assume everytime a pytest function is run the "state" of the program is reset, e.g. message_list is restored to original 

# Acceptance Criteria
## As a user I want to be able to create an account using my details so i can access the features of slackr
### As a user I want to have a unique login so that my account is safe from other’s logging in
* Given the user navigated to the login page
* There should be a box for user to enter email and password
* There should be a button for logging in
* When the user enter a valid email and password
* Then the user should be navigated to the home page
* When the user enter a invalid email and password
* Then the system should decline the login action

### As a user I want to be able to logout of slack so I can show that I am no longer active on slack
* When logged in, a logout button should be near the top of the screen
* Given the logout button is pressed and the server logs the user our successfully
* Then the login page will reappear to the user

### As a user I want to be able to change my password so when I forget it I can login back in
* Given a user navigated to the forot password page and enter a valid email
* An email will be sent to the email with a code 6 digits random code
* From this email they can enter a new password for their account, if they have the verification code
* Using this new password, they can log into their account

### As a user I want a safety net when authenticating a change in my password so I can keep my account private
* Given the user navigated to the register page
* There should be a box for user to enter first name, last name, email and password
* There should be a button for signing up
* When a new user registers, the entered password is encoded
* No other user is able to view another user’s password


## As a user I want to be able to operate on channels so that I can better organize tasks into groups
### As an owner of a channel I want to add other users to my channel so that I can show them the messages they are interested in on my channel
* There should be an invite button at the top of the channel button for adding users
* A bar should appear where the user can type the id of the required user to be invited
* The invited user should now be able to send messages to the channel
* If the entered user does not exist, that user will not be invited
 
## As a leader, I want to be able to make other people an owner in that channel so that they can help me organise
* Owner of a channel can see all of the members of a channel
* Should be a button next to the member which, when pressed, can change the users permissions
* When the owner of a channel presses this button, the user is now added as an owner of the channel
* The new owner now has access to more functionalities such as editing and removing messages they did not send
* The new owner is now able to add new owners to that channel as well

### As an owner of a channel I want to be able to remove an owner so that I can prevent some people from adding and removing owners
* A button should appear next to a user that has their permissions
* When an owner presses this button, the user is no longer an owner of the channel
* The user is no longer displayed as an owner of the channel
* The user loses functionality of being an owner

### As a user I want to see the message history so that I can catch up on the messages I missed
* There should be a button at the top of the messages in a channel called previous messages
* Pressing this button causes more messages to appear in the channel
* All members of a channel should be able to do this

### As a user I want to see all the channels I am currently in so that I can switch to the one to look as its messages
* On the side bar, a list labelled, my channels is visible to a user
* By pressing on one of these channels, the user is taken to the channel and is able to view the details of a channel
* The user can also send messages to the channel

### As a user I want to see all the channels in the workspace so that I can choose the ones I want to join
* On the side bar, a list labelled other channels is visible to the user
* By clicking on one of these channels, a user is able to view the messages in the channel
* The user is not yet able to send messages to the channel

### As a member of a channel I want to see all the other members in the channel so that I have an idea who is in it
* At the top of a channel, a list of all users in the channels in visible
* The user can also see the users handles and display photos
* The other users permissions are also visible, i.e. who is an owner

### As a team lead I want to create a channel for my team to that I can have better communication within a team
* On the side bar of the screen, there is a button to create a new channel
* When pressed, a bar opens for the user to enter a name for the new channel
* The user who created the channel is now the owner
* This channel is added to the list of channels under “My channels”
* The owner can now invite people to the channel
* The owner can send and interact with messages on the channel

### As a member of a channel I want to see the name of the channel so that I know which channel I am currently in
* On the side bar, within the lists of my channels, the name of the channel is visible
* When a user has clicked on the channel, and is now viewing the channel messages, the channel name appears at the top of the page

## As a user I want to be able to send and respond to messages so that I can communicate with other users
### As a user I want to be able to schedule messages to send later so I can communicate with my team when I am not able to access my device
* An icon for scheduling appears next to the write message bar
* Scheduling a message to send later starts when the icon has been pressed
* A message and time to send can be filled in
* The message appears in the channel at the time the message was scheduled to upload
* The user can not send a message if it is longer than 1000 characters
* The message will not send if the entered time has already passed

### As a user I want to be able to send messages so I can communicate with other users on the same channel
* There is an area present to type in the message to be sent
* Send button to be able to send the message
* Once the message is sent to a channel, it appears in the channel 
* The message does not send if it is longer than 1000 characters long
* Only members of the channel are able to send a message to that channel

### As a user I want to be able to delete a message sent by other users so I can remove messages with incorrect details
* Bin icon to indicate a message being deleted
* The message is removed once the bin icon has been clicked
* Message no longer appears in the messages of a channel
* Users who are not owners or admins are not able to delete messages they did not send

### As a user I want to edit messages sent by other users in the channel so that I can correct any mistakes in their message
* Pen icon appears next to a message being edited
* When the pen button has been pressed, a placeholder bar appears to enter a new message in
* The new/edited message appears in the log of messages in the channel
* Users who are not owners or admins are not able to edit messages they did not send

### As a user I want to react to messages with a thumbs up (react) so that I can give a short response to a message
* A thumbs up icon appears next to a message
* Pressing the thumbs up indicates a react
* The button changes colour when it has been pressed
* The number of reacts appears next to the icon
* If a user has already reacted, they cannot react again

### As a user I want to be able to be able to remove my reaction from a message if my response to that message changes
* A thumbs up button appears next to a message, with the number of reacts to it
* Pressing the button allows a user to unreact
* The number of reacts decrements when the button has been pressed

### As an admin member I want to be able to pin a message so other users in the channel can easily see important messages
* A pin icon appears next to a message
* Pressing the pin causes it to be pinned
* The pin icon fills in when it has been pinned
* Only admins and owners are able to pin a message

### As an admin member I want to be able to unpin messages so that outdated or irrelevant messages no longer appear as pinned or of high priority
* A pin icon appears next to a message, it is filled in if it has already been pinned
* Pressing the pin causes it to be unpinned
* The pin icon is no longer filled in when it has been unpinned
* Only admins and owners are able to unpin a message


## As a user I want to be able to filter through all of my messages to make it easier to find what I am looking for
### As a user I want to find messages relating to work” - “As a user I want to find messages on a specific topic so I can narrow down my search
* Should be a search bar near the top of the slackr page
* There should be a space to enter the message being searched for
* There should be a button to press to search for the message
* Messages matching the search should appear to the user
* If the desired message appears, the user should be able to click on the message and be guided to the channel in which the message is in

## As a user I want the ability to customise my profile to make my profile seem more personal
### As a user I want to change my profile picture so my coworkers can recognise me when we send texts
* There should be a profile section the user is able to access
* An edit button should appear next to the display photo area
* When this button has been pressed, there is a region to upload a photo
* This photo is cropped to fit into the display area
* When the user exists the upload area, it should appear in the user’s profile section
* Other users see the image next to users name when they send and when they appear as channel owners

### As a user I want to be able to set my name so that my account is tied to real life
* When registering, two boxes should appear, for the user to be able to enter their first and last name
* Once logged in, in the profile section, these entered names should appear in the first and last fields of the users profiles

### As a user I want to be able to set an email address so I can receive updates through email as well as password resets
* When registering, there should be a box to enter the users email address
* If the email is valid, the user should now be able to receive messages from slackr on that account

### As a user I want to be able to set my own handle so that my teammates can recognise me by a short nickname
* here should be a profile section the user is able to access
* In this profile section, an edit button should appear next to the handle area
* When this edit button is pressed, bar appears for the user to enter a new handle / edit their old handle
* Closing this area causes the handle to appear in the handle section of the profile area
* On channels, the users handle now appears as the new handle
* The user and other users see this new handle

### As a user I want to see my profile when I click the icon so that I can see all my personal details and make sure they are correct
* There should be a button to press which takes the user to a section that displays the users details
* In this profile section the user should be able to see the first and last name they have set, the email they registered with, their handle/display name and display photo

## As a user I want the ability to alter user permissions so other users only have access to what is essential for them to carry out their tasks
### As a team leader in projects I want to be able to change user permissions so I can delegate tasks to group members
* There should be a button next to all users, which when pressed changes their permission
* Only owners of slack are able to press this button and change other users permissions
* When pressed, the user now has functionalities of an admin

# COMP1531 Major Project

A video describing this project and the background here can be found here.

## Aims:

* To provide students with hands on experience testing, developing, and maintaining a backend server in python.
* To develop students' problem solving skills in relation to the software development lifecycle.
* Learn to work effectively as part of a team by managing your project, planning, and allocation of responsibilities among the members of your team<
* Gain experience in collaborating through the use of a source control and other associated modern team-based tools.
* Apply appropriate design practices and methodologies in the development of their solution
* Develop an appreciation for product design and an intuition of how a typical customer will use a product.

## Changelog

* 24/09/2019: Clarify that Monday tutes will DEMO iteration 1 in week 5
Nothing here yet
* 24/09/2019:
 * auth_passwordreset_reset has had "password" added to end
 * standup_start has new parameter "channel_id"
 * standup_send has new parameter "channel_id"
 * message_unreact has a new parameter "react_id"
 * message_edit had the order of its two parameters swappd
 * channel_id added to message_send and message_sendlater
* 24/09/2019: Exceptions and descriptions added to interface items
 * admin_userpermission_add and admin_userpermission_remove combined into admin_userpermission_change
* 25/09/2019: channel_messages correct description given 
* 25/09/2019: "Interface pecifications" => "Interface specifications"
* 25/09/2019: Task 2 for iteration 1 better explained
* 26/09/2019: More detail provided for what the "plan" should entail
* 26/09/2019: Instances of InputError changed to ValueError
* 27/09/2019: Reflection markdown file changed to be half to 1 page in size (reducing the burden). Clarified where it fits into the teamwork mark.
* 27/09/2019: Emphasis placed that [this](https://youtu.be/0_jaxpOSoj4) video is the main source you should be deriving user requirements from.
* 27/09/2019: channel_leave had an irrelevant requirement in it that has been removed now ("Email entered does not belong to a user")
* 27/09/2019: auth_logout clarified to do nothing if an invalid token passed in
* 27/09/2019: auth_passwordreset_reset had "Email entered is not a valid email" requirement removed
## Background
* 27/09/2019: user_profile description and parameters clarified and fixed
* 27/09/2019: message_edit and message_remove interface descriptions fixed
* 27/09/2019: user_profile_sethandle, user_profiles_uploadphoto; updated
* 29/09/2019: user_profile_sethandle had error "name_last is more than 50 characters" removed
* 29/09/2019: user_login now has ValueError to be raised if "Password is not correct"
* 29/09/2019: auth_login and auth_register now return a u_id too. This isnt strictly necessary (as we'll see later), but will make testing easier.
* 29/09/2019: message_id added to the message structure (so that lists of messages contain the id of the message)
* 30/09/2019: Pagination explanation added
* 01/10/2019: AccessError clarified
* 01/10/2019: message_remove exceptions clarified
* 01/10/2019: message_edit exceptions clarified

An overview of this background and this project can be found in a short video found [HERE](https://youtu.be/Mzg3UGv3TSw).

To manage the transition from trimesters to hexamesters in 2020, UNSW has established a new focus on building an in-house digital collaboration and communication tool for groups and teams.

Rather than re-invent the wheel, UNSW has decided that it finds the functionality of **<a href="https://slack.com/intl/en-au/">Slack</a>** to be nearly exactly what it needs. For this reason, UNSW has contracted out Rayden Pty Ltd (a small software business run by Rob and Hayden) to build the new product. In UNSW's attempt to connect with the younger and more "hip" generation that fell in love with flickr, Tumblr, etc, they would like to call the new UNSW-based product **slackr**.

Rayden Pty Ltd has sub-contracted two software firms:

* BananaPie Pty Ltd (two software developers, Sally and Bob, who will build the initial web-based GUI)
* YourTeam Pty Ltd (a team of talented misfits completing COMP1531 in 19T3), who will build the backend python server and possibly assist in the GUI later in the project

In summary, UNSW contracts Rayden Pty Ltd, who sub contracts:

* BananaPie (Sally and Bob) for front end work
* YourTeam (you and others) for backend work

Rayden Pty Ltd met with Sally and Bob (the front end development team) 2 weeks ago to brief them on this project. While you are still trying to get up to speed on the requirements of this project, Sally and Bob understand the requirements of the project very well.

Because of this they have already specified a **common interface** for the front end and backend to operate on. This allows both parties to go off and do their own development and testing under the assumption that both parties comply will comply with the common interface. This is the interface **you are required to use**

Beside the information available in the interface that Sally and Bob provided, you have been told (so far) that the features of slackr that UNSW would like to see implemented include:

1. Ability to login, register if not logged in, and log out
2. Ability to reset password if forgotten it
3. Ability to see a list of channels
4. Ability to create a channel, join a channel, invite someone else to a channel, and leave a channel
5. Within a channel, ability to view all messages, view the members of the channel, and the details of the channel
6. Within a channel, ability to send a message now, or to send a message at a specified time in the future
7. Within a channel, ability to edit, remove, pin, unpin, react, or unreact to a message
8. Ability to view user anyone's user profile, and modify a user's own profile (name, email, handle, and profile photo)
9. Ability to search for messages based on a search string
10. Ability to modify a user's admin privileges: (MEMBER, ADMIN, OWNER)
11. Ability to begin a "standup", which is a 15 minute period where users can send messages that at the end of the period will automatically be collated and summarised to all users

To get further information about the requirements, Rayden Pty Ltd has provided a pre-recorded video briefing (with verbal and visual descriptions) of what UNSW would like to see in the Slackr product. This can be found [HERE](https://youtu.be/0_jaxpOSoj4). Hint: **This video should be the main source of information from which you derive your user stories**

## Setup

After your week 2 tutorial, you should know who your team members are. Follow the instructions on the tutorial sheet to ensure your team is registered. You need to do this by **Thursday 9PM in week 2**.

If you registered your team on time, then on Sunday of week 2, you should have access to an individual repository at this URL:

https://gitlab.cse.unsw.edu.au/COMP1531/19T3/team_name

where *team-name* is the name of your group as registered on the course website.

## Progress check-in

During your lab class, in weeks without demonstrations (see below), you and your team will conduct a short stand-up in the presence of your tutor. Each member of the team will briefly state what they have done in the past week, what they intend to do over the next week, and what issues they faced or are currently facing. This is so your tutor, who is acting as a representative of the client, is kept informed of your progress. They will make note of your presence and may ask you to elaborate on the work you've done.

## Iteration 1: Tests and Stories

### Task

In this iteration, you are expected to:

1. Create extensive tests (using pytest) for all of the functions in the agreed upon interface.

    These should all be in files of the formn `*_test.py`. See below for more information.

2. Create user stories driven by your understanding of UNSW's requirements.
    
    We recommend you get familiar with the slack-app (the one we invited you to) in order to understand the mechanics of a slack-like app to provide better articulated user stories. Consider this a form of market research on "similar products" to better understand where UNSW are coming from.

    Each individual story should form its own card on the project task board (this can be found on gitlab). 

3. Write assumptions that you feel you are making in your interpretation of the specification and of the functions provided.

    Write these in markdown in `assumptions.md`.

4. Write a brief 1-page plan highlighting how you will approach the following iteration (the development stage).

    Since iteration 2 is about implementing the interface that has been provided to you already by Sally and Bob, you should be able to make enough sense of the requirements to 1) Estimate the time they take, 2) Break them up into logical buckets, 3) Figure out the order in which you would implement them

    This isn't meant to be overly complicated. It's just to demonstrate that you've had a **thoughtful** guess at how you'd go about developing the functions.

    Write these in markdown in `plan.md`. You may include diagrams, tables or whatever other information you believe conveys your plan.

5. Write a brief half-page to 1-page reflection on how this iteration has gone and how you successfully operated as a well-functioning team.

    Write these in markdown in `reflection.md`.

You are **not** expected to begin developing or completing the actual functions themselves.

The files described above should all be in the root of your repository. If you've not written markdown before (which we assume most of you haven't), it's not necessary to research the format. Markdown is essentially plain text with a few extra features for basic formatting. You can just stick with plain text if you find that easier.

### Tests

It is up to you how you structure your tests, but we do require that you write all of your stubs and tests in the /server/ folder.

Our recommendation is to break all of the functions to test up into 1 or many files (this is a decision for you and your team), and then create test files in the same directory as the files the tests are testing. An example of this has been done with:

* `/server/echo.py`
* `/server/echo_test.py`

Remember that we encourage you to write stub functions for all of the functions we provide. Stub functions are dummy implementations of functions that allow them to be trivially tested. E.G. A stub function for a user to login may always return a dummy auth token "123456". This will allow your tests to successfully compile. It is expected that *some* errors may appear in your tests as you write them that you won't discover until you develop the backend in iteration 2.

You may also wish to create some helper files with extra helper functions if that would assist you writing your tests.

### (More info) User Stories

The scaffold for user stories will be provided in the lecture on Monday 23rd September. Please refer to that lecture for information about the structure of the user stories.

### Submission

This iteration is due to be submitted at 8pm Sunday 6th October (**week 3**). You will then be demonstrating this in your week 4 lab (week 5 for monday tutes). All team members **must** attend this lab session.

To submit, one team member must run this command in the CSE environment:

```sh
1531 submit iteration1
```

This will submit the contents of your repo on GitLab and perform a check to make sure that the files above are present. **Make sure that everything you intend to submit is included in your repo**. User stories should be entered into GitLab on the task board for your project.

### Marking Criteria

|Section|Weighting|Criteria|
|---|---|---|
|Pytests|40%| <ul><li>Demonstrated an understanding of good test **coverage**</li><li>Demonstrated an understanding of the importance of **clarity** on the communication of test purposes</li><li>Demonstrated an understanding of good test **design**</li><li>Tests not under or over engineered</li></ul>|
|Stories|25%|<ul><li>Demonstration of an understanding of a user's needs when using a product</li><li>Clear sense of the coverage needed for requirements (i.e. all reasonable possibilities explored)</li><li>Strong understanding of the granularity in which to express requirements (not too specific, not too broad)</li><li>Demonstration of an understanding of the language typically used when writing user stories</li><li>Demonstration of an understanding of the difference between high-level/epic user stories and their subsequent user story components</li></ul>|
|Assumptions markdown file|10%|<ul><li>Clear and obvious effort and time gone into thinking about possible assumptions that are being made when interpreting the specification</li></ul>|
|Planning markdown file|10%|<ul><li>Communication of plan for development (iteration 2) in a written format</li><li>Communication of plan for development (iteration 2) in a diagramatic format</li><li>Demonstration of understanding of how to anticipate a timeline</li><li>Demonstration of thoughtfullness regarding software tools to assist the team in procuding iteration 2</li></ul>|
|Reflection markdown file + General teamwork performance|15%|Note: Parts of this section is assessed by your tutor implicity/indirectly. The document may only contribute to around one third of this component's marks. No submission is needed for this part. <ul><li>Highlighting the timing and outcome of team meetings</li><li>Demonstration that responsibilities were allocated across team members</li><li>Clear reflection on areas for improvement</li><li>Impression that team has worked together collaboratively</li><li>Impression that team had processes in place to work through disagreements or tension</li><li>Impression that team had a thought out methodology for completing this iteration</li></ul>|

### Advice

* Do NOT attempt to try and write or start a web server. Don't overthink how these functions are meant to connect to a frontend yet. This is for the next iteration. In this iteration you are just focusing on the high level functions that will eventually be used for a web server.
* While we don't encourage you to implement the functions (because the specification may change, and there are no marks for implementation), we do encourage you to sufficiently "stub" out the functions to ensure they're testable and that your python tests can actually compile and run</li>

### Demonstration

When you demonstrate this iteration in your week 4 lab (week 5 for monday tutes), the breakdown will go approximately like this:

* 5 minutes of demonstration of the code you produced
* 5 minutes of demonstration of your stories, assumptions, and plan
* 10 minutes of Q&A from the tutor(s)

## Iteration 2: Servers and Products

Details will be released in week 4

## Iteration 3: Improvements from customer feedback

Details will be released in week 7

## Interface specifications from Sally and Bob

### Data types

|Variable name|Type|
|-------------|----|
|named exactly **email**|string|
|named exactly **id**|integer|
|named exactly **password**|string|
|named exactly **token**|string|
|named exactly **message**|string|
|contains substring **name**|string|
|contains substring **code**|string|
|has prefix **is_**|boolean|
|has prefix **time_**|datetime|
|has suffix **_id**|integer|
|has suffix **_url**|string|
|has suffix **_str**|string|
|has suffix **end**|integer|
|has suffix **start**|integer|
|(outputs only) named exactly **messages**|List of dictionaries, where each dictionary contains types { message_id, u_id, message, time_created, is_unread }|
|(outputs only) named exactly **channels**|List of dictionaries, where each dictionary contains types { id, name }|
|(outputs only) named exactly **members**|List of dictionaries, where each dictionary contains types { u_id, name_first, name_last }|

### Token
Many of these functions (nearly all of them) need to be called from the perspective of a user who is logged in already. When calling these "authorised" functions, we need to know:
1) Which user is calling it
2) That the person who claims they are that user, is actually that user

We could solve this trivially by storing the user ID of the logged in user on the front end, and every time the front end (from Sally and Bob) calls your background, they just sent a user ID. This solves our first problem (1), but doesn't solve our second problem! Because someone could just "hack" the front end and change their user id and then log themselves in as someone else.

To solve this when a user logs in or registers the backend should return a "token" (basically a hash) that the front end will store and pass into most of your functions in future. When these "authorised" functions are called, you can check if a token is valid, and determine the user ID.

There are a few different ways to do this. However, you don't need to decide on a way until Iteration 2. For now you can just ensure the tokens returned from login/register and the same as ones passed into other functions.

### Access Error
The AccessError is not one of Python's built in types. For iteration one, you can either:
 * Just use another error as a placeholder for now
 * Make your own AccessError as per [instructions that we have provided](https://webcms3.cse.unsw.edu.au/COMP1531/19T3/resources/35860)

### Functions

#### Notes:
 * To check a valid email, just use the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method)
 * A valid password must contain at least 5 characters
 * Members in a channel have two permissions.
   1) Owner of the channel (the person who created it, and whoever else that creator adds)
   2) Members of the channel
 * Slackr user's have three permissions
   1) Owners, which have the same privileges as an admin (permission_id 1)
   1) Admins, who have special permissions that members don't (permission_id 2)
   1) Members, who do not have any special permissions (permission_id 3)
 * All slackr members are by default members, except for the very first user who signs up, who is an admin

|Function name|Parameters|Return type|Exception|Description|
|-------------|----------|-----------|-----------|-----------|
|auth_login|(email, password)|{ u_id, token }|**ValueError** when:<ul><li>Email entered is not a valid email</li><li>Email entered does not belong to a user</li><li>Password is not correct</li></ul> | Given a registered users' email and password and generates a valid token for the user to remain authenticated |
|auth_logout|(token)|{}|N/A|Given an active token, invalidates the taken to log the user out. Given a non-valid token, does nothing|
|auth_register|(email, password, name_first, name_last)|{ u_id, token }|**ValueError** when:<ul><li>Email entered is not a valid email.</li><li>Email address is already being used by another user</li><li>Password entered is not a valid password</li><li>name_first is more than 50 characters</li><li>name_last is more than 50 characters</ul>|Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session|
|auth_passwordreset_request|(email)|{}|N/A|Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.|
|auth_passwordreset_reset|(reset_code, new_password)|{}|**ValueError** when:<ul><li>reset_code is not a valid reset code</li><li>Password entered is not a valid password</li>|Given a reset code for a user, set that user's new password to the password provided|
|channel_invite|(token, channel_id, u_id)|{}|**ValueError** when:<ul><li>channel_id does not refer to a valid channel that the authorised user is part of.</li><li>u_id does not refer to a valid user</li></ul>|Invites a user (with user id u_id) to join a channel with ID channel_id. Once invited the user is added to the channel immediately|
|channel_details|(token, channel_id)|{ name, owner_members, all_members }|**ValueError** when:<ul><li>Channel (based on ID) does not exist</li></ul>**AccessError** when<ul><li>Authorised user is not a member of channel with channel_id</li></ul>|Given a Channel with ID channel_id that the authorised user is part of, provide basic details about the channel|
|channel_messages|(token, channel_id, start)|{ messages, start, end }|**ValueError** when:<ul><li>Channel (based on ID) does not exist</li><li>start is greater than the total number of messages in the channel</li></ul>**AccessError** when<ul><li>Authorised user is not a member of channel with channel_id</li></ul>|Given a Channel with ID channel_id that the authorised user is part of, return up to 50 messages between index "start" and "start + 50". Message with index 0 is the most recent message in the channel. This function returns a new index "end" which is the value of "start + 50", or, if this function has returned the least recent messages in the channel, returns -1 in "end" to indicate there are no more messages to load after this return.|
|channel_leave|(token, channel_id)|{}|**ValueError** when:<ul><li>Channel (based on ID) does not exist</li></ul>|Given a channel ID, the user removed as a member of this channel|
|channel_join|(token, channel_id)|{}|**ValueError** when:<ul><li>Channel (based on ID) does not exist</li></ul>**AccessError** when<ul><li>channel_id refers to a channel that is private (when the authorised user is not an admin)</li></ul>|Given a channel_id of a channel that the authorised user can join, adds them to that channel|
|channel_addowner|(token, channel_id, u_id)|{}|**ValueError** when:<ul><li>Channel (based on ID) does not exist</li><li>When user with user id u_id is already an owner of the channel</li></ul>**AccessError** when the authorised user is not an owner of the slackr, or an owner of this channel</li></ul>|Make user with user id u_id an owner of this channel|
|channel_removeowner|(token, channel_id, u_id)|{}|**ValueError** when:<ul><li>Channel (based on ID) does not exist</li><li>When user with user id u_id is not an owner of the channel</li></ul>**AccessError** when the authorised user is not an owner of the slackr, or an owner of this channel</li></ul>|Remove user with user id u_id an owner of this channel|
|channels_list|(token)|{ channels }|N/A|Provide a list of all channels (and their associated details) that the authorised user is part of|
|channels_listall|(token)|{ channels }|N/A|Provide a list of all channels (and their associated details)|
|channels_create|(token, name, is_public)|{ channel_id }|**ValueError** when:<ul><li>Name is more than 20 characters long</li></ul>|Creates a new channel with that name that is either a public or private channel|
|message_sendlater|(token, channel_id, message, time_sent)|{}|**ValueError** when:<ul><li>Channel (based on ID) does not exist</li><li>Message is more than 1000 characters</li><li>Time sent is a time in the past</li></ul>|Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future|
|message_send|(token, channel_id, message)|{}|**ValueError** when:<ul><li>Message is more than 1000 characters</li></ul>|Send a message from authorised_user to the channel specified by channel_id|
|message_remove|(token, message_id)|{}|**ValueError** when:<ul><li>Message (based on ID) no longer exists</li></ul>**AccessError** when all of the following are not true<ul><li>Message with message_id was not sent by the authorised user making this request</li><li>Message with message_id was not sent by an owner of this channel</li><li>Message with message_id was not sent by an admin or owner of the slack</li></ul>|Given a message_id for a message, this message is removed from the channel|
|message_edit|(token, message_id, message)|{}|**ValueError** when all of the following are not true:<ul><li>Message with message_id was not sent by the authorised user making this request</li><li>Message with message_id was not sent by an owner of this channel</li><li>Message with message_id was not sent by an admin or owner of the slack</li></ul>|Given a message, update it's text with new text|
|message_react|(token, message_id, react_id)|{}|**ValueError** when:<ul><li>message_id is not a valid message within a channel that the authorised user has joined</li><li>react_id is not a valid React ID</li><li>Message with ID message_id already contains an active React with ID react_id</li></ul>|Given a message within a channel the authorised user is part of, add a "react" to that particular message|
|message_unreact|(token, message_id, react_id)|{}|**ValueError** when:<ul><li>message_id is not a valid message within a channel that the authorised user has joined</li><li>react_id is not a valid React ID</li><li>Message with ID message_id does not contain an active React with ID react_id</li></ul>|Given a message within a channel the authorised user is part of, remove a "react" to that particular message|
|message_pin|(token, message_id)|{}|**ValueError** when:<ul><li>message_id is not a valid message</li><li>The authorised user is not an admin</li><li>Message with ID message_id is already pinned</li></ul>**AccessError** when<ul><li>The authorised user is not a member of the channel that the message is within</li></ul>|Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend|
|message_unpin|(token, message_id)|{}|**ValueError** when:<ul><li>message_id is not a valid message</li><li>The authorised user is not an admin</li><li>Message with ID message_id is already unpinned</li></ul>**AccessError** when<ul><li>The authorised user is not a member of the channel that the message is within</li></ul>|Given a message within a channel, remove it's mark as unpinned|
|user_profile|(token, u_id)|{ email, name_first, name_last, handle_str }|**ValueError** when:<ul><li>User with u_id is not a valid user</li></ul>|For a valid user, returns information about their email, first name, last name, and handle|
|user_profile_setname|(token, name_first, name_last)|{}|**ValueError** when:<ul><li>name_first is more than 50 characters</li><li>name_last is more than 50 characters</ul></ul>|Update the authorised user's first and last name|
|user_profile_setemail|(token, email)|{}|**ValueError** when:<ul><li>Email entered is not a valid email.</li><li>Email address is already being used by another user</li>|Update the authorised user's email address|
|user_profile_sethandle|(token, handle_str)|{}|**ValueError** when:<ul><li>handle_str is no more than 20 characters</li></ul>|Update the authorised user's handle (i.e. display name)|
|user_profiles_uploadphoto|(token, img_url, x_start, y_start, x_end, y_end)|{}|**ValueError** when:<ul><li>img_url is returns an HTTP status other than 200.</li><li>x_start, y_start, x_end, y_end are all within the dimensions of the image at the URL.</li></ul>|Given a URL of an image on the internet, crops the image within bounds (x_start, y_start) and (x_end, y_end). Position (0,0) is the top left.|
|standup_start|(token, channel_id)|{ time_finish }|**ValueError** when:<ul><li>Channel (based on ID) does not exist</li></ul>**AccessError** when<ul><li>The authorised user is not a member of the channel that the message is within</li></ul>|For a given channel, start the standup period whereby for the next 15 minutes if someone calls "standup_send" with a message, it is buffered during the 15 minute window then at the end of the 15 minute window a message will be added to the message queue in the channel from the user who started the standup. |
|standup_send|(token, channel_id, message)|{}|**ValueError** when:<ul><li>Channel (based on ID) does not exist</li><li>Message is more than 1000 characters</li></ul>**AccessError** when<ul><li>The authorised user is not a member of the channel that the message is within</li><li>If the standup time has stopped</li></ul>|Sending a message to get buffered in the standup queue, assuming a standup is currently active|
|search|(token, query_str)|{ messages }|N/A|Given a query string, return a collection of messages that match the query|
|admin_userpermission_change|(token, u_id, permission_id)|{}|**ValueError** when:<ul><li>u_id does not refer to a valid user<li>permission_id does not refer to a value permission</li></ul>**AccessError** when<ul><li>The authorised user is not an admin or owner</li></ul>|Given a User by their user ID, set their permissions to new permissions described by permission_id|

### Pagination
The behaviour in which channel_messages returns data is called **pagination**. It's a commonly used method when it comes to getting theoretially unbounded amounts of data from a server to display on a page in chunks. Most of the timelines you know and love - Facebook, Instagram, LinkedIn - do this.

For example, if we imagine a user with token "12345" is trying to read messages from channel with ID 6, and this channel has 124 messages in it, 3 calls from the client to the server would be made. These calls, and their corresponding return values would be:
 * channel_messages("12345", 6, 0) => { [messages], 0, 49 }
 * channel_messages("12345", 6, 50) => { [messages], 50, 99 }
 * channel_messages("12345", 6, 100) => { [messages], 100, -1 }

## Due Dates and Weightings

|Iteration|Code and report due                  |Demonstration to tutor(s)      |Assessment weighting of project (%)|
|---------|-------------------------------------|-------------------------------|-----------------------------------|
|   1     |8pm Sunday 6th October (**week 3**)  |In YOUR **week 4** laboratory (week 5 for monday tutes)  |30%                                |
|   2     |8pm Sunday 27th October (**week 6**) |In YOUR **week 7** laboratory  |40%                                |
|   3     |8pm Sunday 17th November (**week 9**)|In YOUR **week 10** laboratory |30%                                |

## Expectations

While it is up to you as a team to decide how work is distributed between you, for the purpose of assessment there are certain key criteria all members must.

* Code contribution
* Documentation contribution
* Usage of git/GitLab
* Attendance
* Peer assessment
* Academic conduct

The details of each of these is below.

While, in general, all team members will receive the same mark (a sum of the marks for each iteration), **if you as an individual fail to meet these criteria your final project mark may be scaled down**, most likely quite significantly.

### Code contribution

All team members must contribute code to the project. Tutors will assess the degree to which you have contributed by looking at your **git history** and analysing lines of code, number of commits, timing of commits, etc. If you contribute significantly less code than your team members, your work will be closely examined to determine what scaling needs to be applied.

### Documentation contribution

All team members must contribute documentation to the project. Tutors will assess the degree to which you have contributed by looking at your **git history** but also **asking questions** (essentially interviewing you) during your demonstration.

Note that, **contributing more documentation is not a substitute for not contributing code**.

### Peer Assessment

You will be required to complete a form in week 10 where you rate each team member's contribution to the project and leave any comments you have about them. Information on how you can access this form will be released closer to Week 10. Your other team members will **not** be able to see how you rated them or what comments you left.

If your team members give you a less than satisfactory rating, your contribution will be scrutinised and you may find your final mark scaled down.

### Attendance

It is generally assumed that all team members will be present at the demonstrations and at weekly check-ins. If you're absent for more than 80% of the weekly check-ins or any of the demonstrations, your mark may be scaled down.

If, due to exceptional circumstances, you are unable to attend your lab for a demonstration, inform your tutor as soon as you can so they can record your absence as planned.

### Plagiarism

The work you and your group submit must be your own work. Submission of work partially or completely derived from any other person or jointly written with any other person is not permitted. The penalties for such an offence may include negative marks, automatic failure of the course and possibly other academic discipline. Assignment submissions will be examined both automatically and manually for such submissions.

Relevant scholarship authorities will be informed if students holding scholarships are involved in an incident of plagiarism or other misconduct.

Do not provide or show your project work to any other person, except for your group and the teaching staff of COMP1531. If you knowingly provide or show your assignment work to another person for any reason, and work derived from it is submitted you may be penalized, even if the work was submitted without your knowledge or consent. This may apply even if your work is submitted by a third party unknown to you.

Note, you will not be penalized if your work has the potential to be taken without your consent or knowledge.

# COMP1531 Major Project

A video describing this project and the background here can be found here.

## Aims:

* To provide students with hands on experience testing, developing, and maintaining a backend server in python.
* To develop students' problem solving skills in relation to the software development lifecycle.
* Learn to work effectively as part of a team by managing your project, planning, and allocation of responsibilities among the members of your team<
* Gain experience in collaborating through the use of a source control and other associated modern team-based tools.
* Apply appropriate design practices and methodologies in the development of their solution
* Develop an appreciation for product design and an intuition of how a typical customer will use a product.

## Changelog (cleared 5th October in git hash "84cc5a9099")


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

**COMPLETED**

## Iteration 2: Servers and Products

### Task

In this iteration, you are expected to:

1. Implement the backend interface functions, including storage of the data, and wrap them in a flask webserver

2. Provide assurances that your backend implementation is fit for purpose. Consider both verification and validation when doing this. This will, at a minimum, require acceptance criteria for your user stories.

    Briefly describe the strategies you followed and tools you used to achieve this in `assurance.md`.

3. Track your progress via the task board on GitLab.

4. Reflect on your use of agile practices and how you worked as a team.

    Your reflection should, at a minimum, include:
      * How often you met, and why you met that often
      * What methods you used to ensure that meetings were successful
      * What steps you took when things did not go to plan during iteration to
      * Details on how you had multiple people working on the same code 

    Write this in `teamwork.md`.

### Submission

This iteration is due to be submitted at 8pm Sunday 27th October (**week 6**). You will then be demonstrating this in your week 7 lab (week 8 for monday tutes). All team members **must** attend this lab session.

To submit, one team member must run this command in the CSE environment:

```sh
1531 submit iteration2
```

Only one team member is required to submit for the entire groups submission to be recorded. **Make sure that everything you intend to submit is included in your repo**.

When you submit, the following commands will be executed in the root of your repo. It is up to you how you choose to use the results of these commands, but you will need to confirm your submission if any of them fail.

* `python3-coverage run --branch --source=server -m pytest`

    Runs pytest over all python files in `server` and collects coverage information.

* `python3-coverage report`

    Generates a simple report based on the above test run.

* `pylint3 server/*`

    Runs pylint over the all files in `server`.

### Running the server

Open a terminal, and in your project directory run:

`python3 server.py`

This will begin a very simple server. To play around with this server, in another terminal, you can run the following commands to make a GET request and get a response:

`curl 'http://127.0.0.1:5000/echo/get?echo=helloworld`

`curl -d "echo=helloworld" -X POST 'http://127.0.0.1:5000/echo/post'`

More information about running this server will be provided in week 4.

### Storage of data

As you know, in this iteration you will have to store data to implement the backend. This will be discussed in week 5/6 lectures, but in the meantime, you can simply use a single global variable containing nested dictionaries/lists to store the data.

### Connecting to the frontend

Details concerning the front-end will be released in week 5.

### Marking Criteria

|Section|Weighting|Criteria|
|---|---|---|
|Implementation|50%|<ul><li>All interface functions are implemented correctly based on the specification</li><li>Backend tested and working with frontend provided</li><li>Appropriate data structures are used to store application state.</li><li>The flask wrapper for the interface is complete and functional.</li></ul>|
|Assurance|25%|<ul><li>Demonstration of an understanding of the need for software verification and validation</li><li>Development of appropriate acceptance criteria based on user stories and requirements.</li><li>Demonstration of appropriate tool usage for assurance (code coverage, linting, etc.)</li></ul>|
|Teamwork|25%|<ul><li>Consistent work towards the goal of a working backend.</li><li>Task board is always up to date and reflects ongoing work</li><li>Demonstration of appropriate use of agile practices to work effectively as a team.</li></ul>|

### Demonstration

When you demonstrate this iteration, the breakdown will go approximately like this:

* 5 minutes of presenting your code, tests, and how it integrates with the provided front-end
* 10 minutes of Q&A from the tutor(s), including questions about how your team worked as a group

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
|(outputs only) named exactly **messages**|List of dictionaries, where each dictionary contains types { message_id, u_id, message, time_created, is_unread, reacts, is_pinned,  }|
|(outputs only) named exactly **reacts**|List of dictionaries, where each dictionary contains types { react_id, u_ids, is_this_user_reacted } where react_id is the id of a react, and u_ids is a list of user id's of people who've reacted for that react. is_this_user_reacted is whether or not the authorised user has been one of the reacts to this post |
|(outputs only) named exactly **channels**|List of dictionaries, where each dictionary contains types { channel_id, name }|
|(outputs only) named exactly **members**|List of dictionaries, where each dictionary contains types { u_id, name_first, name_last }|

### Token
Many of these functions (nearly all of them) need to be called from the perspective of a user who is logged in already. When calling these "authorised" functions, we need to know:
1) Which user is calling it
2) That the person who claims they are that user, is actually that user

We could solve this trivially by storing the user ID of the logged in user on the front end, and every time the front end (from Sally and Bob) calls your background, they just sent a user ID. This solves our first problem (1), but doesn't solve our second problem! Because someone could just "hack" the front end and change their user id and then log themselves in as someone else.

To solve this when a user logs in or registers the backend should return a "token" (an authorisation hash) that the front end will store and pass into most of your functions in future. When these "authorised" functions are called, you can check if a token is valid, and determine the user ID.

The details of how to deal with this authroisation will be covered in week 5.

### Access Error
The AccessError is not one of Python's built in types. For iteration one, you can either:
 * Just use another error as a placeholder for now
 * Make your own AccessError as per [instructions that we have provided](https://webcms3.cse.unsw.edu.au/COMP1531/19T3/resources/35860)

### Permissions:
 * Members in a channel have two permissions.
   1) Owner of the channel (the person who created it, and whoever else that creator adds)
   2) Members of the channel
 * Slackr user's have three permissions
   1) Owners, which have the same privileges as an admin (permission_id 1).
   2) Admins, who have special permissions that members don't (permission_id 2)
     * Admins have the same capabilities as owners, except that admins cannot change owner's permissions
   3) Members, who do not have any special permissions (permission_id 3)
 * All slackr members are by default members, except for the very first user who signs up, who is an owner

### Interface

|HTTP Request|Endpoint name|Parameters|Return type|Exception|Description|
|------------|-------------|----------|-----------|---------|-----------|
|POST|echo/post|(echo)|{echo}||Returns the input|
|GET|echo/get|(echo)|{echo}||Returns the input|
|POST|auth/login|(email, password)|{ u_id, token }|**ValueError** when:<ul><li>Email entered is not a valid email using the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method)</li><li>Email entered does not belong to a user</li><li>Password is not correct</li></ul> | Given a registered users' email and password and generates a valid token for the user to remain authenticated |
|POST|auth/logout|(token)|{ is_success }|N/A|Given an active token, invalidates the taken to log the user out. If a valid token is given, and the user is successfully logged out, it returns true, otherwise false. |
|POST|auth/register|(email, password, name_first, name_last)|{ u_id, token }|**ValueError** when:<ul><li>Email entered is not a valid email using the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method).</li><li>Email address is already being used by another user</li><li>Password entered is less than 6 characters long</li><li>name_first is between 1 and 50 characters</li><li>name_last is between 1 and 50 characters</ul>|Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session. A handle is generated that is the concatentation of a lowercase-only first name and last name. If the handle is already taken, a number is added to the end of the handle to make it unique. |
|POST|auth/passwordreset/request|(email)|{}|N/A|Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.|
|POST|auth/passwordreset/reset|(reset_code, new_password)|{}|**ValueError** when:<ul><li>reset_code is not a valid reset code</li><li>Password entered is not a valid password</li>|Given a reset code for a user, set that user's new password to the password provided|
|POST|channel/invite|(token, channel_id, u_id)|{}|**ValueError** when:<ul><li>channel_id does not refer to a valid channel that the authorised user is part of.</li><li>u_id does not refer to a valid user</li></ul>**AccessError** when<ul><li>the authorised user is not already a member of the channel</li>|Invites a user (with user id u_id) to join a channel with ID channel_id. Once invited the user is added to the channel immediately|
|GET|channel/details|(token, channel_id)|{ name, owner_members, all_members }|**ValueError** when:<ul><li>Channel ID is not a valid channel</li></ul>**AccessError** when<ul><li>Authorised user is not a member of channel with channel_id</li></ul>|Given a Channel with ID channel_id that the authorised user is part of, provide basic details about the channel|
|GET|channel/messages|(token, channel_id, start)|{ messages, start, end }|**ValueError** when:<ul><li>Channel ID is not a valid channel</li><li>start is greater than or equal to the total number of messages in the channel</li></ul>**AccessError** when<ul><li>Authorised user is not a member of channel with channel_id</li></ul>|Given a Channel with ID channel_id that the authorised user is part of, return up to 50 messages between index "start" and "start + 50". Message with index 0 is the most recent message in the channel. This function returns a new index "end" which is the value of "start + 50", or, if this function has returned the least recent messages in the channel, returns -1 in "end" to indicate there are no more messages to load after this return.|
|POST|channel/leave|(token, channel_id)|{}|**ValueError** when:<ul><li>Channel ID is not a valid channel</li></ul>|Given a channel ID, the user removed as a member of this channel|
|POST|channel/join|(token, channel_id)|{}|**ValueError** when:<ul><li>Channel ID is not a valid channel</li></ul>**AccessError** when<ul><li>channel_id refers to a channel that is private (when the authorised user is not an admin)</li></ul>|Given a channel_id of a channel that the authorised user can join, adds them to that channel|
|POST|channel/addowner|(token, channel_id, u_id)|{}|**ValueError** when:<ul><li>Channel ID is not a valid channel</li><li>When user with user id u_id is already an owner of the channel</li></ul>**AccessError** when the authorised user is not an owner of the slackr, or an owner of this channel</li></ul>|Make user with user id u_id an owner of this channel|
|POST|channel/removeowner|(token, channel_id, u_id)|{}|**ValueError** when:<ul><li>Channel ID is not a valid channel</li><li>When user with user id u_id is not an owner of the channel</li></ul>**AccessError** when the authorised user is not an owner of the slackr, or an owner of this channel</li></ul>|Remove user with user id u_id an owner of this channel|
|GET|channels/list|(token)|{ channels }|N/A|Provide a list of all channels (and their associated details) that the authorised user is part of|
|GET|channels/listall|(token)|{ channels }|N/A|Provide a list of all channels (and their associated details)|
|POST|channels/create|(token, name, is_public)|{ channel_id }|**ValueError** when:<ul><li>Name is more than 20 characters long</li></ul>|Creates a new channel with that name that is either a public or private channel|
|POST|message/sendlater|(token, channel_id, message, time_sent)|{ message_id }|**ValueError** when:<ul><li>Channel ID is not a valid channel</li><li>Message is more than 1000 characters</li><li>Time sent is a time in the past</li></ul>**AccessError** when: <li> the authorised user has not joined the channel they are trying to post to</li></ul>|Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future|
|POST|message/send|(token, channel_id, message)|{ message_id }|**ValueError** when:<ul><li>Message is more than 1000 characters</li></ul>**AccessError** when: <li> the authorised user has not joined the channel they are trying to post to</li></ul>|Send a message from authorised_user to the channel specified by channel_id|
|DELETE|message/remove|(token, message_id)|{}|**ValueError** when:<ul><li>Message (based on ID) no longer exists</li></ul>**AccessError** when none of the following are true:<ul><li>Message with message_id was sent by the authorised user making this request</li><li>The authorised user is an admin or owner of this channel or the slackr</li></ul>|Given a message_id for a message, this message is removed from the channel|
|PUT|message/edit|(token, message_id, message)|{}|**AccessError** when none of the following are true:<ul><li>Message with message_id was sent by the authorised user making this request</li><li>The authorised user is an admin or owner of this channel or the slackr</li></ul>|Given a message, update it's text with new text|
|POST|message/react|(token, message_id, react_id)|{}|**ValueError** when:<ul><li>message_id is not a valid message within a channel that the authorised user has joined</li><li>react_id is not a valid React ID</li><li>Message with ID message_id already contains an active React with ID react_id</li></ul>|Given a message within a channel the authorised user is part of, add a "react" to that particular message|
|POST|message/unreact|(token, message_id, react_id)|{}|**ValueError** when:<ul><li>message_id is not a valid message within a channel that the authorised user has joined</li><li>react_id is not a valid React ID</li><li>Message with ID message_id does not contain an active React with ID react_id</li></ul>|Given a message within a channel the authorised user is part of, remove a "react" to that particular message|
|POST|message/pin|(token, message_id)|{}|**ValueError** when:<ul><li>message_id is not a valid message</li><li>The authorised user is not an admin</li><li>Message with ID message_id is already pinned</li></ul>**AccessError** when<ul><li>The authorised user is not a member of the channel that the message is within</li></ul>|Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend|
|POST|message/unpin|(token, message_id)|{}|**ValueError** when:<ul><li>message_id is not a valid message</li><li>The authorised user is not an admin</li><li>Message with ID message_id is already unpinned</li></ul>**AccessError** when<ul><li>The authorised user is not a member of the channel that the message is within</li></ul>|Given a message within a channel, remove it's mark as unpinned|
|GET|user/profile|(token, u_id)|{ email, name_first, name_last, handle_str }|**ValueError** when:<ul><li>User with u_id is not a valid user</li></ul>|For a valid user, returns information about their email, first name, last name, and handle|
|PUT|user/profile/setname|(token, name_first, name_last)|{}|**ValueError** when:<ul><li>name_first is between 1 and 50 characters</li><li>name_last is between 1 and 50 characters</ul></ul>|Update the authorised user's first and last name|
|PUT|user/profile/setemail|(token, email)|{}|**ValueError** when:<ul><li>Email entered is not a valid email using the method provided [here](https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/) (unless you feel you have a better method).</li><li>Email address is already being used by another user</li>|Update the authorised user's email address|
|PUT|user/profile/sethandle|(token, handle_str)|{}|**ValueError** when:<ul><li>handle_str must be between 3 and 20 characters</li><li>handle is already used by another user</li></ul>|Update the authorised user's handle (i.e. display name)|
|POST|user/profiles/uploadphoto|(token, img_url, x_start, y_start, x_end, y_end)|{}|**ValueError** when:<ul><li>img_url is returns an HTTP status other than 200.</li><li>any of x_start, y_start, x_end, y_end are not within the dimensions of the image at the URL.</li></ul>|Given a URL of an image on the internet, crops the image within bounds (x_start, y_start) and (x_end, y_end). Position (0,0) is the top left.|
|POST|standup/start|(token, channel_id)|{ time_finish }|**ValueError** when:<ul><li>Channel ID is not a valid channel</li></ul>**AccessError** when<ul><li>The authorised user is not a member of the channel that the message is within</li></ul>|For a given channel, start the standup period whereby for the next 15 minutes if someone calls "standup_send" with a message, it is buffered during the 15 minute window then at the end of the 15 minute window a message will be added to the message queue in the channel from the user who started the standup. |
|POST|standup/send|(token, channel_id, message)|{}|**ValueError** when:<ul><li>Channel ID is not a valid channel</li><li>Message is more than 1000 characters</li><li>An active standup is currently running in this channel</li></ul>**AccessError** when<ul><li>The authorised user is not a member of the channel that the message is within</li><li>If the standup time has stopped</li></ul>|Sending a message to get buffered in the standup queue, assuming a standup is currently active|
|GET|search|(token, query_str)|{ messages }|N/A|Given a query string, return a collection of messages that match the query|
|POST|admin/userpermission/change|(token, u_id, permission_id)|{}|**ValueError** when:<ul><li>u_id does not refer to a valid user<li>permission_id does not refer to a value permission</li></ul>**AccessError** when<ul><li>The authorised user is not an admin or owner</li></ul>|Given a User by their user ID, set their permissions to new permissions described by permission_id|

### Errors for all functions

#### AccessError
  * For all functions except auth_register, auth_login
  * Error thrown when token passed in is not a valid token

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

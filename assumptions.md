* assume user names are case sensitive, meaning that 'A' and 'a' are different users
* assume if there is only one member in a channel who is the owner, the channel will not exist if the owner leaves the channel
* assume user created in the fixture is not an admin
* assume user should be able to see the private channels they created
* assume user has to be invited first to be added as an owner
* assume everytime a pytest function is run the "state" of the program is reset i.e. all users are wiped

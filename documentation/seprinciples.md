# Software engineering principles
Throughout iteration 3, our team has focused on implementing software principles to make our code for Slackr not only more maintainable but also understandable, testable and reusable.

Our group has largely focused on reducing repetition in our code and so complying with the DRY (don’t repeat yourself) principle. This has involved creating many auxiliary functions in both our database file and helpers folder. In the database file we have added functions that relate to getting dictionaries from id’s such as in get_channel() and get_message(). In the helpers folder we have abstracted other parts of the code such as:
* Token.py contains functions relating to generating and decoding tokens
* Helpers.py contains different types of functions that are contain functionality that is required in various components of the backend such as is_owner(), which determines if the authorised user is the owner of a channel
* Exception.py holds the Value Error and Access Error we use in raising exceptions

From iteration 2 we had created many of the necessary auxiliary functions in the aforementioned files. Throughout iteration 3 we have then been adding to these functions, by ensuring that they are easily readable by adding more extensive comments and ensuring the logic of the functions are up to date with any changes made in other files.
Some of the changes made to previously created functions include:
* Changing variable names in multiple functions (such as changing user_id to u_id) to improve the readability of our code
* Adding a profile_img_url key to the dictionary for a user in database.py
* Removing the check_permission() function from helper.py and instead refactoring our code to only use the get_permission() function in database.py to reduce unnecessary repetition
Additional functions that we have created in iteration 3 include:
* get_message_channel(): this function takes a message id and returns the channel it is part of. Creating this function allows reducing repetition of code as it is required in many of the functions relating to messages
* crop_image(): this function is used in user_profiles_uploadphoto(). By abstracting this function, the uploadphoto function remains easily readable. Moreover the single responsibility principle is being complied to as the function is then only responsible for one functionality

Overall our reason for abstracting these functions has been to reduce repetition with our code. This firstly allows our code to be maintainable as a change to logic in one of these functions will then be implemented throughout our backend. Secondly our code is then more understandable as the auxiliary functions have clear names that identify their functionality.

Alongside creating helper functions to follow DRY we have also been creating and using them to follow the Single Responsibility Principle (each function only has one job). This has then allowed functions to be more readable and modular. By improving the modularity of our code it is in turn more maintainable.As well as the aforementioned changes we have also focused on keeping our code simple (KISS principle) this allows for more understandable code. Some of the changes made to comply with KISS include:

As well as the aforementioned changes we have also focused on keeping our code simple (KISS principle) this allows for more understandable code. Some of the changes made to comply with KISS include:
* Ensuring that names of additional functions are clear and highlight their responsibility
* Reduced coupling by making all file imports function specific → this ensures bugs are easier to find and identify and reduces the interdependence between components
* In channel_messges() have changed if/else statements to one line conditional expressions to improve simplicity. Have also used more built in functions to improve functionality
By complying with the KISS principle our code is more readable and also more easily maintainable. 

An additional principle we have considered when refactoring and designing our code has been to follow top-down thinking. Whilst the bulk of this was done during iteration 2 and was outlined in the spec (i.e. the breakdown of building Slackr was already divided into subproblems of the individual functions) we have still managed to extend top-down thinking in our work. This has meant complying with the “You aren’t gonna need it” principle. This has meant that as we each work on our backend, we have only built additional auxiliary functions when we find that our logic when solving these problems requires it. Particularly in iteration 3 this has guided the building of user_profiles_uploadphoto() as the auxiliary function, crop_image() in helpers.py was only created after it was identified as necessary to build.
By only implementing functionality when it is required it has improved our efficiency when writing our program and also saves time.

Finally we have also designed and refractored our code whilst incorporating encapsulation. In our program this has meant restricting direct access to the persistent data in the DATA dictionary. Instead of directly accessing the dictionary we have created functions in database.py that, through the get_data() function, access and return the required data needed in our backend. Some of these functions include:
* get_user(): given a u_id returns the dictionary for that user
* get_message(): given a message_id for a message returns the dictionary for that message
* get_channel(): given a channel_id returns the dictionary for the channel

Our group has implemented encapsulation in order to allow access to the data level without revealing the complex arrangement of the data. Moreover it simplifies the maintenance of the program as changes to accessing data now only has to occur in these functions in database.py Finally it makes code in our backend files easier to understand as we have abstracted the logic required to access the DATA dictionary.

Thus our team has worked hard in iteration 3 and by extension the whole assignment to focus on complying with the KISS, DRY, YAGNI principles as well as encapsulation to ensure our code is maintainable, readable and testable.

""" Global variable to store the database """
import json
from threading import Timer
DATA = {
    'user': [],
    'channel': [],
    'slackr': {
                'admin':[],
                'owner':[],
                'member':[]
        }
}

'''
DATA = {
    'user':
        [
            {
                'u_id': u_id,
                'email': 'email',
                'password': hash,
                'name_first': 'first',
                'name_last': 'last',
                'handle_str': 'firstlast',
                'permission_id': p_id,
                'tokens': ['token'],
                'reset': '',
                'profile_img_url': 'profile_img_url'
            }
        ],
    'channel':
        [
            {
                'channel_id': channel_id,
                'name': 'name',
                'is_public': True,
                'owners': [
                                {
                                    'u_id': u_id,
                                    'name_first': 'first',
                                    'name_last': 'last'
                                }
                          ],
                'members': [
                                {
                                    'u_id': u_id,
                                    'name_first': 'first',
                                    'name_last': 'last',
                                    'profile_img_url': 'profile_img_url'
                                }
                          ],
                'messages': [
                                {
                                    'message_id': message_id,
                                    'u_id': u_id,
                                    'message': 'message',
                                    'time_created': time,
                                    'reacts': [
                                                  {
                                                       'react_id': 1,
                                                       'u_ids, [u_id],
                                                       'is_this_user_reacted': True
                                                  }
                                              ],
                                    'is_pinned': True
                                }
                            ],
                'standup_queue': standup_message
            }
        ],
    'slackr':
        [
            {
                'owner': [u_id],
                'admin': [u_id],
                'member': [u_id]
            }
        ]
'''

def get_data():
    """ get global variable i.e. database """
    global DATA
    return DATA

def get_user(u_id):
    """ Given a user id return user dict """
    for user in get_data()['user']:
        if int(u_id) == user['u_id']:
            return user
    return None

def get_channel(channel_id):
    """ Given a channel id return channel dict """
    for channel in get_data()['channel']:
        if int(channel_id) == channel['channel_id']:
            return channel
    return None

def get_message(message_id):
    """ Return message dict """
    for channel in get_data()['channel']:
        for message in channel['messages']:
            if int(message_id) == message['message_id']:
                return message
    return None

def get_permission(user_id):
    """ Get user permission_id """
    for user in get_data()['user']:
        if int(user_id) == user['u_id']:
            return user['permission_id']
    return None

def get_message_channel(message_id):
    """ Return the channel dict that the message is in """
    for channel in get_data()['channel']:
        for message in channel['messages']:
            if int(message_id) == message['message_id']:
                return channel
    return None

def clear():
    """ Clear the database """
    global DATA
    DATA = {'user': [],
            'channel': [],
            'slackr': {
                'admin':[],
                'owner':[],
                'member':[]
                }
            }

def save():
    """ Export DATA to a json file every second """
    timer = Timer(1, save)
    timer.start()
    global DATA
    with open('export.json', 'w') as file:
        json.dump(DATA, file)

def load():
    """ Load the json file to the database """
    global DATA
    with open('export.json', 'r') as file:
        DATA = json.load(file)

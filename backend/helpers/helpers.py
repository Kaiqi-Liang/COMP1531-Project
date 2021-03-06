""" Helper functions """
import re
from PIL import Image
from backend.database import get_data
from backend.helpers.exception import ValueError

def check_email(email):
    """ Check if an email is valid """
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' # regex for email address
    if re.search(email_regex, email):
        return True
    return False


def check_user_in_channel(u_id, channel):
    """ Check if a user is in a channel """
    for member in channel['members']:
        if int(u_id) == member['u_id']:
            return True
    return False


def is_owner(u_id, channel):
    """ Check if a user is an owner of a channel """
    for owner in channel['owners']:
        if int(u_id) == owner['u_id']:
            return True
    return False


def get_message_channel(message_id):
    """ Get the channel that the given message is in """
    for channel in get_data()['channel']:
        for message in channel['messages']:
            if int(message_id) == message['message_id']:
                return channel
    return None


def crop_image(photo, x_start, y_start, x_end, y_end):
    """ crop a given image in the file system with given dimensions """
    image = Image.open(photo)
    width, height = image.size
    if x_start == x_end or y_start == y_end:
        raise ValueError("Invalid crop size!")
    if x_start >= width or x_start < 0 or x_end >= width or x_end < 0:
        raise ValueError("Invalid width crop!")
    if y_start >= height or y_start < 0 or y_end >= height or y_end < 0:
        raise ValueError("Invalid height crop!")

    return image.crop((x_start, y_start, x_end, y_end))

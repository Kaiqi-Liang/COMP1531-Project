''' Search function '''
from backend.database import get_data, get_permission
from backend.helpers.token import get_user_from_token
from backend.helpers.helpers import check_user_in_channel

def search(token, query_str):
    messages = []
    u_id = get_user_from_token(token)
    for channel in get_data()['channel']:
        if check_user_in_channel(u_id, channel) or get_permission(u_id) in [1, 2]:
            # search channel messages that match query string
            for message in channel['messages']:
                if query_str in message['message']:
                    messages.append(message)
    return {'messages': messages}

# Check if user is in channel ...
def check_in_channel(token, channel_id):
    channels = channels_list(token)
    for channel in channels:
        if channel[id] == channel_id:
            return True
    return False

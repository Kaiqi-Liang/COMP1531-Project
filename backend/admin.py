""" Admin functions """
from backend.database import get_data, get_user
from backend.helpers.token import get_user_from_token
from backend.helpers.exception import ValueError, AccessError

# after permission change to admin or owner they need to be added to every single channel as an owner

def admin_userpermission_change(token, u_id, permission_id):
    slackr = get_data()["slackr"]
    try:
        u_id = int(u_id)
    except:
        raise ValueError("u_id does not refer to a valid user")
    permission_id = int(permission_id)

    user1 = get_user(get_user_from_token(token))
    user2 = get_user(u_id)
    if permission_id > 3 or permission_id < 1:
        raise ValueError("permission_id not valid")
    if user2 is None:
        raise ValueError("u_id does not refer to a valid user")

    # if user2's permission is the same as permission_id
    if user2['permission_id'] == permission_id:
        return {}

    # if user1 is the owner of the slackr
    if user1["permission_id"] == 1:
        # user1 cannot remove themselves if they are the only owner ...
        if len(slackr['admin']) == 1 and user2 == user1:
            return {}
        # since user1 can change permissions of everyone ...
        try:
            slackr['owner'].remove(user2['u_id'])
        except:
            raise ValueError
        try:
            slackr['admin'].remove(user2['u_id'])
        except:
            raise ValueError

        user2["permission_id"] = permission_id
        if user2["permission_id"] <= 2:
            slackr['admin'].append(user2['u_id'])
            if user2["permission_id"] == 1:
                slackr['owner'].append(user2['u_id'])

    # if user1 is an admin of the slackr
    elif user1["permission_id"] == 2:
        # if user2 is an owner of the slackr, user1 cannot change
        if user2["permission_id"] == 1 or permission_id == 1:
            raise AccessError("The authorised user is not an owner")

        try:
            slackr['admin'].remove(user2['u_id'])
        except:
            raise ValueError

        user2["permission_id"] = permission_id
        if user2["permission_id"] <= 3:
            slackr['member'].append(user2['u_id'])
            if user2["permission_id"] == 2:
                slackr['admin'].append(user2['u_id'])

    # members don't have rights
    else:
        raise AccessError("The authorised user is not an admin or owner")

    return {}

from backend.database import get_data, get_channel, get_user
from backend.helpers.token import get_user_from_token
from backend.helpers.exception import ValueError, AccessError

def admin_userpermission_change(token, u_id, permission_id):
    slackr = get_data()["slackr"]
    u_id = int(u_id)
    permission_id = int(permission_id)

    user1 = get_user(get_user_from_token(token))
    user2 = get_user(u_id)
    if permission_id > 3:
        raise ValueError("permission_id not valid")
    if permission_id < -1:
        raise ValueError("permission_id not valid")   
    if user2 == None:
        raise ValueError("u_id does not refer to a valid user")

    # if user2's permission is the same as permission_id
    if user2['permission_id'] == permission_id:
        raise AccessError("Trying to change to same permission!")

    # if user1 is the owner of the slackr
    if user1["permission_id"] == 1:
        # user1 cannot remove themselves if they are the only owner ...
        if len(slackr['admin']) == 1 and user2 == user1:
            raise AccessError("You are the only owner!")
        # since user1 can change permissions of everyone ...
        try:
            slackr['owner'].remove(user2['u_id'])
        except:
            ValueError
        try:
            slackr['admin'].remove(user2['u_id'])
        except:
            ValueError

        user2["permission_id"] = permission_id
        if user2["permission_id"] <= 2:
            slackr['admin'].append(user2['u_id'])
            if user2["permission_id"] == 1:
                slackr['owner'].append(user2['u_id'])

    # if user1 is an admin of the slackr
    elif user1["permission_id"] == 2:
        # if user2 is an owner of the slackr, user1 cannot change
        if user2["permission_id"] == 1 or permission_id == 1:
            raise AccessError("You're not an owner, you can't do that!")
        else:
            try:
                slackr['admin'].remove(user2['u_id'])
            except:
                ValueError

            user2["permission_id"] = permission_id
            if user2["permission_id"] <= 3:
                slackr['member'].append(user2['u_id'])
                if user2["permission_id"] == 2:
                    slackr['admin'].append(user2['u_id'])
    # members don't have rights >:)
    else:
        raise AccessError("Members don't have rights!")

    return {}

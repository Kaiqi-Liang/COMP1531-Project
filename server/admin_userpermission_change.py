from access_error import AccessError

def admin_userpermission_change (token, u_id, permission_id):
    if u_id == "Invalid user":
            raise ValueError("Does not refer to valid user")
    if permission_id < 1 or permission_id > 3:
            raise ValueError("Invalid permission id")
    # need to check if the user is an admin or owner!!
    return

def init_all_users():
    return {}

def add_new_user(user_id, user_name, user_password, user_email, all_users):
    retval = {}
    if(user_id in all_users):
        retval['code'] = -1
        retval['description'] = 'user already exists'
    else:
        all_users[user_id] = {'name': user_name, 'mail': user_email, 'pass': user_password}
        retval['code'] = 0
        retval['description'] = 'user inserted'
    return retval

def delete_user(user_id, all_users):
    if(user_id in all_users):
        del all_users[user_id]
        status = 'deleted'
    else:
        status = 'user not found'
    return status

def show_user(user_id, all_users):
    if(user_id in all_users):
        return all_users[user_id]
import json

def init_all_users():
    return {}

def add_new_user(user_id, user_name, user_password, user_email, all_users):
    if(user_id in all_users):
        raise ValueError('user already exists')
    else:
        all_users[user_id] = {'name': user_name, 'mail': user_email, 'pass': user_password}

def delete_user(user_id, all_users):
    if(user_id in all_users):
        del all_users[user_id]
    else:
        raise ValueError('user not found')

def show_user(user_id, all_users):
    if(user_id in all_users):
        return all_users[user_id]
    else:
        raise ValueError("User not found")
    
def list_users(all_users):
    for id, user in all_users:
        print(f"ID: {id}, User: {user.name}")

def save_users(all_users):
    try:
        with open('users.json','w') as outfile:
            json.dump(all_users, outfile)
    except Exception as ex:
        raise ex

def load_users():
    try:
        with open('users.json') as users_json:
            users = json.load(users_json)
            return users
    except Exception as ex:
        raise ex
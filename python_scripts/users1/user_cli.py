import users_ops

def start_all():
    all_commands = make_commands_dict()
    all_users = users_ops.init_all_users()

    while(True):
        print('users> ', end=None)
        user_command = input()
        if user_command == 'quit':
            break
        else:
            run_command(user_command, all_commands, all_users)
    

def make_commands_dict():
    commands_dict = {}
    commands_dict['add'] = handle_add_command
    commands_dict['del'] = handle_delete_command
    commands_dict['show'] = handle_print_command
    commands_dict['print'] = handle_print_command
    commands_dict['save'] = handle_save_command
    commands_dict['load'] = handle_load_command
    return commands_dict

def run_command(command, all_commands, all_users):
    words = command.split()
    all_commands = make_commands_dict()
    if words:
        if words[0] in all_commands:
            all_commands[words[0]] (all_users)
        else:
            print('no such command')

def handle_add_command(all_users):
    uid = input("enter id: ")
    uname = input("enter username: ")
    upass = input("enter password: ")
    uemail = input("enter email: ")
    try:
        users_ops.add_new_user(uid, uname, upass, uemail, all_users)
        print(f"Added {uname} successfully.")
    except ValueError as ex:
        print("Could not add user: ", ex)

def handle_delete_command(user_id, all_users):
    try:
        users_ops.delete_user(user_id, all_users)
    except ValueError as ex:
        print("Could not delete user: ", ex)

def handle_print_command(all_users):
    uid = input('enter user to print: ')
    try:
        user_data = users_ops.get_user(uid, all_users)
        print('name: ', user_data['name'])
        print('pass: ', user_data['pass'])
        print('email: ', user_data['email'])
    except ValueError as ex:
        print(ex)

def handle_list_command(all_users):
    users_ops.list_users(all_users)

def handle_save_command(all_users):
    try:
        users_ops.save_users(all_users)
    except Exception as ex:
        print("Could not save users: ", ex)

def handle_load_command(all_users):
    try:
        all_users = users_ops.load_users()
        print(all_users)
    except Exception as ex:
        print("Could not load users: ", ex)

start_all()
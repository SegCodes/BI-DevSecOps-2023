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
    retval = users_ops.add_new_user(uid, uname, upass, uemail, all_users)
    print(retval['description'])

def handle_delete_command():
    print('delete')

def handle_print_command(all_users):
    uid = input('enter user to print: ')
    retval = users_ops.get_user(uid, all_users)
    if retval['code'] == 0:
        user_data = retval['details']
        print('name: ', user_data['name'])
        print('pass: ', user_data['pass'])
        print('email: ', user_data['email'])
    print('user not found')

start_all()
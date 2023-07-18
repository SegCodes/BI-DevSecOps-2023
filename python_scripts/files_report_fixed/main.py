import os_handler
import report_handler
import os

def save_dirs_test():
    print('======= DIRS SIZES TEST =======')
    exec_dir = os.path.dirname(os.path.realpath(__file__))  
    dir_list = os_handler.scan_dirs('/home/osboxes/Documents/work/BI-DevSecOps-2023/python_scripts', [])
    os_handler.list_dirs(dir_list)
    os_handler.save_list_to_json(dir_list, exec_dir + '/dirs_sizes.json')
    print('===============================')

def save_files_test():
    print('======= FILES DATES TEST =======')
    exec_dir = os.path.dirname(os.path.realpath(__file__))  
    files_list = os_handler.scan_files('/home/osboxes/Documents/work/BI-DevSecOps-2023/python_scripts', [])
    os_handler.list_files(files_list)
    os_handler.save_list_to_json(files_list, exec_dir + '/files_dates.json')
    print('================================')

def get_biggest_dirs_list_test():
    print('======= SORT DIRS SIZES LIST TEST =======')
    exec_dir = os.path.dirname(os.path.realpath(__file__))
    sorted_dirs_list = os_handler.get_biggest_dirs_list(exec_dir + '/dirs_sizes.json')
    os_handler.list_dirs(sorted_dirs_list)
    print('=========================================')

def get_newest_files_list_test():
    print('======= SORT FILES DATES LIST TEST =======')
    exec_dir = os.path.dirname(os.path.realpath(__file__))
    sorted_files_list = os_handler.get_newest_files_list(exec_dir + '/files_dates.json')
    os_handler.list_files(sorted_files_list)
    print('==========================================')

def final_test():
    print('======= GENERATE REPORT TEST =======')
    exec_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Save dirs
    dir_list = os_handler.scan_dirs('/home/osboxes/Documents/work/BI-DevSecOps-2023/python_scripts', [])
    os_handler.list_dirs(dir_list)
    os_handler.save_list_to_json(dir_list, exec_dir + '/dirs.json')

    # Save files
    files_list = os_handler.scan_files('/home/osboxes/Documents/work/BI-DevSecOps-2023/python_scripts', [])
    os_handler.list_files(files_list)
    os_handler.save_list_to_json(files_list, exec_dir + '/files.json')

    # Get required lists
    biggest_dirs_list = os_handler.get_biggest_dirs_list(exec_dir + '/dirs.json')
    duplicate_files_list = os_handler.get_duplicate_files_list(exec_dir + '/files.json')
    newest_files_list = os_handler.get_newest_files_list(exec_dir + '/files.json')
    oldest_files_list = os_handler.get_oldest_files_list(exec_dir + '/files.json')

    # Build categories for report builder
    categories_dict = {
        'biggest_dirs': biggest_dirs_list,
        'duplicate_files': duplicate_files_list,
        'newest_files': newest_files_list,
        'oldest_files': oldest_files_list 
        }
    
    # Build Report
    report_handler.build_report(categories_dict, exec_dir)
    print('====================================')

def main():
    # save_dirs_test()
    # save_files_test()
    # get_biggest_dirs_list_test()
    # get_newest_files_list_test()
    # final_test()
    # os_handler.scan_dirs('/home/osboxes/Documents/work/BI-DevSecOps-2023/python_scripts', [])
    # print (os_handler.hash_table)
    os_handler.handle_newest_files()
    pass

if __name__ == '__main__':
    main()
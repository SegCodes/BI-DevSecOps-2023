import os_handler
import report_handler
import os

def main():
    os_handler.scan_dirs('/home/osboxes/Documents/work/BI-DevSecOps-2023/python_scripts', 10)
    exec_dir = os.path.dirname(os.path.realpath(__file__))
    categories_dict = {
        'BiggestDirs': os_handler.biggest_dirs,
        'DuplicateFiles': os_handler.duplicate_table,
        'NewestFiles': os_handler.newest_files,
        'OldestFiles': os_handler.oldest_files
    }
    report_handler.build_report(categories_dict, exec_dir, 10)
    pass

if __name__ == '__main__':
    main()
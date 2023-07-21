import os
from datetime import datetime
import hashlib

hash_table, duplicate_table = {}, {}
newest_files, oldest_files, biggest_dirs = [], [], []

def handle_all_dirs_operations(dir: os.DirEntry, n):
    handle_biggest_dirs(dir, n)
    print(f'Biggest Directories: {biggest_dirs}\n')

def handle_biggest_dirs(dir: os.DirEntry, n):
    global biggest_dirs
    dir_size = get_dir_size(dir)
    if len(biggest_dirs) < n:
        dir_dict = {
            "Name": dir.name,
            "Path": dir.path,
            "Size": dir_size
        }
        biggest_dirs.append(dir_dict)
        biggest_dirs.sort(key=dir_size_predicator, reverse=True)
    else:
        biggest_dirs.sort(key=dir_size_predicator, reverse=True)
        for index, curr_dir in enumerate(biggest_dirs):
            if curr_dir['Size'] < dir_size:
                biggest_dirs.pop()
                dir_dict = {
                    "Name": dir.name,
                    "Path": dir.path,
                    "Size": dir_size
                }
                biggest_dirs.insert(index, dir_dict)
                return

def get_dir_size(dir: os.DirEntry):
    dir_size = 0
    for file in os.scandir(dir.path):
        if file.is_file():
            dir_size += file.stat().st_size
    return convert_dir_size(dir_size)

def handle_all_file_operations(file: os.DirEntry, n):
    handle_duplicate(file)
    handle_newest_files(file, n)
    handle_oldest_files(file, n)
    print(f'Newest files: {newest_files}\n')
    print(f'Oldest files: {oldest_files}\n')
    print(f'dupliacte files: {duplicate_table}\n')

def handle_duplicate(file: os.DirEntry):
    global hash_table, duplicate_table
    file_hash = get_file_hash(file)
    if file_hash not in hash_table:
        file_hash_dict = {
            file_hash: {
                'Path': file.path
                }
            }
        hash_table.update(file_hash_dict)
        file_hash_dict_dup = { 
            file_hash: {
                'Name': file.name,
                'Paths': {file.path}
            }
        }
        duplicate_table.update(file_hash_dict_dup)
    else:
        if file_hash not in duplicate_table:
            file_hash_dict = { 
                file_hash: {
                    'Name': file.name,
                    'Paths': {file.path}
                }
            }
            duplicate_table.update(file_hash_dict)
        else:
            file_hash_dict = duplicate_table[file_hash]
            file_hash_dict['Paths'].add(file.path)

def handle_newest_files(file: os.DirEntry, n):
    file_date = datetime.fromtimestamp(file.stat().st_ctime)
    if len(newest_files) < n:
        newest_files.append({
            'Name': file.name,
            'Path': file.path,
            'DateObject': file_date,
            'Date': str(file_date)
        })
        newest_files.sort(key=file_date_predicator,reverse=True)
    else:
        newest_files.sort(key=file_date_predicator,reverse=True)
        for index, curr_file in enumerate(newest_files):
            curr_file_date = curr_file['DateObject']
            if file_date > curr_file_date:
                newest_files.pop()
                newest_files.insert(index, {
                    'Name': file.name,
                    'Path': file.path,
                    'DateObject': file_date,
                    'Date': str(file_date)
                })
                return

def handle_oldest_files(file: os.DirEntry, n):
    file_date = datetime.fromtimestamp(file.stat().st_ctime)
    if len(oldest_files) < n:
        oldest_files.append({
            'Name': file.name,
            'Path': file.path,
            'DateObject': file_date,
            'Date': str(file_date)
        })
        oldest_files.sort(key=file_date_predicator,reverse=False)
    else:
        oldest_files.sort(key=file_date_predicator,reverse=False)
        for index, curr_file in enumerate(oldest_files):
            curr_file_date  = curr_file['DateObject']
            if file_date < curr_file_date:
                oldest_files.pop()
                oldest_files.insert(index, {
                    'Name': file.name,
                    'Path': file.path,
                    'DateObject': file_date,
                    'Date': str(file_date)
                })
                return

def scan_dirs(path: str, n):
    """Goes over all the dirs in the given path and returns a list of all the directories
    containing their info.


    Parameters:
    --------------
    path: str, required
        The parent directory which acts as the starting path for the scan.
    
    dir_list: list, required
        The list which will contain all of the directories info.

    Return Value:
    --------------
    dir_list: list
        The updated list with all the directories info.
    """
    for dir_entry in os.scandir(path):
        if dir_entry.is_dir(follow_symlinks=False):
            handle_all_dirs_operations(dir_entry, n)
            scan_dirs(dir_entry.path, n)
        else:
            handle_all_file_operations(dir_entry, n)
            pass
    return

def convert_dir_size(dir_size: int) -> int:
    return round(dir_size / 1024 ** 1, 2)

def dir_size_predicator(dir_dict: dict) -> int:
    return dir_dict['Size']

def get_file_hash(file_to_process: str) -> str:
    sha256 = hashlib.sha256()

    with open(file_to_process, 'rb') as file:
        while True:
            hash_data = file.read(65536)
            if not hash_data:
                break
            sha256.update(hash_data)
    return sha256.hexdigest()

def file_date_predicator(dir_dict: dict) -> int:
    return dir_dict['DateObject']
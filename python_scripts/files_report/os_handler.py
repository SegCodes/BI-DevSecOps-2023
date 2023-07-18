import os
import json
import datetime
import hashlib
import itertools

def scan_dirs(path: str, dir_list: list) -> list:
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
            dir_size = get_dir_size(dir_entry.path)
            curr_dir = {
                'name': dir_entry.name,         
                'path': dir_entry.path, 
                'size': dir_size,
                'kb_size': convert_dir_size(dir_size)
            }            
            # print(f'dir: {curr_dir["name"]}')
            # print(f'dir Path: {curr_dir["path"]}\n')
            # print(f'dir Size: {curr_dir["size"]}')
            dir_list.append(curr_dir)
            scan_dirs(dir_entry.path, dir_list)
    return dir_list

def get_dir_size(dir_path: str) -> int:
    """Gets the size of a directory in the given path.
    
    Parameters:
    --------------
    dir_path: str, required
        The path of the directory.
    
    Return Value:
    --------------
    dir_size: int
        The size of the directory.
    """
    dir_size = 0
    for dir_entry in os.scandir(dir_path):
        if dir_entry.is_dir(follow_symlinks=False):
            dir_size = get_dir_size(dir_entry.path)
        else:
            dir_size += dir_entry.stat(follow_symlinks=False).st_size
    return dir_size

def convert_dir_size(dir_size: int) -> int:
    return round(dir_size / 1024 ** 1, 2)

def list_dirs(dir_list: list) -> None:
    """Prints all the directories in a directories list.

    Parameters:
    --------------
    dir_list: list, required
        The directories list to be printed.
    """
    for dir in dir_list:
        print(f'Dir: {dir["name"]}')
        print(f'Path: {dir["path"]}')
        print(f'Size: {dir["size"]}')
        print(f'Human Size: {dir["kb_size"]} KB\n')

def get_biggest_dirs_list(json_path: str) -> list: 
    """Sorts a directories list from json from largest to smallest
    
    Parameters:
    --------------
    json_path: str, required
        The json path containing the list to be sorted.

    Return Value:
    --------------
    dirs_list: list
        The sorted directories list.
    """
    with open(json_path, 'r') as json_data:
        dirs_list = json.load(json_data)
        dirs_list.sort(key=dir_size_predicator, reverse=True)
        return dirs_list[:10]

def dir_size_predicator(dir_dict: dict) -> int:
    return dir_dict['size']

def scan_files(path: str, files_list: list) -> list:
    """Goes over all the files in the given path and returns a list of all the files
    containing their info.


    Parameters:
    --------------
    path: str, required
        The parent directory which acts as the starting path for the scan.
    
    files_list: list, required
        The list which will contain all of the files info.

    Return Value:
    --------------
    files_list: list
        The updated list with all the files info.
    """
    for dir_entry in os.scandir(path):
        if dir_entry.is_dir(follow_symlinks=False):
            files_list = scan_files(dir_entry.path, files_list)
        else:
            date = dir_entry.stat(follow_symlinks=False).st_ctime
            curr_file = {
                'name': dir_entry.name,
                'path': dir_entry.path,
                'date': date,
                'norm_date': str(datetime.datetime.fromtimestamp(date)),
                'hash': get_file_hash(dir_entry.path)
            }
            files_list.append(curr_file)
    return files_list

def get_file_hash(file_to_process: str) -> str:
    sha256 = hashlib.sha256()

    with open(file_to_process, 'rb') as file:
        while True:
            hash_data = file.read(65536)
            if not hash_data:
                break
            sha256.update(hash_data)
    return sha256.hexdigest()

def list_files(files_list: list) -> None:
    """Prints all the files in a files list.

    Parameters:
    --------------
    files_list: list, required
        The files list to be printed.
    """
    for file in files_list:
        print(f'File: {file["name"]}')
        print(f'Path: {file["path"]}')
        print(f'Hash: {file["hash"]}')
        print(f'Creation Date: {file["date"]}')
        print(f'Creation Date - Normal: {file["norm_date"]}\n')

def get_newest_files_list(json_path: str) -> list: 
    """Gets the 10 most newest files.
    
    Parameters:
    --------------
    json_path: str, required
        The path of the json containing the list to be sorted.

    Return Value:
    --------------
    files_list: list
        The list with the 10 newest files.
    """
    with open(json_path, 'r') as json_data:
        files_list = json.load(json_data)
        files_list.sort(key=file_date_predicator, reverse=True)
        return files_list[:10]
    
def get_oldest_files_list(json_path: str) -> list: 
    """Gets the 10 most oldest files.
    
    Parameters:
    --------------
    json_path: str, required
        The path of the json containing the list to be sorted.

    Return Value:
    --------------
    files_list: list
        The list with the 10 oldest files.
    """
    with open(json_path, 'r') as json_data:
        files_list = json.load(json_data)
        files_list.sort(key=file_date_predicator, reverse=False)
        return files_list[:10]

def file_date_predicator(dir_dict: dict) -> int:
    return dir_dict['date']

def get_duplicate_files_list(json_path: str) -> list: 
    """Gets a list of duplicated (appears at least twice) files.
    
    Parameters:
    --------------
    json_path: str, required
        The path of the json containing the list to be sorted.

    Return Value:
    --------------
    files_list: list
        The list with the duplicated files.
    """
    with open(json_path, 'r') as json_data:
        files_list = json.load(json_data)
        duplicate_file_list = []
        counter = 0
        for curr_file, comp_file in itertools.combinations(files_list, 2):
            if curr_file["hash"] == comp_file["hash"] and curr_file["path"] != comp_file["path"]:
                counter += 1

            if counter > 0 and curr_file["hash"] not in duplicate_file_list:    
                duplicate_file_list.append(curr_file)
            
            counter = 0
        return duplicate_file_list

def save_list_to_json(obj_list: list, path: str) -> None:
    """Saves a objects list to a json in the given path.
    
        Parameters:
    --------------
    obj_list: list, required
        The objects list to be saved.
    
    path: str, required
        The path in which the json will be saved.
    """
    with open(path, 'w') as dest_json:
        json.dump(obj_list, dest_json, indent=4)
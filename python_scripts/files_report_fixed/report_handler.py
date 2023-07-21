def build_report(categories_dict: dict, report_path: str, n) -> None:
    """Builds a OS Reports that contains the following info:
        
        1. N most biggest directories.
        2. List of duplicate files (same hash appears more than once).
        3. N newest files.
        4. N oldest files.

    The report is saved as a .txt file in the path provided.
        
    Parameters:
    --------------
    categories_dict: dict, required
        The dictionary containing all the lists with the required info per category.
    
    path: str, required
        The path to save the report.
    """
    report_body = '======== OS REPORT ========'
    report_body += f'\n------- {n} MOST BIGGEST DIRECTORIES ------\n'
    biggest_dirs_list = categories_dict['BiggestDirs']
    for i in range(len(biggest_dirs_list)):
        report_body += (f'{i + 1}:\n\tName: {biggest_dirs_list[i]["Name"]}' +
                        f'\n\tPath: {biggest_dirs_list[i]["Path"]}' +
                        f'\n\tSize: {biggest_dirs_list[i]["Size"]} KB\n')
    
    report_body += f'\n------ DUPLICATE FILES ------\n'
    duplicate_files_dict = categories_dict['DuplicateFiles']
    for i, (file_hash, file_info) in enumerate(duplicate_files_dict.items()):
        if(len(file_info['Paths']) > 1):
            report_body += f'Name: {file_info["Name"]}\nPaths:'
            # report_body += f'\n\tHash: {duplicate_files_dict["Hash"]}\n'
            for file_path in file_info['Paths']:
                report_body += f'\n\t{file_path}'
            report_body += f'\nFile\'s Total Appearances: {len(file_info["Paths"])}\n\n'

    report_body += f'------ {n} NEWEST FILES ------\n'
    newest_files_list = categories_dict['NewestFiles']
    for i, file in enumerate(newest_files_list):
        report_body += (f'{i + 1}:\n\tName: {file["Name"]}' +
                        f'\n\tPath: {file["Path"]}' +
                        f'\n\tCreation Date: {file["Date"]}\n')

    report_body += f'\n------ {n} OLDEST FILES ------\n'
    oldest_files_list = categories_dict['OldestFiles']
    for i, file in enumerate(oldest_files_list):
        report_body += (f'{i + 1}:\n\tName: {file["Name"]}' +
                        f'\n\tPath: {file["Path"]}' +
                        f'\n\tCreation Date: {file["Date"]}\n')
    
    report_body += f'==========================='

    # Build Report
    with open(report_path + '/files_report.txt', 'w') as report_file:
        report_file.write(report_body)
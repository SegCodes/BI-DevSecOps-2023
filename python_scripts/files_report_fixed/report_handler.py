def build_report(categories_dict: dict, path: str) -> None:
    """Builds a OS Reports that contains the following info:
        
        1. 10 most biggest directories.
        2. List of duplicate files (same hash appears more than once).
        3. 10 newest files.
        4. 10 oldest files.

    The report is saved as a .txt file in the path provided.
        
    Parameters:
    --------------
    categories_dict: dict, required
        The dictionary containing all the lists with the required info per category.
    
    path: str, required
        The path to save the report.
    """
    report_body = '======== OS REPORT ========'
    report_body += f'\n10 MOST BIGGEST DIRECTORIES:\n'
    biggest_dirs_list = categories_dict['biggest_dirs']
    for i in range(len(biggest_dirs_list)):
        report_body += f'{i + 1}:\n\tName: {biggest_dirs_list[i]["name"]}'
        report_body += f'\n\tPath: {biggest_dirs_list[i]["path"]}'
        report_body += f'\n\tSize: {biggest_dirs_list[i]["kb_size"]} KB\n'
    
    report_body += f'\nDUPLICATE FILES:\n'
    duplicate_files_list = categories_dict['duplicate_files']
    for i in range(len(duplicate_files_list)):
        report_body += f'{i + 1}:\n\tName: {duplicate_files_list[i]["name"]}'
        report_body += f'\n\tPath: {duplicate_files_list[i]["path"]}'
        report_body += f'\n\tCreation Date: {duplicate_files_list[i]["norm_date"]}'
        report_body += f'\n\tHash: {duplicate_files_list[i]["hash"]}\n'

    report_body += f'\n10 NEWEST FILES:\n'
    newest_files_list = categories_dict['newest_files']
    for i in range(len(newest_files_list)):
        report_body += f'{i + 1}:\n\tName: {newest_files_list[i]["name"]}'
        report_body += f'\n\tPath: {newest_files_list[i]["path"]}'
        report_body += f'\n\tCreation Date: {newest_files_list[i]["norm_date"]}\n'

    report_body += f'\n10 OLDEST FILES:\n'
    oldest_files_list = categories_dict['oldest_files']
    for i in range(len(oldest_files_list)):
        report_body += f'{i + 1}:\n\tName: {oldest_files_list[i]["name"]}'
        report_body += f'\n\tPath: {oldest_files_list[i]["path"]}'
        report_body += f'\n\tCreation Date: {oldest_files_list[i]["norm_date"]}\n'
    
    report_body += f'==========================='

    # Build Report
    with open(path + '/files_report.txt', 'w') as report_file:
        report_file.write(report_body)
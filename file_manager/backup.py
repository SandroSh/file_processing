import os
import shutil




def backup_file(file_path, backup_dir = 'backup/'):
    """
    Creates a backup copy of a file in the specified backup directory.

    This function checks if the given file exists, and if so, it copies the file
    to the specified backup directory. If the directory doesn't exist, it is created.
    
    @param file_path: str - The path of the file to back up.
    @param backup_dir: str - The directory where the backup file will be stored (default is 'backup/').
    @return: {path: str, usage: tuple} - The path of the newly created backup file.
    @raises FileNotFoundError: If the file does not exist.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not foundm path - {file_path}')
    
    os.makedirs(backup_dir, exist_ok=True)
    backup_path =os.path.join(backup_dir, os.path.basename(file_path))

    shutil.copy(file_path,  backup_path)
    return {"path": backup_path,"Usage": shutil.disk_usage(backup_path)}
 

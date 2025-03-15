import os

def file_exists(file_path):
    """
    Checks if a file exists at the given path.

    @param file_path: str - The full path of the file to check.
    @return: bool - True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def file_extension(file_path):
    """
    Checks if a file is .txt format  at the given path.

    @param file_path: str - The full path of the file to check.
    @return: {extension:string, is_text_file:string}.
    """
    return{"extension": file_path.lower().split('.')[1], "is_text_file": file_path.lower().endswith('.txt')}


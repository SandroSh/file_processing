import os





def write_file(file_path, data):
    """
    Writes data to a file, overwriting existing content.

    This function opens the specified file in write mode ('w'),
    meaning any existing content in the file will be erased.
    The provided data is then written to the file.

    @param file_path: str - The path of the file to write to.
    @param data: str - The content to be written to the file.
    @raises IOError: If an error occurs during file writing.
    """
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(data)
    except Exception as e:
        raise IOError(f'Error in writing to a file {e}')
    

def append_file(file_path, data):
    """
    Writes data to a file, appending it to existing content.

    This function opens the specified file in write mode ('a'),
    meaning any existing content in the file will not be deleted.
    The provided data is then appended to the file.

    @param file_path: str - The path of the file to write to.
    @param data: str - The content to be appended to the file.
    @raises IOError: If an error occurs during file writing.
    """
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(data + '\n')
    except Exception as e:
        raise IOError(f'Error while appending text {e}')
    
def create_and_write_file(directory: str, name: str,  data: str, extension = 'txt'):
    """
    creates file writes data  in it.

    This function creates the file with specified name,
    The provided data is then writed to the file.

    @param directory: str - The path of the directory where file will be created.
    @param name: str - The name of the file.
    @param data: str - The content to be appended to the file.
    @param extension: str - The extension of a file.
    @raises IOError: If an error occurs during file creating or writing.
    """
    try:
        # Ensure that directory exists
        os.makedirs(directory,exist_ok=True)

        file_name = f"{name}.{extension}"
        file_path = os.path.join(directory,file_name)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        
        return file_path
    except Exception as e:
        raise IOError(f'error creaating or writing to a file {e}')
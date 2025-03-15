import os

def read_file(file_path):
    """
    reads data from a file.

    This function opens the specified file in read mode ('r'),
    meaning any existing content from the file will be read.
    The provided data is then returned.

    @param file_path: str - The path of the file to read from.
    @param data: str - The content to be raed from the file.
    @raises FileNotFoundError: If an error occurs during file reading.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found {file_path}')
    
    with open(file_path, 'r',encoding='utf-8') as file:
        data = file.read()
        return data, len(data)
    

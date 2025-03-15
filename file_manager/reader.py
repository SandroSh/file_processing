import os

def read_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found {file_path}')
    
    with open(file_path, 'r',encoding='utf-8') as file:
        data = file.read()
        return data, len(data)
    

import os





def list_files(directory):
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]
    except FileNotFoundError:
        return f'Error: directory {directory} not found'
    except PermissionError:
        return f'Error: denied access for {directory}'    

def list_files_by_extension(directory, extension):
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f)) and f.endswith(extension)]
    except FileNotFoundError:
        return f'Error: directory {directory} not found'
    except PermissionError:
        return f'Error: denied access for {directory}'    

def list_files_recursive(directory):
    file_list = []

    try:
        for root, _, files in os.walk(directory):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list
    except FileNotFoundError:
        return f'Error: directory {directory} not found'
    except PermissionError:
        return f'Error: denied access for {directory}'    



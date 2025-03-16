import json


def load_json(file_path:str) -> dict:
    """
    Load JSON data from a file.

    :param file_path: Path to the JSON file.
    :return: Dictionary representation of JSON data.
    """
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found on this address {file_path}')
    except json.JSONDecodeError:
        raise json.JSONDecodeError('Fail decode json')
    
def save_json(file_path:str, data:dict) -> None:
    """
    Save dictionary data to a JSON file.

    :param data: Dictionary to save.
    :param file_path: Path to the JSON file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
            print(f'Data succesfully saved to {file_path}')
    except IOError:
        print('Error to write to file')
    

def process_json(data:dict) -> dict:
    """
    Process JSON data by modifying it's content
    :param data: Dictionary containing JSON data.
    :return: modified dictionary with lowercase strings
    """
    if not isinstance(data, dict):
        print('Provided data is not dictionary')
        return {}
    
    data['processed'] = True
    data['quantity'] = len(data)

    # Convert all values to lowercase
    for key, value in data.items():
        if isinstance(value, str):
            data[key] = value.lower()

    return data
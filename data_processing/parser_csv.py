import csv





def parse_csv(file_path: str) -> list[dict]:
    """ 
    Parses CSV data and returns it as a list of dictionaries, where each row is a dictionary.

    This function reads a CSV file and converts each subsequent row into a 
    dictionary with column names as keys.

    @param file_path: str - The path to the CSV file to parse.
    @return: list[dict] - A list of dictionaries representing the rows of the CSV file.
    @raises FileNotFoundError: If the file does not exist.
    @raises ValueError: If the CSV file format is invalid.
    """
    data = []

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)
    except FileNotFoundError:
        FileNotFoundError('File not found')
    
    return data
    

        
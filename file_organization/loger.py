import logging





logging.basicConfig(
    filename='file_ops.log',
    level= logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

#  Implement logging for separate read and write operations

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            logging.info('Successfully read file')
            return content
    except Exception as e:
        logging.exception(f'Error reading file {e}')
        
        
def write_file(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            content = file.write(data)
            logging.info('Successfully write in file')
            return content
    except Exception as e:
        logging.exception(f'Error writing in file {e}')
        
        

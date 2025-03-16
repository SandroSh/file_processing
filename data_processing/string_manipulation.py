from  file_manager import reader, writer





def remove_empty_lines(file_path):
    try:
        lines = reader(file_path)
        non_empty_lines = [line for line in lines if line.strip()]
        writer(file_path, non_empty_lines)
    
    except IOError:
        raise IOError('Error')

def replace_word(file_path, old_word, new_word):
    try:
        lines = reader(file_path)
        updated_lines = [line.replace(old_word,new_word) for line in lines]
        writer(file_path,updated_lines)
    except IOError:
        raise IOError('Error')


def count_word(file_path, word):
    try:
        lines = reader(file_path)
        return sum(line.count(word) for line in lines)
    except IOError:
        raise IOError('Error')

def extract_lines_with_specific_words(file_path, word):
    try:
        lines = reader(file_path)
        filtered_lines = [line for line in lines if word in line]
        return filtered_lines
    except IOError:
        raise IOError('Error')





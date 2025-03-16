import os





def sort_files(directory: str, sort_by:str = 'name', reverse: bool = False) -> list[str]:
    
    if not os.path.isdir(directory):
        raise ValueError(f'{directory} is not valid directory')
    
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]
    
    if not files:
        return []
    
    sort_functions = {
        'name': lambda x: os.path.basename(x).lower(),
        'type': lambda x: os.path.splitext(x)[1].lower() or 'no extension',
        'date': lambda x: os.path.getatime(x)
    }
    
    if sort_by not in sort_functions:
        raise ValueError('sort is available only with name, type, dat')
    
    return sorted(files, key = sort_functions[sort_by], reverse=reverse)
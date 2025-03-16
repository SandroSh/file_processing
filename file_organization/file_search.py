import os
import fnmatch




def search_files(start_dir, pattern):
    
    matching_files = []
    
    for root, _, files in os.walk(start_dir):
        for filename in fnmatch.filter(files, pattern):
            matching_files.append(os.path.join(root, filename))
            
    return matching_files



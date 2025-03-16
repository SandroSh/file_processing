import os
import shutil




def organize_files(directory):
    if not os.path.isdir(directory):
        print(f'{directory} is not valid')
        return
    
    all_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory,f))]
    
    
    if not all_files:
        print('There is no files')
        return
    
    organized_count = 0;
    
    for filename in all_files:
        file_path = os.path.join(directory,filename)
        
        _, extension =  os.path.splitext(filename)
        extension = extension[1:].lower()
        
        extension_dir = os.path.join(directory, extension)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)
        
        destination = os.path.join(extension_dir, filename)
        
        try:
            shutil.move(file_path, destination)
            organized_count += 1
        except Exception as e:
            print(f'Error moving {filename}: {e}')
    print(f"organized {organized_count} files")
        
        
        
        

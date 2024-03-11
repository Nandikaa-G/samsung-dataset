import os
import json

def is_json(file_path):
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        return True
    except (ValueError, IOError):
        return False

def check_directory(directory_path):
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.json'):
            if not is_json(file_path):
                return file_name
        else:
            return file_name
    return None

# Specify the directory path here
directory_path = './output'
invalid_file = check_directory(directory_path)
if invalid_file:
    print(f"{invalid_file} is not a valid JSON file or the directory does not exist.")
else:
    print("All files are valid JSON files.")

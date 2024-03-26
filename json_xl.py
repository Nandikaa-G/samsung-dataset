import os
import pandas as pd
import json

# Function to read JSON from a file
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to traverse through a directory and extract data from JSON files
def extract_data_from_json_files(directory):
    data = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.json'):
            file_path = os.path.join(directory, file_name)
            json_data = read_json(file_path)
            data.append({'file_name': file_name, 'json_data': json_data})
    return data

# Main function
def main():
    directory = './output1'  # Update with your directory path
    data = extract_data_from_json_files(directory)
    df = pd.DataFrame(data)
    df.to_excel('json_data.xlsx', index=False)

if __name__ == "__main__":
    main()

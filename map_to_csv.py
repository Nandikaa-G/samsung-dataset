import os
import pandas as pd
import json

# Function to read JSON file
def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to read text file
def read_text(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

# Function to traverse directories and gather data
def traverse_directories():
    data = []
    for i in range(501, 751): #change based on your table numbers
        table_file = f'./output1/table_{i}.json' #location where tables are stored
        summary_file = f'./output2/table_{i}_summ.txt' #location where summaries are stored

        if os.path.exists(table_file) and os.path.exists(summary_file):
            try:
                table_data = read_json(table_file) #to read json
            except json.JSONDecodeError:
                print(f"Invalid JSON file: {table_file}")
                continue
            try:
                summary_data = read_text(summary_file) #to read text
            except Exception as e:
                print(f"Error reading text file {summary_file}: {e}")
                continue    
            
            data.append({ 
                's.no': i,
                'table name': f'table_{i}',
                'json content': table_data,
                'summary': summary_data
            })

    return data

# Function to save data to spreadsheet
def save_to_spreadsheet(data):
    df = pd.DataFrame(data)
    df.to_excel('output_mugil.xlsx', index=False)

# Main function
def main():
    data = traverse_directories()
    save_to_spreadsheet(data)

if __name__ == "__main__":
    main()

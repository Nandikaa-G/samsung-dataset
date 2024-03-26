import os
import pandas as pd

# Function to read text from a file
def read_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Function to traverse through a directory and extract text from text files
def extract_text_from_files(directory):
    data = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory, file_name)
            text = read_text(file_path)
            data.append({'file_name': file_name, 'text': text})
    return data

# Main function
def main():
    directory = './output2'  # Update with your directory path
    data = extract_text_from_files(directory)
    df = pd.DataFrame(data)
    df.to_excel('onlyText.xlsx', index=False)

if __name__ == "__main__":
    main()

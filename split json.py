import os
import json

i=250
def increment():
    global i
    i+=1

def get_json_files(directory):
    json_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            json_files.append(filename)
    return json_files


def split_json_file(input_file, output_dir, max_entries=20):
    with open(input_file, 'r') as f:
        data = json.load(f)

    num_files = (len(data)//max_entries)+1  

    for j in range(num_files):
        increment()
        start_index = j * max_entries
        end_index = min((j + 1) * max_entries, len(data))
        output_data = data[start_index:end_index]

        output_filename = os.path.join(output_dir, f"table_{i}.json") 
        with open(output_filename, 'w') as f:
            json.dump(output_data, f, indent=4)      
output_directory = "output"  # files stored in new output directory


directory_path = './amruth'
json_files = get_json_files(directory_path)

print(json_files)

if not os.path.exists(output_directory):
        os.makedirs(output_directory)

for input_json_file in json_files:
    split_json_file("./amruth/"+input_json_file, output_directory)  



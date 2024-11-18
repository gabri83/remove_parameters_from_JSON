import os
import json

# Step 1: Define the directory containing the original JSON files
input_directory = '/path/to/original/json/files/'  # Change this to your actual input directory path

# Step 2: Define the output directory to save modified JSON files
output_directory = '/path/to/output/json/files/'  # Change this to your desired output directory path

# Step 3: Ensure the output directory exists, if not, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Step 4: Define the parameters to be removed (add as many as needed)
parameters_to_remove = ['your_parameter', 'another_parameter']  # Add any parameters you want to remove

# Step 5: Loop through each JSON file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.json'):  # Only process files with a .json extension
        input_file_path = os.path.join(input_directory, filename)
        
        # Step 6: Open and load the original JSON file
        with open(input_file_path, 'r') as json_file:
            data = json.load(json_file)
        
        # Step 7: Remove the specified parameters if they exist in the JSON data
        for parameter in parameters_to_remove:
            if parameter in data:
                del data[parameter]
        
        # Step 8: Define the output file path
        output_file_path = os.path.join(output_directory, filename)
        
        # Step 9: Save the modified JSON data to the output directory
        with open(output_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)  # Write back with pretty printing (indentation)
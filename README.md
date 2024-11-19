
# JSON Parameter Removal Script

This script processes multiple JSON files to remove specified parameters and saves the updated files in a separate directory.

## Features
- Remove one or more parameters from JSON files.
- Preserve original files by saving modified versions to a different directory.
- Easy to customize for any number of parameters.

## How to Use

### Prerequisites
1. Install Python (version 3.6 or higher recommended).
2. Ensure your JSON files are in a directory.

### Steps
1. **Download the script** and place it in your working directory.
2. Define the following in the script:
    - `input_directory`: Path to the folder containing your JSON files.
    - `output_directory`: Path to the folder where modified files will be saved.
    - `parameters_to_remove`: List of parameters you want to remove from the JSON files.
3. Run the script:
    ```bash
    python3 script_name.py
    ```
4. Check the `output_directory` for the updated JSON files.

### Example
**Original JSON File:**
```json
{
    "name": "example",
    "age": 40,
    "your_parameter": "remove_this",
    "another_parameter": "remove_this_too",
    "city": "London"
}
```

**Parameters to Remove:**
```python
parameters_to_remove = ['your_parameter', 'another_parameter']
```

**Modified JSON File:**
```json
{
    "name": "example",
    "age": 40,
    "city": "London"
}
```

## Customization
- To add or remove parameters, update the `parameters_to_remove` list in the script:
    ```python
    parameters_to_remove = ['parameter1', 'parameter2']
    ```

- You can adjust the `input_directory` and `output_directory` paths as needed.

## Notes
- Ensure the `output_directory` exists or the script will create it automatically.
- Backup your original files before running the script, though the script does not modify them directly.

## License
This script is released under the MIT License.

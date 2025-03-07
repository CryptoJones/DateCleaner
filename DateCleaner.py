import os
import re

# Get the list of files in the current directory
current_directory = os.getcwd()
path_string = "C:\\Users\\akclark\\Dropbox\\Family Info\\_Health\\"
files = os.listdir(path_string)

# Function to modify the filename
def modify_filename(filename):
    # Check if the filename starts with a date in YYYYMMDD format
    match = re.match(r'(\d{4})(\d{2})(\d{2})(.*)', filename)
    
    if match:
        # Extract the date and the rest of the filename
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        rest_of_filename = match.group(4)
        
        # Modify the date format by adding hyphens
        new_filename = f'{year}-{month}-{day}{rest_of_filename}'
        
        # Rename the file
        os.rename(path_string+filename, path_string+new_filename)
        print(f'Renamed: {filename} -> {new_filename}')
    else:
        print(f'No date prefix found in: {filename}')

# Iterate over the files and modify those with a date prefix
for file in files:
    modify_filename(file)


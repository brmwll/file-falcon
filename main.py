import os
import shutil
import json
from pync import Notifier

# Load the configuration file
with open('config.json', 'r') as file:
    config = json.load(file)

# Set the path to the Downloads directory
downloads_dir = os.path.expanduser('~/Downloads')

# Iterate over all files in the Downloads directory
for filename in os.listdir(downloads_dir):
    if os.path.isfile(os.path.join(downloads_dir, filename)):
        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension[1:]

        # Determine the directory for the file type
        directory = next((key for key, value in config.items()
                         if file_extension in value), 'Others')

        # Create the directory if it doesn't exist
        directory_path = os.path.join(downloads_dir, directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # Move the file to the directory if a file with the same name doesn't already exist there
        if not os.path.exists(os.path.join(directory_path, filename)):
            shutil.move(os.path.join(downloads_dir, filename), directory_path)

# Send a desktop notification when the script is done
Notifier.notify('Your files have been organized.', title='Organizing Complete')

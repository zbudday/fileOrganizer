import os
import shutil

def move_files(folder_name):
    # Define categories and some of their file extensions
    categories = {
        'images': ['.jpg', '.jpeg', '.gif', '.tif', '.tiff', '.avif'],  # Image file extensions
        'data': ['.dat', '.csv', '.xlsx', '.json', '.txt', '.db'],  # Data file extensions
        'programs': ['.py', '.c', '.java', '.cpp']  # Program file extensions
    }

    # Create a dictionary to map extensions to their categories
    extension_to_category = {}
    for category, extensions in categories.items(): #Loops through categories
        for ext in extensions:
            extension_to_category[ext] = category

    # Create subfolders of images, data, & programs if they don't exist
    for category in categories.keys():
        os.makedirs(os.path.join(folder_name, category), exist_ok=True) #Creates categories of the categories' keys (images, data, programs)
    os.makedirs(os.path.join(folder_name, "other"), exist_ok=True) #Creates the 'other' folder

    # Loop over files in the folder
    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)
        
        # Skip if it's not a file (e.g., it's a directory)
        if not os.path.isfile(file_path):
            print(f"Skipping directory: {filename}")
            continue

        # Determine the category based on file extension
        extension = os.path.splitext(filename)[1].lower()
        destination = extension_to_category.get(extension, "other")  # Default to "other" if extension not found

        # Shows when files are being moved and where to
        print(f"Processing file: {filename}, Extension: {extension}, Destination: {destination}")

        # Move the file to the appropriate folder / debugging to make sure only files are moved (folders cannot be currently)
        try:
            shutil.move(file_path, os.path.join(folder_name, destination, filename))
            print(f"Moved {filename} to {destination} folder")
        except Exception as e:
            print(f"Error moving {filename}: {e}")


# Get the folder path from the user (must enter the full path from C:\Users\...)
folder_path = input("Enter the full path to the folder name to organize: ")

# Check if the folder exists and organize it
if os.path.exists(folder_path):
    move_files(folder_path)
    print("Your files have been organized")
else:
    print("That folder path does not exist")
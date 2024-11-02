import os

# Define the directory path
directory_path = r'C:\Users\Asus\OneDrive - Universidad de los Andes\Documentos\DJ\Music library'

def list_folders(path):
    # List to store folder names
    folder_names = []
    
    # Check if the path exists
    if os.path.exists(path):
        # Iterate over the items in the directory
        for item in os.listdir(path):
            # Create the full path
            item_path = os.path.join(path, item)
            # Check if the item is a directory
            if os.path.isdir(item_path):
                folder_names.append(item)
    else:
        print(f"The directory '{path}' does not exist.")
    
    return folder_names

# Get the list of folders
folders = list_folders(directory_path)

# Print the list of folder names
for folder in folders:
    print(folder)

import os
import shutil
from pathlib import Path

def flatten_soulseek_downloads(source_dir, destination_dir):
    # Create destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if file is a music file
            if file.lower().endswith(('.mp3', '.flac', '.m4a', '.wav', '.aac', '.aiff',  '.aif')):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_dir, file)
                
                # Handle duplicate filenames
                if os.path.exists(destination_path):
                    base, extension = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(destination_path):
                        new_filename = f"{base}_{counter}{extension}"
                        destination_path = os.path.join(destination_dir, new_filename)
                        counter += 1
                
                # Move the file
                shutil.move(source_path, destination_path)
                print(f"Moved: {file}")

# Example usage
source_directory = r"C:\Users\Asus\OneDrive - Universidad de los Andes\Documentos\Soulseek Downloads\complete"
destination_directory = r"C:\Users\Asus\OneDrive - Universidad de los Andes\Documentos\Soulseek Downloads\all_files"

flatten_soulseek_downloads(source_directory, destination_directory)
import os
import shutil

# Define the paths
genres_file_path = r"C:\Users\Asus\OneDrive - Universidad de los Andes\Documentos\Personal Projects\music automation\genres.txt"
source_directory = r"C:\Users\Asus\OneDrive - Universidad de los Andes\Documentos\Soulseek Downloads\all_files"
music_library_directory = r"C:\Users\Asus\OneDrive - Universidad de los Andes\Documentos\DJ\Music library"

# Specify the audio file extensions to look for
audio_extensions = ('.flac', '.aiff', '.aif', '.mp3')

# Function to move files based on genres
def move_files_by_genre():
    # Read the genres and file names from genres.txt
    with open(genres_file_path, 'r', encoding='utf-8') as genres_file:
        lines = genres_file.readlines()
    
    # Create a dictionary to hold genre and respective files
    genre_files = {}

    for line in lines:
        # Split the line into the track name and genre
        parts = line.rsplit(":", 1)  # Split from the right to isolate genre
        if len(parts) == 2:
            track_info = parts[0].strip()  # Track name and artist
            genre = parts[1].strip()  # Genre
            
            # Extract just the track name for file searching
            file_name = track_info.split(",")[0].strip()  # Get the track name before any comma

            # Add the file name to the corresponding genre in the dictionary
            if genre not in genre_files:
                genre_files[genre] = []
            genre_files[genre].append(file_name)

    # Move the files to their respective genre folders
    for genre, files in genre_files.items():
        # Create the genre directory if it does not exist
        genre_folder_path = os.path.join(music_library_directory, genre)
        os.makedirs(genre_folder_path, exist_ok=True)

        for file_name in files:
            # Check for files with the specified extensions in the source directory
            found_file = False
            for extension in audio_extensions:
                source_file_path = os.path.join(source_directory, file_name + extension)
                if os.path.isfile(source_file_path):
                    # Move the file to the genre folder
                    shutil.move(source_file_path, genre_folder_path)
                    print(f'Moved: {file_name + extension} to {genre_folder_path}')
                    found_file = True
                    break  # Exit the loop once the file is found and moved
            
            # If the file is not found, print the message
            if not found_file:
                print(f'File not found: {file_name} with any known extension')

# Execute the function
if __name__ == "__main__":
    move_files_by_genre()


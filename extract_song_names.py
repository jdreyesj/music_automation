import os
from mutagen import File

def extract_metadata(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return None

    # Extracting metadata
    audio = File(file_path)

    # Get the title; if not found, leave it as None
    title = audio.tags.get('title', [None])[0] if audio.tags else None

    # Get the author (artist); if not found, leave it as None
    author = audio.tags.get('artist', [None])[0] if audio.tags else None

    return title, author

def main():
    # Directory containing audio files
    audio_directory = r"C:\Users\Asus\OneDrive - Universidad de los Andes\Documentos\Soulseek Downloads\all_files"
    
    # Directory where the script is located (and where we want to save the output)
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Supported audio file extensions
    audio_extensions = ('.flac', '.aiff', '.aif', '.mp3')

    # List to hold audio files
    audio_files = []

    # Iterate through the directory to find audio files
    for filename in os.listdir(audio_directory):
        if filename.endswith(audio_extensions):
            audio_files.append(os.path.join(audio_directory, filename))

    # Prepare output for the text file
    output_lines = []

    # Extract title and author from each audio file
    for file_path in audio_files:
        title, author = extract_metadata(file_path)
        file_name = os.path.splitext(os.path.basename(file_path))[0]  # Extract file name without extension
        
        # Conditional output
        if title is None and author is None:
            line = f"File: {file_name}"  # Only the file name if no title and author
        else:
            # Include title and author if available
            title_output = title if title is not None else ""
            author_output = author if author is not None else ""
            line = f"File: {file_name}, Title: {title_output}, Author: {author_output}"

        # Print to console
        print(line)
        
        # Append the line to the output list for writing to the text file
        output_lines.append(line)

    # Write the results to a text file in the same directory as the script
    output_file_path = os.path.join(script_directory, "audio_metadata_output.txt")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in output_lines:
            output_file.write(line + '\n')

    print(f"\nMetadata has been written to: {output_file_path}")

if __name__ == "__main__":
    main()

import py7zr
import os

def uncompress_7z(archive_path, extract_path="extracted_7z"):
    """
    Uncompresses a .7z archive to the specified extraction path using py7zr.

    Args:
        archive_path (str): The path to the .7z archive file.
        extract_path (str, optional): The directory where the contents will be extracted.
                                     Defaults to "extracted_7z" in the current directory.
    """
    try:
        with py7zr.SevenZipFile(archive_path, 'r') as archive:
            os.makedirs(extract_path, exist_ok=True)  # Create the extraction directory if it doesn't exist
            archive.extractall(extract_path)
        print(f"Successfully extracted '{archive_path}' to '{extract_path}'.")
    except FileNotFoundError:
        print(f"Error: 7z archive not found at '{archive_path}'.")
    except py7zr.Bad7zFile:
        print(f"Error: '{archive_path}' is not a valid 7z file or is corrupted.")
    except Exception as e:
        print(f"An error occurred during uncompression: {e}")

if __name__ == "__main__":
    archive_to_uncompress = "your_archive.7z"  # Replace with the actual path to your .7z file
    extraction_directory = "uncompressed_content"  # Replace with your desired extraction directory

    uncompress_7z(archive_to_uncompress, extraction_directory)
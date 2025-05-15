import zipfile
import os

def unzip_archive(zip_filepath, extract_path="extracted_files"):
    """
    Unzips a ZIP archive to the specified extraction path.

    Args:
        zip_filepath (str): The path to the ZIP archive file.
        extract_path (str, optional): The directory where the contents will be extracted.
                                     Defaults to "extracted_files" in the current directory.
    """
    try:
        with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
            os.makedirs(extract_path, exist_ok=True)  # Create the extraction directory if it doesn't exist
            zip_ref.extractall(extract_path)
        print(f"Successfully extracted '{zip_filepath}' to '{extract_path}'.")
    except FileNotFoundError:
        print(f"Error: ZIP file not found at '{zip_filepath}'.")
    except zipfile.BadZipFile:
        print(f"Error: '{zip_filepath}' is not a valid ZIP file or is corrupted.")
    except Exception as e:
        print(f"An error occurred during unzipping: {e}")

if __name__ == "__main__":
    archive_to_unzip = "full_archive.zip"  # Replace with the actual path to your ZIP file
    extraction_directory = "unzipped_content"  # Replace with your desired extraction directory

    unzip_archive(archive_to_unzip, extraction_directory)
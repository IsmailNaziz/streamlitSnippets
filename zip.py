import os
import zipfile

def concatenate_split_zip(parent_folder, file_prefix, output_filename):
    """
    Concatenates split ZIP archive chunks using Python's zipfile module.

    Args:
        parent_folder (str): The path to the folder containing the split ZIP files.
        file_prefix (str): The common prefix of the split ZIP files
                           (e.g., 'my_archive.zip').
        output_filename (str): The desired name for the final concatenated ZIP archive.
    """
    chunk_files = sorted([
        os.path.join(parent_folder, f)
        for f in os.listdir(parent_folder)
        if f.startswith(file_prefix + ".") and f.split(".")[-1].isdigit()
    ], key=lambda x: int(x.split(".")[-1]))

    if not chunk_files:
        print(f"No chunk files found with prefix '{file_prefix}' in '{parent_folder}'.")
        return

    with open(output_filename, 'wb') as outfile:
        for chunk_file in chunk_files:
            print(f"Processing chunk: {chunk_file}")
            with open(chunk_file, 'rb') as infile:
                outfile.write(infile.read())

    print(f"\nSuccessfully concatenated to '{output_filename}'.")

if __name__ == "__main__":
    parent_dir = "/path/to/your/chunks"  # Replace with the actual path to the folder
    prefix = "my_file.zip"             # Replace with the actual prefix of your chunk files
    output_file = "full_archive.zip"      # Replace with your desired output filename

    concatenate_split_zip(parent_dir, prefix, output_file)
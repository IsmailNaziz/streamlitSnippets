import py7zr
import os

def concatenate_7zip_chunks(input_prefix, output_filename):
    """
    Concatenates 7-Zip split archive chunks created by 7-Zip on Windows
    using py7zr.

    Args:
        input_prefix (str): The common prefix of the split archive files
                            (e.g., 'myarchive.7z.').
        output_filename (str): The desired name for the final concatenated archive.
    """
    chunk_files = sorted([f for f in os.listdir('.') if f.startswith(input_prefix)])

    if not chunk_files:
        print(f"No chunk files found with the prefix '{input_prefix}'.")
        return

    with py7zr.SevenZipFile(output_filename, 'w') as outfile:
        for chunk_file in chunk_files:
            print(f"Processing chunk: {chunk_file}")
            with py7zr.SevenZipFile(chunk_file, 'r') as infile:
                for member in infile.getnames():
                    outfile.copy(infile, member)

    print(f"\nSuccessfully concatenated to '{output_filename}'.")

if __name__ == "__main__":
    prefix = "myarchive.7z."  # Replace with the actual prefix of your chunk files
    output_file = "full_archive.7z"  # Replace with your desired output filename
    concatenate_7zip_chunks(prefix, output_file)
import os

def save_temp_file(file_bytes: bytes, filename: str) -> str:
    """
    Save a temporary file to the 'temp/' directory.

    Args:
        file_bytes (bytes): The content of the uploaded file.
        filename (str): The desired filename.

    Returns:
        str: The full path to the saved temporary file.
    """
    # Define the temp directory path
    temp_dir = os.path.join(os.getcwd(), "temp")

    # Ensure the 'temp/' directory exists
    os.makedirs(temp_dir, exist_ok=True)

    # Build the full path for the temporary file
    temp_file_path = os.path.join(temp_dir, filename)

    # Write the bytes to the file
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(file_bytes)

    return temp_file_path

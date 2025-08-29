from pathlib import Path

def write_file(file_name, file_content):
    """
    Creates or overwrites a text file and writes content.
    Supports both string paths and Path objects.
    """
    file_path = Path(file_name).with_suffix(".txt")
    with open(file_path, "w") as file:
        file.write(file_content)
    pass

def append_file(file_name, append_content):
    """
    Appends content to a text file. Creates the file if it doesn't exist.
    Supports both string paths and Path objects.
    """
    file_path = Path(file_name).with_suffix(".txt")
    with open(file_path, "a") as file:
        file.write(append_content)
    pass

def read_file(file_name):
    """
    Reads and returns the content of a text file.
    Supports both string paths and Path objects.
    """
    file_path = Path(file_name).with_suffix(".txt")
    with open(file_path, "r") as file:
        content = file.read()
    return content
    pass

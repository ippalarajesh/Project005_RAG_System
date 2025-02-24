# utils/file_handler.py

def read_file(filename):
    """Read contents of a file."""
    with open(filename, "r") as file:
        return file.read()

def write_file(filename, data):
    """Write data to a file."""
    with open(filename, "w") as file:
        file.write(data)

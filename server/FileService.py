import os

def change_dir(path):
    if os.path.isdir(path):
        print("Current working directory: {0}".format(os.getcwd()))
        os.chdir(path)
        print("Current working directory after parse: {0}".format(os.getcwd()))
    else:
        print("Current working directory: {0}".format(os.getcwd()))
        os.makedirs(path)
        os.chdir(path)
        print("Current working directory after parse: {0}".format(os.getcwd()))
    pass


def get_files():
    """Get info about all files in working directory.

    Returns:
        List of dicts, which contains info about each file. Keys:
        - name (str): filename
        - create_date (datetime): date of file creation.
        - edit_date (datetime): date of last file modification.
        - size (int): size of file in bytes.
    """

    pass


def get_file_data(filename):
    """Get full info about file.

    Args:
        filename (str): Filename.

    Returns:
        Dict, which contains full info about file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - edit_date (datetime): date of last file modification
        - size (int): size of file in bytes

    Raises:
        RuntimeError: if file does not exist.
        ValueError: if filename is invalid.
    """

    pass


def create_file(filename, content=None):
    """Create a new file.

    Args:
        filename (str): Filename.
        content (str): String with file content.

    Returns:
        Dict, which contains name of created file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - size (int): size of file in bytes

    Raises:
        ValueError: if filename is invalid.
    """

    pass


def delete_file(filename):
    """Delete file.

    Args:
        filename (str): filename

    Raises:
        RuntimeError: if file does not exist.
        ValueError: if filename is invalid.
    """

    pass

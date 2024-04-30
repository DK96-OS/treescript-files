"""File Validation Methods.
    These Methods all raise SystemExit exceptions.
"""
from pathlib import Path
from sys import exit

from .string_validation import validate_name


def validate_input_file(file_name: str) -> str:
    """
    Read the Input File, Validate (non-blank) data, and return Input str.

    Parameters:
    - file_name (str): The Name of the Input File.

    Returns:
    str - The String Contents of the Input File.

    Raises:
    SystemExit - If the File does not exist, or is empty or blank, or read failed.
    """
    file_path = Path(file_name)
    if not file_path.exists():
        exit("The Input File does not Exist.")
    try:
        data = file_path.read_text()
    except IOError as e:
        exit("Failed to Read from File.")
    if validate_name(data):
        return data
    exit("Input was Empty")

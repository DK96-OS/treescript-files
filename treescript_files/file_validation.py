""" File Validation Methods.
 - The Methods raise SystemExit and TypeError exceptions.
"""
from pathlib import Path
from sys import exit

from treescript_files.string_validation import validate_name


def validate_input_file(
    file_name: str,
) -> str:
    """ Read the Input File, Validate (non-blank) data, and return Input str.

**Parameters:**
 - file_name (str): The Name of the Input File. The Path string.

**Returns:**
 str - The String Contents of the Input File.

**Raises:**
 TypeError - If the file_name argument is not a string.
 SystemExit - If the File does not exist, or is empty or blank, or read failed.
    """
    if not isinstance(file_name, str):
        raise TypeError
    if not (file_path := Path(file_name)).exists():
        exit("The Input File does not Exist.")
    try:
        if validate_name(data := file_path.read_text()):
            return data
    except OSError:
        exit("Failed to Read from File.")
    exit("Input was Empty or Invalid.")

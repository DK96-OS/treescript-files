"""String Validation Methods.
"""
from typing import Literal


def validate_name(argument) -> bool:
    """
    Determine whether an argument is a non-empty string.
        Does not count whitespace.
        Uses the strip method to remove empty space.

    Parameters:
    - argument (str) : The given argument.

    Returns:
    bool - True if the argument qualifies as valid.
    """
    if argument is None or not isinstance(argument, str):
        return False
    elif len(argument.strip()) < 1:
        return False
    return True


def validate_data_label(data_label: str) -> bool:
    """
    Determine whether a Data Label is Valid.

    Parameters:
    - data_label (str): The String to check for validity.

    Returns:
    bool - Whether the String is a valid Data Label.
    """
    if not 0 < len(data_label) < 100:
        return False
    if '/' in data_label or '\\' in data_label:
        return False
    # Remove Dash Characters
    if '-' in data_label:
        data_label = data_label.replace('-', '')
    # Remove Underscore Characters
    if '_' in data_label:
        data_label = data_label.replace('_', '')
    # Remove Dot Characters
    if '.' in data_label:
        data_label = data_label.replace('.', '')
    if '!' == data_label:
        return True
    # All Remaining Characters must be alphanumeric
    return data_label.isalnum()


def validate_dir_name(dir_name: str) -> str | None:
    """
    Determine that a directory is correctly formatted.
        This method should be called once for each slash type.

    Parameters:
    - dir_name (str): The given input to be validated.

    Returns:
    str | None - The valid directory name, or none if it may be a file.

    Raises:
    ValueError - When the name is not suitable for directories or files.
    """
    # Keep Name Length Reasonable
    if (name_length := len(dir_name)) >= 100:
        raise ValueError(f'Name too Long!: {name_length}')
    # Check for slash characters
    if (name := _filter_slash_chars(dir_name)) is not None:
        # Is a Dir
        if len(name) == 0:
            raise ValueError('The name is empty')
        # Check for invalid characters (parent dir, current dir)
        if name in ['.', '..']:
            raise ValueError('Invalid Directory')
        return name
    # Is a File
    return None


def _validate_slash_char(dir_name: str) -> Literal['\\', '/'] | None:
    """
    Determine which slash char is used by the directory, if it is a directory.
        Discourages use of both slash chars, by raising ValueError.

    Parameters:
    - dir_name (str): The given input to be validated.

    Returns:
    str | None - The slash character used, or none if no chars were found.

    Raises:
    ValueError - When the name contains both slash characters.
    """
    slash = None
    if '/' in dir_name:
        slash = '/'
    if '\\' in dir_name:
        if slash is not None:
            raise ValueError('Invalid Directory slash character combination.')
        slash = '\\'
    return slash


def _filter_slash_chars(dir_name: str) -> str | None:
    """
    Remove all of the slash characters and return the directory name.
        Returns None when there are no slash characters found.
        Raises ValueError when slash characters are used improperly.

    Parameters:
    - dir_name (str): The given input to be validated.

    Returns:
    str | None - The valid directory name, or none if it may be a file.

    Raises:
    ValueError - When the name is not suitable for directories or files.
    """
    slash = _validate_slash_char(dir_name)
    if slash is None:
        return None
    if dir_name.endswith(slash) or dir_name.startswith(slash):
        name = dir_name.strip(slash)
        # Check for internal slash characters
        if slash in name:
            raise ValueError('Multi-dir line detected')
    else:
        # Found slash chars only within the node name (multi-dir line)
        raise ValueError('Multi-dir line detected')
    return name

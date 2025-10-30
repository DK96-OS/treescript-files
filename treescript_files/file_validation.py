""" File Validation Methods.
 - The Methods raise SystemExit and TypeError exceptions.
"""
from pathlib import Path
from sys import exit


_FILE_SIZE_LIMIT = 8 * 1024**2 # 8 MB
_FILE_SIZE_LIMIT_ERROR_MSG = "File larger than 8 MB Limit."
_FILE_SYMLINK_DISABLED_MSG = "Symlink file paths are disabled."

_FILE_DOES_NOT_EXIST_MSG = "The File does not Exist."
_FILE_READ_OSERROR_MSG = "Failed to Read from File."
_FILE_EMPTY_MSG = 'The Input File is Empty.'


def validate_input_file(
    file_name: str,
    file_size_limit: int = _FILE_SIZE_LIMIT,
) -> str | None:
    """ Read the Input File, Validate (non-blank) data, and return Input str.
 - Max FileSize is 8 MB by default.
 - Symlink type file paths are disabled.

**Parameters:**
 - file_name (str): The Name of the Input File.

**Returns:**
 str? - The String Contents of the Input File.

**Raises:**
 SystemExit - If the File does not exist, or is empty or blank, or read failed.
    """
    try:
        if not (file_path := Path(file_name)).exists():
            exit(_FILE_DOES_NOT_EXIST_MSG)
        if file_path.is_symlink():
            exit(_FILE_SYMLINK_DISABLED_MSG)
        if file_path.lstat().st_size > file_size_limit:
            exit(_FILE_SIZE_LIMIT_ERROR_MSG)
        if (data := file_path.read_text()) is not None:
            if len(data.strip()) > 0:
                return data
            exit(_FILE_EMPTY_MSG)
        # Fallthrough: return None
    except OSError:
        exit(_FILE_READ_OSERROR_MSG)
    return None

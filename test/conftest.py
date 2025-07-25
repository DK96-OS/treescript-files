""" Test Fixtures and Data Providers.
"""


def create_depth(depth: int) -> str:
    """ Creates a string of space chars equivalent to the given depth.

**Parameters:**
 - depth (int): The amount of depth in the Tree Node Structure.

**Returns:**
 str - The String of Space Char, of the required length.
	"""
    # Two space characters per unit of depth
    return '  ' * depth


def raise_exception(name: str):
    """ Raise an Exception in a mock method.
 - Argument is lowercased before matching.

**Available Exceptions:**
 - OSError
 - IOError
 - SystemExit
 - ValueError
 - TypeError
 - BaseException
    """
    match name.lower():
        case 'oserror':
            raise OSError
        case 'ioerror':
            raise IOError
        case 'systemexit':
            raise SystemExit
        case 'valueerror':
            raise ValueError
        case 'typeerror':
            raise TypeError
        case 'baseexception':
            raise BaseException

""" Test Fixtures and Data Providers.
"""
import pytest


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


@pytest.fixture
def temp_cwd():
    """ Creates a Temporary Working Directory for Git subprocesses.
    """
    from tempfile import TemporaryDirectory
    tdir = TemporaryDirectory()
    from os import getcwd, chdir
    initial_cwd = getcwd()
    chdir(tdir.name)
    yield tdir
    chdir(initial_cwd)
    tdir.cleanup()


class PrintCollector:  # Author: DK96-OS
    def __init__(self):
        self.collection: str = ''

    def get_output(self) -> str:
        return self.collection

    def append_print_output(self, output: str):
        self.collection = self.collection + output

    def assert_expected(self, expected: str):
        assert self.collection == expected

    def get_mock_print(self):
        def _collection(result, **kwargs):
            self.append_print_output(result)

        return _collection

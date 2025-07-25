""" Test Fixtures and Data Providers.
"""
import pytest


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

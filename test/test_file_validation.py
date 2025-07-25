""" Testing File Validation Methods.
"""
import pytest
from pathlib import Path

from test.conftest import raise_exception
from treescript_files.file_validation import validate_input_file


@pytest.mark.parametrize(
    "test_input,expect",
    [
        ("file_name", "file_data"),
        ("file_name12", "file_data"),
    ]
)
def test_validate_input_file_returns_data(test_input, expect):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: "file_data")
        assert validate_input_file(test_input) == expect


def test_validate_input_file_does_not_exist_raises_exit():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: False)
        with pytest.raises(SystemExit):
            validate_input_file("file_name")


def test_validate_input_file_is_empty_raises_exit():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: "")
        with pytest.raises(SystemExit):
            validate_input_file("file_name")


def test_validate_input_file_fails_to_read_raises_exit():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: raise_exception('ioerror'))
        with pytest.raises(SystemExit):
            validate_input_file("file_name")


def test_validate_input_file_os_error_raises_exit():
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: raise_exception('oserror'))
        with pytest.raises(SystemExit, match='Failed to Read from File.'):
            validate_input_file("file_name")


@pytest.mark.parametrize(
    "test_input,expect",
    [
        ("file_name", "file_data"),
        ("file_name12", "file_data"),
    ]
)
def test_validate_input_file_is_empty_returns_none(test_input, expect):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: expect)
        assert validate_input_file(test_input) == expect

""" Testing File Validation Methods.
"""
import os

import pytest
from pathlib import Path

from test.conftest import raise_exception
from treescript_files import file_validation
from treescript_files.file_validation import validate_input_file


@pytest.mark.parametrize(
    "input_file_name,expected_result",
    [
        ("file_name", "file_data"),
        ("file_name12", "file_data"),
    ]
)
def test_validate_input_file_returns_data(tmp_path, input_file_name, expected_result):
    os.chdir(tmp_path)
    (input_file_path := tmp_path / input_file_name).touch()
    input_file_path.write_text(expected_result)
    assert validate_input_file(input_file_name) == expected_result


def test_validate_input_file_does_not_exist_raises_exit(tmp_path):
    os.chdir(tmp_path)
    with pytest.raises(SystemExit, ):
        validate_input_file("file_name")


def test_validate_input_file_is_empty_raises_exit(tmp_path):
    os.chdir(tmp_path)
    (tmp_path / 'file_name').touch()
    with pytest.raises(SystemExit, match=file_validation._FILE_EMPTY_MSG):
        validate_input_file("file_name")


def test_validate_input_file_io_error_raises_exit(tmp_path):
    os.chdir(tmp_path)
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: raise_exception('ioerror'))
        with pytest.raises(SystemExit, match=file_validation._FILE_READ_OSERROR_MSG):
            validate_input_file("file_name")


def test_validate_input_file_os_error_raises_exit(tmp_path):
    os.chdir(tmp_path)
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: raise_exception('oserror'))
        with pytest.raises(SystemExit, match=file_validation._FILE_READ_OSERROR_MSG):
            validate_input_file("file_name")

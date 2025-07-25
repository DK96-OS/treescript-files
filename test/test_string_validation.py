""" Testing String Validation Methods.
"""
import pytest

from treescript_files.string_validation import validate_name, validate_dir_name


@pytest.mark.parametrize(
    "test_input,expect",
    [
        (None, False),
        (4, False),
        ({}, False),
        ([], False),
        ("", False),
        (" ", False),
        ("\n", False),
    ]
)
def test_validate_name_returns_false(test_input, expect):
    assert validate_name(test_input) == expect


@pytest.mark.parametrize(
    "test_input,expect",
    [
        ("1", True),
        ("a", True),
        ("test", True),
    ]
)
def test_validate_name_returns_true(test_input, expect):
    assert validate_name(test_input) == expect


@pytest.mark.parametrize(
    "test_input",
    [
        "1",
        "a",
        "test",
    ]
)
def test_validate_dir_name_no_slash_chars_returns_none(test_input):
    assert validate_dir_name(test_input) is None


@pytest.mark.parametrize(
    "test_input,expect",
    [
        ("a/", 'a'),
        ("abc/", 'abc'),
        ("a1/", 'a1'),
    ]
)
def test_validate_dir_name_is_valid_returns_name(test_input, expect):
    assert expect == validate_dir_name(test_input)


@pytest.mark.parametrize(
    "test_input",
    [
        "a/b/",
        "abc/d/",
        "test/dir",
    ]
)
def test_validate_dir_name_multi_dir_line_raises_value_error(test_input):
    with pytest.raises(ValueError):
        validate_dir_name(test_input)

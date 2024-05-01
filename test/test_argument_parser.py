"""Testing Argument Parser Module Methods.
"""
import pytest
from treescript_files.argument_parser import _validate_arguments, parse_arguments


def test_parse_arguments_empty_arguments_raises_exit():
    try:
        parse_arguments([])
        assert False
    except SystemExit as e:
        assert True


def test_parse_arguments_valid_args_returns_data():
    tree_file_name = 'script.tree'
    result = parse_arguments([tree_file_name])
    assert result.tree_file == tree_file_name
    assert result.parent_path is None


def test_parse_arguments_parent_path_returns_data():
    tree_file_name = 'script.tree'
    parent_path = '~/project/'
    result = parse_arguments([tree_file_name, parent_path])
    assert result.tree_file == tree_file_name
    assert result.parent_path == parent_path


def test_parse_arguments_parent_path_returns_data():
    tree_file_name = 'script.tree'
    parent_path = '~/project/'
    result = parse_arguments([tree_file_name, '--parent', parent_path])
    assert result.tree_file == tree_file_name
    assert result.parent_path == parent_path


def test_parse_arguments_parent_path_returns_data():
    tree_file_name = 'script.tree'
    parent_path = '~/project/'
    result = parse_arguments([tree_file_name, '--parent', parent_path])
    assert result.tree_file == tree_file_name
    assert result.parent_path == parent_path


def test_parse_arguments_invalid_args_raises_exit():
    try:
        parse_arguments(['asd', 'egwe', 'wef'])
        assert False
    except SystemExit as e:
        assert True


def test_validate_arguments_empty_tree_file_name_raises_exit():
    try:
        _validate_arguments('', None)
        assert False
    except SystemExit as e:
        assert True


def test_validate_arguments_empty_parent_path_raises_exit():
    try:
        _validate_arguments('tree', '')
        assert False
    except SystemExit as e:
        assert True


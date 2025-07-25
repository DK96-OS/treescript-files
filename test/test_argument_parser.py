""" Testing Argument Parser Module Methods.
"""
import pytest

from treescript_files.argument_data import ArgumentData
from treescript_files.argument_parser import _validate_arguments, parse_arguments


def test_parse_arguments_valid_args_returns_data():
    tree_file_name = 'script.tree'
    result = parse_arguments([tree_file_name])
    assert result.tree_file == tree_file_name
    assert result.parent_path is None
    assert result.separator =='\n'


def test_parse_arguments_parent_path_returns_data():
    tree_file_name = 'script.tree'
    parent_path = '~/project/'
    result = parse_arguments([tree_file_name, '--parent', parent_path])
    assert result.tree_file == tree_file_name
    assert result.parent_path == parent_path
    assert result.separator =='\n'


@pytest.mark.parametrize(
    "test_input,expect",
    [
        (['script.tree', '--space'], ArgumentData('script.tree', None, ' ')),
        (['script.tree', '-s'], ArgumentData('script.tree', None, ' ')),
        (['script.tree', '--comma'], ArgumentData('script.tree', None, ',')),
        (['script.tree', '-c'], ArgumentData('script.tree', None, ',')),
        (['script.tree', '--tab'], ArgumentData('script.tree', None, '\t')),
        (['script.tree', '-t'], ArgumentData('script.tree', None, '\t')),
    ]
)
def test_parse_arguments_output_separator_options(test_input,expect):
    assert expect == parse_arguments(test_input)


@pytest.mark.parametrize(
    "test_input",
    [
        (['script.tree', '~/project/']),
        (['script.tree', '~']),
    ]
)
def test_parse_arguments_parent_path_missing_flag_raises_exit(test_input):
    with pytest.raises(SystemExit):
        parse_arguments(test_input)


@pytest.mark.parametrize(
    "test_input",
    [
        (['--parent', '~/project/']),
        (['--space']),
        (['--comma']),
        (['--tab']),
    ]
)
def test_parse_arguments_no_tree_raises_exit(test_input):
    with pytest.raises(SystemExit):
        parse_arguments(test_input)


@pytest.mark.parametrize(
    "test_input",
    [
        ([]),
        (['']),
        (['asd', 'egwe', 'wef']),
    ]
)
def test_parse_arguments_invalid_args_raises_exit(test_input):
    with pytest.raises(SystemExit):
        parse_arguments(test_input)


def test_validate_arguments_empty_tree_file_name_raises_type_error():
    with pytest.raises(TypeError):
        _validate_arguments('', None)


def test_validate_arguments_empty_parent_path_raises_type_error():
    with pytest.raises(TypeError):
        _validate_arguments('tree', '')

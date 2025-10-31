""" Testing Tree Reader and Process Input Data Method
"""
from re import escape

import pytest

from treescript_files import line_reader, generate_treescript_files
from treescript_files.input_data import InputData
from treescript_files.tree_reader import process_input_data


def test_process_input_data_single_file_no_parent_path_returns_valid_path():
    input_data = InputData(
        tree_input='src/\n  file.py',
        parent_path=None
    )
    result = list(process_input_data(input_data))
    assert len(result) == 1
    assert result[0] in ['src/file.py', 'src\\file.py']


def test_process_input_data_invalid_indentation_raises_exit():
    input_data = InputData(
        tree_input='src/\n file.py',
        parent_path=None
    )
    with pytest.raises(SystemExit, match=escape(line_reader._INVALID_DEPTH_ERROR_MSG)):
        list(process_input_data(input_data))


@pytest.mark.parametrize(
    'parent_path', [
        'module/',
        'module',
        'module\\',
    ]
)
def test_process_input_data_parametrized_parent_path_returns_valid_path(parent_path: str):
    input_data = InputData(
        tree_input='src/\n  file.py',
        parent_path=parent_path,
    )
    result = list(process_input_data(input_data))
    assert len(result) == 1
    assert result[0] in ['module/src/file.py', 'module\\src\\file.py']


@pytest.mark.parametrize(
    'parent_path', [
        'project/module/main/',
        'project/module/main',
        'project\\module\\main\\',
        'project\\module\\main',
    ]
)
def test_process_input_data_parametrized_parent_path_long_returns_valid_path(parent_path: str):
    input_data = InputData(
        tree_input='src/\n  file.py',
        parent_path=parent_path,
    )
    result = list(process_input_data(input_data))
    assert len(result) == 1
    assert result[0] in ['project/module/main/src/file.py', 'project\\module\\main\\src\\file.py']


@pytest.mark.parametrize(
    'parent_path', [
        '/project/module/main/',
        '/project/module/main',
        '\\project\\module\\main\\',
        '\\project\\module\\main',
    ]
)
def test_process_input_data_parametrized_parent_path_long_with_start_slash_returns_valid_path(parent_path: str):
    input_data = InputData(
        tree_input='src/\n  file.py',
        parent_path=parent_path,
    )
    result = list(process_input_data(input_data))
    assert len(result) == 1
    assert result[0] in ['/project/module/main/src/file.py', '\\project\\module\\main\\src\\file.py']


@pytest.mark.parametrize(
    'parent_path', [
        './project/module/main/',
        './project/module/main',
        '.\\project\\module\\main\\',
        '.\\project\\module\\main',
    ]
)
def test_process_input_data_parametrized_parent_path_long_in_cwd_returns_valid_path(parent_path: str):
    input_data = InputData(
        tree_input='src/\n  file.py',
        parent_path=parent_path,
    )
    result = list(process_input_data(input_data))
    assert len(result) == 1
    assert result[0] in ['./project/module/main/src/file.py', '.\\project\\module\\main\\src\\file.py']


@pytest.mark.parametrize(
    'parent_path', [
        '../project/module/main/',
        '../project/module/main',
        '..\\project\\module\\main\\',
        '..\\project\\module\\main',
    ]
)
def test_process_input_data_parametrized_parent_path_long_in_parent_dir_returns_valid_path(parent_path: str):
    input_data = InputData(
        tree_input='src/\n  file.py',
        parent_path=parent_path,
    )
    result = list(process_input_data(input_data))
    assert len(result) == 1
    assert result[0] in ['../project/module/main/src/file.py', '..\\project\\module\\main\\src\\file.py']


def test_process_input_data_two_files_returns_valid_paths():
    input_data = InputData(
        tree_input='src/\n  file.py\n  file2.py',
        parent_path=None,
    )
    result = list(process_input_data(input_data))
    assert len(result) == 2
    assert result[0] in ['src/file.py', 'src\\file.py']
    assert result[1] in ['src/file2.py', 'src\\file2.py']


@pytest.mark.parametrize(
    'parent_path', [
        'module/',
        'module',
        'module\\',
    ]
)
def test_process_input_data_two_files_parent_path_returns_valid_paths(parent_path: str):
    input_data = InputData(
        tree_input='src/\n  file.py\n  file2.py',
        parent_path=parent_path,
    )
    result = list(process_input_data(input_data))
    assert len(result) == 2
    assert result[0] in ['module/src/file.py', 'module\\src\\file.py']
    assert result[1] in ['module/src/file2.py', 'module\\src\\file2.py']


@pytest.mark.parametrize(
    'parent_path', [
        'module/',
        'module',
        'module\\',
    ]
)
def test_generate_treescript_files_parametrized_parent_path_returns_valid_paths(parent_path: str):
    generator = generate_treescript_files(
        treescript_file='src/\n  file.py\n  file2.py DataLabel # Comment',
        parent_path=parent_path,
    )
    result = list(generator)
    assert len(result) == 2
    assert result[0] in ['module/src/file.py', 'module\\src\\file.py']
    assert result[1] in ['module/src/file2.py', 'module\\src\\file2.py']


def test_generate_treescript_files_invalid_indentation_raises_exit():
    generator = generate_treescript_files(
        treescript_file='src/\n file.py',
        parent_path=None
    )
    with pytest.raises(SystemExit, match=escape(line_reader._INVALID_DEPTH_ERROR_MSG)):
        list(generator)

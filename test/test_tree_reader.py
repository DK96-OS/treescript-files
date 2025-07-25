""" Testing Tree Reader and Process Input Data Method
"""
from treescript_files.input_data import InputData
from treescript_files.tree_reader import process_input_data


def test_process_input_data_single_file():
    input_data = InputData(
        tree_input='src/\n  file.py',
        parent_path=None
    )
    result = list(process_input_data(input_data))
    assert len(result) == 1
    assert result[0] == 'src/file.py'


def test_process_input_data_parent_path():
    input_data = InputData(
        tree_input='src/\n  file.py',
        parent_path='module/'
    )
    result = list(process_input_data(input_data))
    assert len(result) == 1
    assert result[0] == 'module/src/file.py'


def test_process_input_data_two_files():
    input_data = InputData(
        tree_input='src/\n  file.py\n  file2.py',
        parent_path=None
    )
    result = list(process_input_data(input_data))
    assert len(result) == 2
    assert result[0] == 'src/file.py'
    assert result[1] == 'src/file2.py'


def test_process_input_data_two_files_parent_path():
    input_data = InputData(
        tree_input='src/\n  file.py\n  file2.py',
        parent_path='module/'
    )
    result = list(process_input_data(input_data))
    assert len(result) == 2
    assert result[0] == 'module/src/file.py'
    assert result[1] == 'module/src/file2.py'

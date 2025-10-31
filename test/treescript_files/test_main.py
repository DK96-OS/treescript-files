""" Testing Main Module.
 - Basic Integration Tests
"""
import builtins
import os
import sys
from re import escape

import pytest

from test.conftest import PrintCollector
from treescript_files import file_validation
from treescript_files.__main__ import main


TEST_INPUT_FILE_NAME = 'tree_like_file_path'


def test_main_no_args_raises_exit(tmp_path):
    sys.argv = ['treescript-files']
    os.chdir(tmp_path)
    with pytest.raises(SystemExit, match='No Arguments given.'):
        main()


def test_main_empty_input_file_raises_exit(monkeypatch, tmp_path):
    sys.argv = ['treescript-files', TEST_INPUT_FILE_NAME]
    os.chdir(tmp_path)
    (tmp_path / TEST_INPUT_FILE_NAME).touch()
    #
    with pytest.raises(SystemExit, match=escape(file_validation._FILE_EMPTY_MSG)):
        main()


def test_main_basic_input_file_returns_treescript(monkeypatch, tmp_path):
    sys.argv = ['treescript-files', TEST_INPUT_FILE_NAME]
    os.chdir(tmp_path)
    (input_file_path := tmp_path / TEST_INPUT_FILE_NAME).touch()
    input_file_path.write_text('src/\n  file.py')
    #
    collector = PrintCollector()
    monkeypatch.setattr(builtins, 'print', collector.get_mock_print())
    main()
    assert collector.collection in [
        'src/file.py',
        'src\\file.py'
    ]


def test_main_two_input_files_returns_treescript(monkeypatch, tmp_path):
    sys.argv = ['treescript-files', TEST_INPUT_FILE_NAME]
    os.chdir(tmp_path)
    (input_file_path := tmp_path / TEST_INPUT_FILE_NAME).touch()
    input_file_path.write_text('src/\n  file.py\n  file2.py')
    #
    collector = PrintCollector()
    monkeypatch.setattr(builtins, 'print', collector.get_mock_print())
    main()
    assert collector.collection in [
        'src/file.py\nsrc/file2.py',
        'src\\file.py\nsrc\\file2.py',
    ]


def test_main_large_parent_path_arg_raises_exit(tmp_path):
    sys.argv = ['treescript-files', TEST_INPUT_FILE_NAME, '--parent', './' + '/'.join(f'abc{i}' for i in range(19))]
    os.chdir(tmp_path)
    with pytest.raises(ValueError, match='ParentPath Prefix Argument Too Long.'):
        main()


def test_main_invalid_parent_path_slash_char_combination_raises_exit(tmp_path):
    sys.argv = ['treescript-files', TEST_INPUT_FILE_NAME, '--parent', './abc\\def\\']
    os.chdir(tmp_path)
    with pytest.raises(ValueError, match='Invalid Directory slash character combination.'):
        main()

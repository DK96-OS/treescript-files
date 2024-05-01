"""Testing Path Stack
"""
import pytest
from treescript_files.path_stack import PathStack


@pytest.fixture
def stack():
    return PathStack()


def test_join_stack_empty_returns_slash(stack):
    assert stack.join_stack() == ''


def test_join_stack_single_item_returns_stack(stack):
    stack.push('src')
    assert stack.join_stack() == 'src/'


def test_reduce_depth_empty_to_zero_returns_True(stack):
    assert stack.reduce_depth(0)


def test_reduce_depth_empty_to_one_returns_false(stack):
    assert not stack.reduce_depth(1)


def test_reduce_depth_single_item_same_depth_returns_true(stack):
    stack.push('src')
    assert stack.reduce_depth(1)
    assert stack.get_depth() == 1


def test_reduce_depth_single_item_less_depth_returns_true(stack):
    stack.push('src')
    assert stack.reduce_depth(0)
    assert stack.get_depth() == 0

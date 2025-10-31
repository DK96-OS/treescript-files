""" Reads the TreeData from a Generator.
"""
from pathlib import Path
from typing import Generator, Literal

from treescript_files.input_data import InputData
from treescript_files.line_reader import read_input_tree
from treescript_files.path_stack import PathStack
from treescript_files.string_validation import validate_slash_char
from treescript_files.tree_data import TreeData


def process_input_data(
    input_data: InputData,
) -> Generator[str, None, None]:
    """Process the Input Data and set-up file path generators.

**Parameters:**
 - input_data (InputData): The program input data.

**Yields:**
 str - The file path strings.
    """
    yield from generate_treescript_files(
        treescript_file=input_data.tree_input,
        parent_path=input_data.parent_path,
    )


def generate_treescript_files(
    treescript_file: str,
    parent_path: str | None
) -> Generator[str, None, None]:
    """ Process the Input Data and set-up file path generators.

**Parameters:**
 - treescript_file (str): The Input TreeScript file to translate into file path strings.
 - parent_path (str?): The ParentPath to prefix file paths with.

**Yields:**
 str - The file path strings.
    """
    file_generator = _process_tree_data(read_input_tree(treescript_file))
    if parent_path is not None:
        file_generator = _prefix_parent(parent_path, file_generator)
    return file_generator


def _process_tree_data(
    tree_data_generator: Generator[TreeData, None, None]
) -> Generator[str, None, None]:
    """ Read the TreeData to determine the File path strings.
    """
    path_stack = PathStack()
    for tree_node in tree_data_generator:
        # Check Depth Change
        if (delta := tree_node.depth - path_stack.get_depth()) > 0:
            exit(f'You have jumped {delta} steps in the tree on line: {tree_node.line_number}')
        elif delta < 0:
            path_stack.reduce_depth(tree_node.depth)
        # Process Node
        if tree_node.is_dir:
            path_stack.push(tree_node.name)
        else:
            yield path_stack.join_stack() + tree_node.name


def _prefix_parent(
    parent: str,
    input_stream: Generator[str, None, None],
    path_separator: Literal['\\', '/'] = str(Path('a/b'))[1],
) -> Generator[str, None, None]:
    """ Append a Prefix Parent Path to each file.
 - Must first ensure that the parent dir is compatible path-separator-wise.

**Parameters:**
 - parent (str): The prefix string to add to the file paths.
 - input_stream (Generator[str]): A Generator stream of file path strings.

**Yields:**
 str - The completed File path strings.
    """
    if (slash_char := validate_slash_char(parent)) != path_separator:
        if slash_char is not None:
            parent = parent.replace(slash_char, path_separator)
    # Ensure that the Prefix Ends with a Separator.
    if not parent.endswith(path_separator):
        parent += path_separator
    # Start the Generator.
    for i in input_stream:
        yield parent + i

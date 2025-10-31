""" Validated Input DataClass for TreeScript Files.
 Author: DK96-OS 2024 - 2025
"""
from dataclasses import dataclass
from typing import Generator

from .argument_data import ArgumentData
from .file_validation import validate_input_file
from .string_validation import validate_slash_char
from .tree_data import TreeData


@dataclass(frozen=True)
class InputData:
    """ The Data Class Containing Program Input.

**Fields:**
 - tree_input (str): The Tree Input to the program.
 - parent_path (str?): The Parent Path to prefix, or None. Default: None.
 - separator (str): The separator between elements in the program output. Default: Newline Character.
    """
    tree_input: str
    parent_path: str | None = None
    separator: str = '\n'

    def get_tree_data(self) -> Generator[TreeData, None, None]:
        """ Initializes a Generator for processing the Tree Input.
 - See line_reader module for more details.

**Yields:**
 TreeData - One TreeData object per Line of Tree_Input text.
        """
        from treescript_files.line_reader import read_input_tree
        return read_input_tree(self.tree_input)


def validate_arguments(argument_data: ArgumentData) -> InputData:
    """ Validate ArgumentData and return InputData.

**Parameters:**
 - argument_data (ArgumentData): The dataclass object containing Arguments to be validated and utilized towards producing the program InputData.

**Returns:**
 InputData - A frozen Dataclass containing validated program input.
    """
    # Parent Path Prefix Validation Part 1:
    if (path_prefix := argument_data.parent_path) is not None:
        if len(path_prefix) >= 100: # Keep MaxLength Reasonable
            raise ValueError('ParentPath Prefix Argument Too Long.')
        # Prevent Invalid Dir Slash Combinations
        if validate_slash_char(path_prefix) is not None:
            pass # This is handled by Validation Part 2.
        elif len(path_prefix.strip()) < 1:
            path_prefix = None # Remove blank arguments
    return InputData(
        tree_input=validate_input_file(argument_data.tree_file),
        parent_path=path_prefix,
        separator=argument_data.separator,
    )

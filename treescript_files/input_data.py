""" Validated Input DataClass for TreeScript Files.
 Author: DK96-OS 2024 - 2025
"""
from typing import Generator
from dataclasses import dataclass

from .argument_data import ArgumentData
from .file_validation import validate_input_file
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
    return InputData(
        tree_input=validate_input_file(argument_data.tree_file),
        parent_path=argument_data.parent_path,
        separator=argument_data.separator,
    )

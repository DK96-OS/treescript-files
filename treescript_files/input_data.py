"""Valid Input Data Class.
"""
from typing import Generator
from dataclasses import dataclass

from .argument_data import ArgumentData
from .file_validation import validate_input_file
from .tree_data import TreeData


@dataclass(frozen=True)
class InputData:
    """A Data Class Containing Program Input.

    Fields:
    - tree_input (str): The Tree Input to the program.
    - parent_path (str | None): The Parent Path to prefix, or None.
    - separator (str): The separator between elements in the program output.
    """

    tree_input: str
    parent_path: str | None
    separator : str = '\n'

    def get_tree_data(self) -> Generator[TreeData, None, None]:
        """
        Initializes a Generator for processing the Tree Input.
            See line_reader module for more details.

        Returns:
        Generator - Yields one TreeData for each Line of Tree Input.
        """
        from .line_reader import read_input_tree
        return read_input_tree(self.tree_input)


def validate_arguments(argument_data: ArgumentData) -> InputData:
    """Validate ArgumentData and return InputData.
    """
    return InputData(
        tree_input=validate_input_file(argument_data.tree_file),
        parent_path=argument_data.parent_path,
        separator=argument_data.separator,
    )

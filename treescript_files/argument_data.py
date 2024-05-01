"""The Arguments Received from the Command Line Input.

This DataClass is created after the argument syntax is validated.

Syntax Validation:
- The Input File is Present and non-blank.
- The Parent Path is non-blank string or None.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ArgumentData:
    """
    The syntactically valid arguments recevied by the Program.

    Fields:
    - tree_file (str): The file containing the Tree.
    - parent_path (str | None): The parent path to prefix files with.
    """

    tree_file: str
    parent_path: str | None

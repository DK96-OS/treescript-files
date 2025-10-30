""" Tree Node DataClass.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class TreeData:
    """ A DataClass representing a Tree Node.

**Fields:**
 - line_number (int): The LineNumber of the TreeData Node in the Input File.
 - depth (int): The depth in the tree.
 - is_dir (bool): Whether this Node is a directory.
 - name (str): The Name of the Tree Node.
    """
    line_number: int
    depth: int
    is_dir: bool
    name: str

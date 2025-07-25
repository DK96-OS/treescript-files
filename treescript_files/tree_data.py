""" Tree Node DataClass.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class TreeData:
    """ A DataClass representing a Tree Node.

**Fields:**
 - depth (int): The depth in the tree.
 - is_dir (bool): Whether this Node is a directory.
 - name (str): The Name of the Tree Node.
 - data_label (str): The Data Label.
    """
    line_number: int
    depth: int
    is_dir: bool
    name: str
    data_label: str

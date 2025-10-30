""" Line Reader.

The Default Input Reader.
 - Processes a single line at a time, and determines its key properties.
 - The Depth is the Integer number of directories between the current line and the root.
 - The Directory Boolean indicates whether the line represents a Directory.
 - The Name String is the name of the line.
"""
from sys import exit
from typing import Generator

from .string_validation import validate_dir_name, validate_name
from .tree_data import TreeData


_INVALID_DEPTH_ERROR_MSG = "Invalid Indentation (Number of Spaces) in Line: "
_INVALID_NODE_NAME_ERROR_MSG = "Invalid Name in Line: "


def read_input_tree(
    input_tree_data: str
) -> Generator[TreeData, None, None]:
    """ Generate structured Tree Data from the Input Data String.

**Parameters:**
 - input_tree_data (str): The Input string, which should contain TreeScript.

**Yields:**
 TreeData - Produces TreeData from the Input Data.

**Raises:**
 SystemExit - When any Line cannot be read as TreeScript successfully.
    """
    for line_number, line in enumerate(input_tree_data.splitlines(), start=1):
        if len(lstr := line.lstrip()) == 0 or lstr.startswith('#'):
            continue
        yield _process_line(line_number, line)


def _process_line(
    line_number: int,
    line: str,
) -> TreeData:
    """ Processes a single line of the input tree structure.
 - Returns a tuple indicating the depth, type (file or directory), name of file or dir, and file data if available.

**Parameters:**
 - line_number (int): The number for future reference.
 - line (str): A line from the input tree structure.

**Returns:**
 TreeData - where int is the depth, bool is true when is Directory, and str is name, followed by str data.

**Raises:**
 SystemExit - When Line cannot be read successfully.
    """
    # Remove Leading Spaces (and trailing)
    if chr(32) in (args := line.strip()):
        args = args.split(chr(32))  # Split line into words.
        name = args[0]  # First Word is the Tree Node Name.
        # Additional Words are ignored.
        is_dir, node_name = _validate_node_name(line_number, name)
    else:  # Was Not Split
        is_dir, node_name = _validate_node_name(line_number, args)
    return TreeData(
        line_number=line_number,
        depth=_calculate_depth(line_number, line),
        is_dir=is_dir,
        name=node_name,
    )


def _validate_node_name(
    line_number: int,
    node_name: str,
) -> tuple[bool, str]:
    """ Determine whether this Tree Node is a Directory, and validate the name.

**Parameters:**
 - line_number (int): Identifies the line in the input tree.
 - node_name (str): The argument received for the node name.

**Returns:**
 tuple[bool, str] - Node information: is a directory, name of node.

**Raises:**
 SystemExit - When the directory name is invalid.
    """
    try: # Check if the line contains any slash characters
        if (dir_name := validate_dir_name(node_name)) is not None:
            return True, dir_name
        # Fall-Through to File Node
    except ValueError: # An error in the dir name validation method, such that it cannot be a file either
        exit(_INVALID_NODE_NAME_ERROR_MSG + str(line_number))
    if not validate_name(node_name):
        exit(_INVALID_NODE_NAME_ERROR_MSG + str(line_number))
    return False, node_name # Is a FileNode


def _calculate_depth(
    line_number: int,
    line: str
) -> int:
    """ Calculates the depth of a line in the tree structure.

**Parameters:**
 - line_number (int): The LineNumber used for debugging invalid line indentation.
 - line (str): A line from the tree command output.

**Returns:**
 int - The depth of the line in the tree structure, or -1 if space count is invalid.
    """
    space_count = len(line) - len(line.lstrip())
    # Bit Shift Shuffle Equivalence Validation (space_count is divisible by 2)
    if (depth := space_count >> 1) << 1 != space_count:
        # Invalid Space Count! Someone made an off-by-one whitespace mistake!
        exit(_INVALID_DEPTH_ERROR_MSG + str(line_number))
    return depth

"""Initialize Test Module.
"""


def create_depth(depth: int) -> str:
    """Creates a string of space chars equivalent to the given depth.

	Parameters:
	- depth (int): The amount of depth in the Tree Node Structure.

	Returns:
	str: The String of Space Char, of the required length.
	"""
	# Two space characters per unit of depth
    return '  ' * depth

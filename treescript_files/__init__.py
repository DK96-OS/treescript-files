""" TreeScript Files Package Level Methods.
 Author: DK96-OS 2024 - 2025
"""
from treescript_files.argument_parser import parse_arguments
from treescript_files.input_data import InputData, validate_arguments
from treescript_files.tree_reader import generate_treescript_files


def ts_files(
    input_data: InputData,
) -> str:
    """ Converts TreeScript InputData into the desired Files output.

**Parameters:**
 - input_data (InputData): The program input data.

**Returns:**
 str - The String containing all of the Files, in the desired output format.
    """
    file_generator = generate_treescript_files(
        treescript_file=input_data.tree_input,
        parent_path=input_data.parent_path,
    )
    return input_data.separator.join(file_generator)


def validate_input(
    arguments: list[str],
) -> InputData:
    """ Validate the Given Arguments list using the ArgumentParser Module.

**Parameters:**
 - arguments (list[str]): The list of arguments to parse and validate.

**Returns:**
 InputData - The dataclass object containing the program input.
    """
    return validate_arguments(
        parse_arguments(arguments)
    )

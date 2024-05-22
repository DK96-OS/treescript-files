"""TreeScript Files Package Methods.
"""
from treescript_files.input_data import InputData
from treescript_files.tree_reader import process_input_data


def ts_files(
    input_data: InputData,
) -> str:
    """
    Converts TreeScript InputData into the desired Files output.

    Parameters:
    - input_data (InputData): The program input data.

    Returns:
    str - The String containing all of the Files, in the desired output format.
    """
    file_generator = process_input_data(input_data)
    return input_data.separator.join(file_generator)

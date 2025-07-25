#!/usr/bin/python


def main():
    """ TreeScript Files Main Method (Entry Point).
 Author: DK96-OS 2024 - 2025
    """
    from sys import argv
    from treescript_files import validate_input
    input_data = validate_input(argv[1:])
    #
    from treescript_files import ts_files
    output_data = ts_files(input_data)
    #
    print(output_data)


if __name__ == "__main__":
    # Get the directory of the current file (__file__ is the path to the script being executed)
    from pathlib import Path
    current_directory = Path(__file__).resolve().parent.parent
    # Add the directory to sys.path
    from sys import path
    path.append(str(current_directory))
    main()

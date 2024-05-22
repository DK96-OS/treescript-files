#!/usr/bin/python
from sys import argv, path

from treescript_files import ts_files
from treescript_files.argument_parser import parse_arguments
from treescript_files.input_data import validate_arguments


def main():
    input_data = validate_arguments(
        parse_arguments(argv[1:])
    )
    output_data = ts_files(input_data)
    print(output_data)


if __name__ == "__main__":
    from pathlib import Path
    # Get the directory of the current file (__file__ is the path to the script being executed)
    current_directory = Path(__file__).resolve().parent.parent
    # Add the directory to sys.path
    path.append(str(current_directory))
    main()

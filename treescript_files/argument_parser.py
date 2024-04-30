"""Defines and Validates Argument Syntax.

Encapsulates Argument Parser.

Returns Argument Data, the args provided by the User.
"""
from argparse import ArgumentParser
from sys import exit
from typing import Optional

from .argument_data import ArgumentData
from .string_validation import validate_name


def parse_arguments(args: Optional[list[str]] = None) -> ArgumentData:
    """
    Parse command line arguments.

    Parameters:
    - args: A list of argument strings.

    Returns:
    ArgumentData : Container for Valid Argument Data.
    """
    if args is None or len(args) == 0:
        exit("No Arguments given. ")
    # Initialize the Parser and Parse Immediately
    try:
        parsed_args = _define_arguments().parse_args(args)
    except SystemExit as e:
        exit("Unable to Parse Arguments.")
    #
    return _validate_arguments(
        parsed_args.tree_file,
        parsed_args.parent,
    )


def _validate_arguments(
    tree_file: str,
    parent_path: str | None,
) -> ArgumentData:
    """
    Checks the values received from the ArgParser.
        Uses Validate Name method from StringValidation.

    Parameters:
    - tree_file_name (str): The file name of the tree input.

    Returns:
    ArgumentData - A DataClass of syntactically correct arguments.
    """
    # Validate Tree Name Syntax
    if not validate_name(tree_file):
        exit("The Tree File argument was invalid.")
    if parent_path is not None:
        if not validate_name(parent_path):
            exit("The Parent Path argument was invalid.")
    return ArgumentData(
        tree_file=tree_file,
        parent_path=parent_path,
    )


def _define_arguments() -> ArgumentParser:
    """
    Initializes and Defines Argument Parser.
       - Sets Required/Optional Arguments and Flags.

    Returns:
    argparse.ArgumentParser - An instance with all supported Arguments.
    """
    parser = ArgumentParser(
        description="Tree Script Builder"
    )
    # Required argument
    parser.add_argument(
        'tree_file',
        type=str,
        help='The File containing the Tree Node Structure'
    )
    parser.add_argument(
        '--parent',
        type=str | None,
        default=None,
        help='The Parent Path to prefix files with.',
    )
    return parser

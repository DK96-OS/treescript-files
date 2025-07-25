""" Defines and Validates Argument Syntax.
 - Encapsulates Argument Parser.
 - Returns Argument Data, the args provided by the User.
"""
from argparse import ArgumentParser
from sys import exit

from .argument_data import ArgumentData
from .string_validation import validate_name


def parse_arguments(
    args: list[str],
) -> ArgumentData:
    """ Parse command line arguments.

**Parameters:**
 - args (list[str]): A list of argument strings.

**Returns:**
 ArgumentData - Container for Valid Argument Data.
    """
    if args is None or len(args) == 0:
        exit("No Arguments given. ")
    # Initialize the Parser and Parse Immediately
    try:
        parsed_args = _define_arguments().parse_args(args)
    except SystemExit:
        exit("Unable to Parse Arguments.")
    return _validate_arguments(parsed_args)


def _determine_output_separator(
    parsed_args,
) -> str:
    """ Given the parsed arguments object, determine the separator.

**Parameters:**
 - parsed_args (Namespace): The object returned by the ArgumentParser.

**Returns:**
 str - The separator to use between elements in the output.
    """
    if parsed_args.space:
        return ' '
    if parsed_args.tab:
        return '\t'
    if parsed_args.comma:
        return ','
    return '\n'


def _validate_arguments(
    parsed_args,
) -> ArgumentData:
    """ Checks the values received from the ArgParser.
 - Uses Validate Name method from StringValidation.

**Parameters:**
 - parsed_args : The object returned by ArgumentParser.

**Returns:**
 ArgumentData - A DataClass of syntactically correct arguments.
    """
    tree_file = parsed_args.tree_file
    parent_path = parsed_args.parent
    # Validate Tree Name Syntax
    if not validate_name(tree_file):
        exit("The Tree File argument was invalid.")
    if parent_path is not None:
        if not validate_name(parent_path):
            exit("The Parent Path argument was invalid.")
    #
    return ArgumentData(
        tree_file=tree_file,
        parent_path=parent_path,
        separator=_determine_output_separator(parsed_args)
    )


def _define_arguments() -> ArgumentParser:
    """ Initializes and Defines Argument Parser.
 - Sets Required/Optional Arguments and Flags.

**Returns:**
 argparse.ArgumentParser - An instance with all supported Arguments.
    """
    parser = ArgumentParser(
        description="TreeScript Files",
    )
    # Required argument
    parser.add_argument(
        'tree_file',
        type=str,
        help='The File containing the Tree Node Structure'
    )
    # Optional Arguments
    parser.add_argument(
        '--parent',
        type=str,
        default=None,
        help='The Parent Path to prefix files with.',
    )
    parser.add_argument(
        '--space', '-s',
        action='store_true',
        default=False,
        help='Use a space as the element separator.',
    )
    parser.add_argument(
        '--comma', '-c',
        action='store_true',
        default=False,
        help='Use a comma as the element separator.',
    )
    parser.add_argument(
        '--tab', '-t',
        action='store_true',
        default=False,
        help='Use a tab as the element separator.',
    )
    return parser

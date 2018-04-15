"""
This module is responsible for CLI argument parsing.
"""
import argparse
from src.exceptions import CLIParseError, UtilsFileDoesNotExistError
from src.utils import assert_file_existing


class CLI():
    """Use python's argparse to validate and prepare arguments.

    """
    def __init__(self):
        """Setup argument parser.

           Attributes:
               parser (argparse.ArgumentParser): parser-object.

        """
        self.parser = argparse.ArgumentParser(
            description='Downloads images specified in txt-file')
        self.parser.add_argument('-i', dest='filename', required=True,
                                 help='Path to input file', metavar='FILE',
                                 type=lambda x: assert_file_existing(x))
        self.parser.add_argument('-v', dest='verbose', help='Verbose mode',
                                 action='store_true')

    def parse(self, args):
        """Parse arguments.

           Args:
               args (str): CLI arguments.

           Returns:
               Tuple(str, bool): input-filename, verbose (default: False)

           Raises:
               UtilsFileDoesNotExistError: if input-file does not exist.
               CLIParseError: if parsing failed.

        """
        try:
            parsed_args = self.parser.parse_args(args)
        except UtilsFileDoesNotExistError:
            raise
        except SystemExit as e:
            raise CLIParseError("The commandline given was invalid")

        return parsed_args.filename, parsed_args.verbose

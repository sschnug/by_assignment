"""
This module provides the basic entry to use the program.
"""

from src.cli import CLI
from src.config_parser import read_config
from src.input_parser import InputParser
from src.downloader import Downloader


def run(argv):
    """This function is the core-function using all the other components to
       do the expected work.

       This includes parsing the commandline, reading "config.ini", parsing
       the input-file and actual downloading of all the files.

       Called by ```run.py``` in base-dir.

    """
    # Parse arguments
    arg_parser = CLI()
    input_path, verbose = arg_parser.parse(argv[1:])  # argv[0] = script-name

    # Read config-file
    output_path = read_config()

    # Create and use input-parser
    parser = InputParser(input_path, output_path, verbose)

    # Create downloader
    downloader = Downloader(output_path, verbose)

    # Use downloader
    for url, filename in parser.get_url_targetname_pairs():
        downloader.download(url, filename)

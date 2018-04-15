"""
This module provides parsing-capabilities used to grab infos from "config.ini".
"""

import configparser
from src.exceptions import (ConfigParserParseError,
                            ConfigParserParseErrorSection,
                            ConfigParserParseErrorKey)
from src.utils import assert_file_existing


def read_config(fp='config.ini'):
    """Read "config.ini" to prepare configuration.

       Args:
           fp (str): Path to config-file (default: "config.ini" in base-dir).

       Returns:
           str: output-path.

       Raises:
           ConfigParserParseError: When path is valid, but parsing fails.
           ConfigParserParseErrorSection:
               When path is valid, parsing is ok, but a necessary section is
               missing.
           ConfigParserParseErrorKey: When path is valid, parsing is ok, but a
               necessary key within a sections is missing.

    """
    assert_file_existing(fp)

    try:
        config = configparser.ConfigParser()
        config.read(fp)
    except Exception as e:
        raise ConfigParserParseError(
            'Parsing of config from "{}" failed'.format(fp))

    # Explicit checkes for current "config.ini" specification:
    # "output" section with "TARGET_DIR" key
    if 'output' not in config:
        raise ConfigParserParseErrorSection(
            'Parsing of config from "{}" failed'.format(fp))

    if 'TARGET_DIR' not in config['output']:
        raise ConfigParserParseErrorKey(
            'Parsing of config from "{}" failed'.format(fp))

    return config['output']['TARGET_DIR']

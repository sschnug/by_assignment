import unittest
import tempfile
from src.exceptions import (ConfigParserParseError,
                            ConfigParserParseErrorSection,
                            ConfigParserParseErrorKey,
                            UtilsFileDoesNotExistError)
from src.config_parser import read_config

VALID_CONFIG = b"""[output]
TARGET_DIR=example_out"""

INVALID_CONFIG_A = b"""[input]
TARGET_DIR=example_out"""

INVALID_CONFIG_B = b"""[output]
TARGET_DIR_=example_out"""

INVALID_CONFIG_C = b"""NoSectionBrackets plus a +"""


class TestConfigParserBase(unittest.TestCase):
    """Unit-testing for ConfigParser.

    """
    def setUp(self):
        """Create tempfile used as input.

        """
        self.config_file_valid_format = tempfile.NamedTemporaryFile()
        self.config_file_invalid_format_a = tempfile.NamedTemporaryFile()
        self.config_file_invalid_format_b = tempfile.NamedTemporaryFile()
        self.config_file_invalid_format_c = tempfile.NamedTemporaryFile()

        self.config_file_valid_format.write(VALID_CONFIG)
        self.config_file_valid_format.seek(0)

        self.config_file_invalid_format_a.write(INVALID_CONFIG_A)
        self.config_file_invalid_format_a.seek(0)

        self.config_file_invalid_format_b.write(INVALID_CONFIG_B)
        self.config_file_invalid_format_b.seek(0)

        self.config_file_invalid_format_c.write(INVALID_CONFIG_C)
        self.config_file_invalid_format_c.seek(0)

    def tearDown(self):
        """Close and delete tempfile.

        """
        self.config_file_valid_format.close()
        self.config_file_invalid_format_a.close()
        self.config_file_invalid_format_b.close()
        self.config_file_invalid_format_c.close()


class TestConfigParserIO(TestConfigParserBase):
    """Unit-testing config_parser: IO-cases

    """
    def test_existing_valid_file(self):
        """File given exists and is a valid config.

        """
        config = read_config(self.config_file_valid_format.name)
        self.assertEqual(config, 'example_out')

    def test_existing_invalid_file_a(self):
        """File given exists and is an invalid config (section output missing).

        """
        with self.assertRaises(ConfigParserParseErrorSection):
            config = read_config(self.config_file_invalid_format_a.name)

    def test_existing_invalid_file_b(self):
        """File given exists and is an invalid config (key TARGET_DIR missing).

        """
        with self.assertRaises(ConfigParserParseErrorKey):
            config = read_config(self.config_file_invalid_format_b.name)

    def test_existing_invalid_file_c(self):
        """File given exists and is an invalid config (parser fails).

        """
        with self.assertRaises(ConfigParserParseError):
            config = read_config(self.config_file_invalid_format_c.name)


class TestConfigParserParsing(TestConfigParserBase):
    """Unit-testing config_parser: Parsing-cases

    """
    def test_non_existing_file(self):
        """File given does not exist. Nothing to parse from.

           This "non-existence" in this test is true with high-probability.

        """
        with self.assertRaises(UtilsFileDoesNotExistError):
            config = read_config(self.config_file_valid_format.name + '1')

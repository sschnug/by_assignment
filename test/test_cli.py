import unittest
import tempfile
from src.exceptions import UtilsFileDoesNotExistError
from src.cli import CLI


class TestCLI(unittest.TestCase):
    """Unit-testing for CLI.

    """
    def setUp(self):
        """Create tempfile used as input.

        """
        self.input_file = tempfile.NamedTemporaryFile()

    def tearDown(self):
        """Close and delete tempfile.

        """
        self.input_file.close()

    def test_valid_minimal(self):
        """Minimal call with valid input-file.

        """
        arg_parser = CLI()
        parsed_args = arg_parser.parse(['-i', self.input_file.name])
        self.assertEqual(parsed_args[0], self.input_file.name)
        self.assertEqual(parsed_args[1], False)

    def test_valid_verbose_on(self):
        """Test valid input-file with verbose=on.

        """
        arg_parser = CLI()
        parsed_args = arg_parser.parse(['-i', self.input_file.name, '-v'])
        self.assertEqual(parsed_args[0], self.input_file.name)
        self.assertEqual(parsed_args[1], True)

    def test_invalid_minimal(self):
        """Minimal call with non-existing input-file.

           This "non-existence" in this test is true with high-probability.

           Will raise UtilsFileDoesNotExistError.

        """
        arg_parser = CLI()
        with self.assertRaises(UtilsFileDoesNotExistError):
            parsed_args = arg_parser.parse(['-i', self.input_file.name + '1'])

    def test_invalid_verbose_on(self):
        """Minimal call with non-existing input-file.

           This "non-existence" in this test is true with high-probability.

           Will raise UtilsFileDoesNotExistError.

        """
        arg_parser = CLI()
        with self.assertRaises(UtilsFileDoesNotExistError):
            parsed_args = arg_parser.parse(['-i', self.input_file.name + '1',
                                            '-v'])

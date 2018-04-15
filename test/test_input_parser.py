import unittest
import tempfile
import secrets
import shutil
from src.exceptions import (InputParserParseError,
                            URLParsingError,
                            URLInferFilenameError,
                            UtilsFileDoesNotExistError)
from src.input_parser import InputParser

FIRST_URL = ("https://storage.googleapis.com/"
             "blueyonder_assignment/python-pseudocode.jpg")
SECOND_URL = ("https://storage.googleapis.com/blueyonder_assignment"
              "/while-loop-animation-python.gif")
FIRST_FILE = 'python-pseudocode.jpg'
SECOND_FILE = 'while-loop-animation-python.gif'
_BROKEN_URL_FILENAME = ("https://storage.googleapis.com/blueyonder_assignment"
                        "/while-loop-animation\0-python.gif")
MALFORMED_URL = 'foo.bar'
VALID_URLS = FIRST_URL + '\n' + SECOND_URL
MALFORMED_URLS = VALID_URLS + '\n' + MALFORMED_URL
MALFORMED_FILENAME = VALID_URLS + '\n' + _BROKEN_URL_FILENAME
MALFORMED_EMPTY = FIRST_URL + '\n' + '\n' + SECOND_URL


class TestInputParser(unittest.TestCase):
    """
    Unit-testing for InputParser.

    """
    def setUp(self):
        """Create temporary-files needed for testing.

        """
        self.valid_out_dir = tempfile.mkdtemp()

        self.valid_f = tempfile.NamedTemporaryFile(mode='w')
        self.valid_f.write(VALID_URLS)
        self.valid_f.seek(0)

        self.malformed_f = tempfile.NamedTemporaryFile(mode='w')
        self.malformed_f.write(MALFORMED_URLS)
        self.malformed_f.seek(0)

        self.malformed_f_filename = tempfile.NamedTemporaryFile(mode='w')
        self.malformed_f_filename.write(MALFORMED_FILENAME)
        self.malformed_f_filename.seek(0)

        self.malformed_f_empty_line = tempfile.NamedTemporaryFile(mode='w')
        self.malformed_f_empty_line.write(MALFORMED_EMPTY)
        self.malformed_f_empty_line.seek(0)

        self.wrong_file_mode = tempfile.NamedTemporaryFile(mode='wb')
        self.wrong_file_mode.write(secrets.token_bytes(100))
        self.wrong_file_mode.seek(0)

    def tearDown(self):
        """Clean-up temporary-files.

        """
        shutil.rmtree(self.valid_out_dir)
        self.valid_f.close()
        self.malformed_f.close()
        self.malformed_f_filename.close()
        self.malformed_f_empty_line.close()
        self.wrong_file_mode.close()

    def test_valid_case(self):
        """All good case.

        """
        parser = InputParser(self.valid_f.name, self.valid_out_dir)
        parser_res = parser.get_url_targetname_pairs()
        self.assertEqual(parser_res[0][0], FIRST_URL)
        self.assertEqual(parser_res[1][0], SECOND_URL)
        self.assertEqual(parser_res[0][1], FIRST_FILE)
        self.assertEqual(parser_res[1][1], SECOND_FILE)

    def test_invalid_input_path(self):
        """Path does not lead to existing file.

        """
        with self.assertRaises(UtilsFileDoesNotExistError):
            parser = InputParser(self.valid_f.name + '_WRONG_PATH',
                                 self.valid_out_dir)

    def test_invalid_input_urls(self):
        """Opening successfull, but parsing URL/filename fails.

        """
        with self.assertRaises(URLParsingError):
            parser = InputParser(self.malformed_f.name, self.valid_out_dir)

    def test_invalid_filenames(self):
        """Opening successfull, parsing successfull, but inferred filename is invalid.

        """
        with self.assertRaises(URLInferFilenameError):
            parser = InputParser(self.malformed_f_filename.name,
                                 self.valid_out_dir)

    def test_malformed_input_file(self):
        """Opening successfull, parsing successfull, but there is an empty-line!

        """
        with self.assertRaisesRegex(InputParserParseError,
                                    ("Input file-format looks wrong. Are there"
                                     " empty lines?")):
            parser = InputParser(self.malformed_f_empty_line.name,
                                 self.valid_out_dir)

    def test_wrong_file_mode(self):
        """Opening fails (with high probability), as binary-file is opened in txt-mode.

        """
        with self.assertRaisesRegex(InputParserParseError,
                                    'Could not open input'):
            parser = InputParser(self.wrong_file_mode.name, self.valid_out_dir)

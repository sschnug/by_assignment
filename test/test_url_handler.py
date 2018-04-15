import unittest
import tempfile
import shutil
from src.exceptions import (URLParsingError,
                            URLInferFilenameError,
                            UtilsFileNameValidError)
from src.url_handler import URLHandler

VALID_URL = ("https://storage.googleapis.com/blueyonder_assignment"
             "/python-pseudocode.jpg")
VALID_URL_INF_FILENAME = 'python-pseudocode.jpg'

MALFORMED_URL = 'foo.bar'
BROKEN_URL_FILENAME = ("https://storage.googleapis.com/blueyonder_assignment"
                       "/while-loop-animation\0-python.gif")


class TestURLHandler(unittest.TestCase):
    """Unit-testing for URLHandler.

    """
    def setUp(self):
        """Create temp-directory as output-dir.

        """
        self.valid_out_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Delete temp-directory.

        """
        shutil.rmtree(self.valid_out_dir)

    def test_valid_url_split(self):
        """Valid URL is given:
           - can be parsed (urlsplit)
           - filename can be inferred
             - filename is valid

        """
        url_handler = URLHandler(VALID_URL, self.valid_out_dir)
        filename = url_handler.get_filename()
        self.assertEqual(filename, VALID_URL_INF_FILENAME)

    def test_invalid_url_split(self):
        """Invalid URL is given:
           - cannot be parsed

        """
        with self.assertRaises(URLParsingError):
            url_handler = URLHandler(MALFORMED_URL, self.valid_out_dir)

    def test_invalid_filename_inference(self):
        """URL given:
           - can be parsed
           - filename-inference leads to invalid filename.

        """
        with self.assertRaises(URLInferFilenameError):
            url_handler = URLHandler(BROKEN_URL_FILENAME, self.valid_out_dir)

import unittest
import tempfile
import os
import shutil
from src.exceptions import (UtilsFileDoesNotExistError,
                            UtilsFileDoesExistError,
                            UtilsFileNameValidError)
from src.utils import assert_file_existing, assert_filename_valid

INVALID_FILENAME = 'myfile\0.jpg'  # null-byte!


class TestUtils(unittest.TestCase):
    """Unit-testing for utils

    """
    def setUp(self):
        """Create temporary-file / temporary-dir needed for testing.

        """
        self.valid_fp = tempfile.NamedTemporaryFile()
        self.valid_out_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean-up temporary-file / temporary-dir.

        """
        self.valid_fp.close()
        shutil.rmtree(self.valid_out_dir)

    def test_is_filepath_valid_with_valid_fp(self):
        """All good case: is_filepath_valid.

        """
        assert_file_existing(self.valid_fp.name)

    def test_is_filepath_valid_with_invalid_fp(self):
        """Path does not lead to existing file.

        """
        with self.assertRaises(UtilsFileDoesNotExistError):
            assert_file_existing(self.valid_fp.name + '1')

    def test_is_filename_valid_all_valid(self):
        """All good case: is_filename_valid.

        """
        assert_filename_valid(os.path.basename(self.valid_fp.name),
                              self.valid_out_dir)

    def test_is_filename_valid_with_invalid_existing_fp(self):
        """Inferred filename already exists at out-dir.

        """
        with self.assertRaises(UtilsFileDoesExistError):
            assert_filename_valid(os.path.basename(self.valid_fp.name),
                                  os.path.dirname(self.valid_fp.name))

    def test_is_filename_valid_with_invalid_inferred_fname(self):
        """Inferred filename can't be used.

        """
        with self.assertRaises(UtilsFileNameValidError):
            assert_filename_valid(INVALID_FILENAME,
                                  os.path.dirname(self.valid_fp.name))

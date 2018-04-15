import unittest
import tempfile
import os
import shutil
from src.exceptions import DownloaderDownloadError
from src.downloader import Downloader

EXISTING_DOWNLOADL_URL = ("https://storage.googleapis.com/"
                          "blueyonder_assignment/python-pseudocode.jpg")
NON_EXISTING_DOWNLOAD_URL = ("https://storage.googleapis.com/"
                             "blueyonder_assignment/NOFILE.nope")


def get_size(filename):
    """Get size of file in bytes.

    """
    st = os.stat(filename)
    return st.st_size


class TestDownloader(unittest.TestCase):
    """Unit-testing for Downloader.

    """
    def setUp(self):
        """Create temp-directory as output-dir.

        """
        self.valid_out_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Delete temp-directory.

        """
        shutil.rmtree(self.valid_out_dir)

    def test_existing_download_valid_outdir(self):
        """Valid Download-link; valid out-dir.

        """
        target_file = os.path.join(self.valid_out_dir, '1.file')

        downloader = Downloader(self.valid_out_dir)
        downloader.download(EXISTING_DOWNLOADL_URL, target_file)
        self.assertEqual(get_size(target_file), 35832)

    def test_nonexisting_download_valid_outdir(self):
        """Invalid Download-link; valid out-dir.

        """
        target_file = os.path.join(self.valid_out_dir, '1.file')

        downloader = Downloader(self.valid_out_dir)
        with self.assertRaises(DownloaderDownloadError):
            downloader.download(NON_EXISTING_DOWNLOAD_URL, target_file)

    def test_existing_download_invalid_outdir(self):
        """Valid Download-link; invalid out-dir.

           Directory invalid / non-existing with high-probability.

        """
        target_file = os.path.join(self.valid_out_dir + '1', '1.file')

        downloader = Downloader(self.valid_out_dir)
        with self.assertRaises(DownloaderDownloadError):
            downloader.download(EXISTING_DOWNLOADL_URL, target_file)

    def test_nonexisting_download_invalid_outdir(self):
        """Invalid Download-link; invalid out-dir.

           Directory invalid / non-existing with high-probability.

        """
        target_file = os.path.join(self.valid_out_dir + '1', '1.file')

        downloader = Downloader(self.valid_out_dir)
        with self.assertRaises(DownloaderDownloadError):
            downloader.download(NON_EXISTING_DOWNLOAD_URL, target_file)

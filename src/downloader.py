"""
This module does the actual downloading & file-saving.
"""

from os.path import join
from urllib.request import urlretrieve
from src.exceptions import DownloaderDownloadError


class Downloader():
    """This class is responsible for actual network-activity / downloading and
       saving.

    This class "retrieves" links and store them on the HDD. This includes
    network-activity and filesystem-activity.

    Expected usage: init once; call download multiple times.

    """
    def __init__(self, out_path, verbose=False):
        """Init with output-path and (optional) verbosity-flag.

           Args:
               out_path (str): valid output-path.
               verbose (bool, optional): be verbose or not (default).

           Attributes:
               out_path (str): original output-path given.
               verbose (bool): be verbose or not.

        """
        self.out_path = out_path
        self.verbose = verbose

    def download(self, url, target_filename):
        """Download single file from URL and save to target-filename.

           Args:
               url (str): valid URL.
               target_filename (str): valid filename

           Raises:
               DownloaderDownloadError: If download/saving fails.

        """
        joined_out_path = join(self.out_path, target_filename)

        if self.verbose:
            print('Download "{}" -> "{}"'.format(url, joined_out_path))

        try:
            local_filename, headers = urlretrieve(url, joined_out_path)

        except Exception as e:
            raise DownloaderDownloadError(
                '\n\nCould not retrieve / download url "{}" -> "{}"'
                .format(url, joined_out_path))

        if self.verbose:
            print('...success')

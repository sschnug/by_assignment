"""
This module provides URL-handling functionality as checking and inferring
filenames.
"""

from urllib.parse import urlsplit
from os.path import basename
from src.exceptions import (URLParsingError,
                            URLInferFilenameError,
                            UtilsFileDoesExistError,
                            UtilsFileNameValidError)
from src.utils import assert_filename_valid


class URLHandler():
    """This class is responsible for parsing, checking and preparing URLs for
       later downloading.

    """
    def __init__(self, url, out_path):
        """Init with a single URL and output-path.

           Args:
               url (str): valid URL to be downloaded.
               out_path (str): valid output-path (existing directory)

           Attributes:
               url (str): original URL given.
               valid_url (str): parsed URL.
               out_path (str): original output-path given.
               inferred_filename (str): target-filename obtained from URL.

           Raises:
               URLParsingError: When URL parsing failed.
               URLInferFilenameError: When no valid filename could be parsed
                                      from URL.

        """
        self.url = url
        self.valid_url = True
        self.out_path = out_path

        self._url_split()
        self._url_get_filename()

    def _url_split(self):
        """Split URL into components (serves as minimal validation).

           This is a critical part of the code and decides which kind of urls
           are allowed!

        """
        try:
            self.urlsplit_res = urlsplit(self.url)
            assert all([self.urlsplit_res.scheme, self.urlsplit_res.netloc,
                        self.urlsplit_res.path])
        except Exception as e:
            self.valid_url = False
            raise URLParsingError(
                'URL "{}" could not be parsed by urlsplit'.format(self.url))

    def _url_get_filename(self):
        """Infer filename from urlsplit result.

           This is a critical part of the code and decides which filenames are
           used to save files!

        """
        try:
            self.inferred_filename = basename(self.urlsplit_res.path).strip()
            assert_filename_valid(self.inferred_filename, self.out_path)
        except UtilsFileDoesExistError:
            raise
        except UtilsFileNameValidError:
            raise URLInferFilenameError(
                'Inferred filename "{}" from URL "{}" is not a valid filename'
                .format(self.inferred_filename, self.url))
        except Exception as e:
            self.valid_url = False
            raise URLInferFilenameError(
                'Could not infer filename from URL "{}"'.format(self.url))

    def get_filename(self):
        """Public getter for results.

           Returns:
               Tuple(str, str): url, target-filename (full-path).

        """
        assert self.valid_url
        return self.inferred_filename

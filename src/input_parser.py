"""
This module provides the parsing of some input-link including basic checks.
"""

from src.exceptions import InputParserParseError
from src.utils import assert_file_existing
from src.url_handler import URLHandler


class InputParser():
    """This class is responsible for parsing URLS (including basic checking)
       & inferrence of target-filenames for later storage.

    """
    def __init__(self, filepath, out_path, verbose=False):
        """Init with input-path (file with links), output-path (directory) and
           (optional) verbosity-flag.

           Args:
               filepath (str): valid path to input-file (with correct format).
               out_path (str): valid path to output-directory.
               verbose (bool, optional): be verbose or not (default).

           Attributes:
               filepath (str): original input-filepath given.
               urls (list(str)): parsed URLs.
               target_filenames (list(str)): inferred filename for each url
                                             in urls.
               out_path (str): original output-path given.
               verbose (bool): be verbose or not.

           Raises:
               InputParserParseError: When opening or parsing input-file fails.

        """
        self.filepath = filepath
        self.urls = []
        self.target_filenames = []
        self.out_path = out_path
        self.verbose = verbose

        self._parse_file()
        self._check_urls()

    def _parse_file(self):
        """Open file and parse line-by-line.

        """
        if self.verbose:
            print('Read input-file...')

        assert_file_existing(self.filepath)

        try:
            with open(self.filepath, 'r') as f:
                for url in f.readlines():
                    self.urls.append(url.strip())
        except Exception as e:
            raise InputParserParseError(
                'Could not open input "{}"'.format(self.filepath))

        # check number of urls read against number of lines
        # this disallows empty lines!
        n_lines = len(self.urls)
        self.urls = list(filter(None, self.urls))
        if n_lines != len(self.urls):
            raise InputParserParseError(
                'Input file-format looks wrong. Are there empty lines?')

        if self.verbose:
            print('...success')

    def _check_urls(self):
        """Check URLs & infer filenames of previously read raw URLs.

        """
        if self.verbose:
            print('Check URLs')

        for url in self.urls:
            urlhandler = URLHandler(url, self.out_path)
            self.target_filenames.append(urlhandler.get_filename())

        if self.verbose:
            print('...success')

    def get_url_targetname_pairs(self):
        """Public getter for results.

           Returns:
               List(Tuple(str, str)): each tuple being a pair of
                                      url / target-filename.

        """
        return list(zip(self.urls, self.target_filenames))

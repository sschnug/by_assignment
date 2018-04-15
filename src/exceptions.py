"""
This module provides custom-exceptions.
"""


class CLIParseError(Exception):
    """Raised when class-method CLI.parse fails

       This means, the commandline used is invalid.
    """


class URLParsingError(Exception):
    """Raised when class-method URLHandler._url_split cannot parse the given URL.

       This means, that the URL is invalid.

    """
    pass


class URLInferFilenameError(Exception):
    """Raised when class-method URLHandler._url_get_filename could not infer a
       valid filename.

       This usually means, that the URL was being parsed correctly, but the
       inferred filename is not a valid one on this OS.

       This error can also appear if OS-access-rights are too strict on
       out-dir.

    """
    pass


class ConfigParserParseError(Exception):
    """Raised when function read_config could not parse "config.ini".

       This means, that the provided ini-file is not a valid ini-file.

    """
    pass


class ConfigParserParseErrorSection(Exception):
    """Raised when function read_config could not find section needed in
       "config.ini".

    """
    pass


class ConfigParserParseErrorKey(Exception):
    """Raised when function read_config could not find key needed in some
       section "config.ini".

    """
    pass


class DownloaderDownloadError(Exception):
    """Raised when class-method Downloader.download failed".

       This can be the case due to:

       - network problems
       - server-side problems / authentification or access-rights
       - missing OS-access-rights for saving the file
       - not enough HDD-diskspace

    """
    pass


class InputParserParseError(Exception):
    """Raised when class-method InputParser._parse_file failed.

       This usually means, that:

       - OS-access-rights are too strict
       - file is binary instead of text
       - there are empty lines (which is forbidden)

    """
    pass


class UtilsFileDoesNotExistError(Exception):
    """Raised when function assert_file_existing failed.

       This means, that:

       - the given path is wrong / leads to non-existing file
       - OS-access-rights are too strict

    """
    pass


class UtilsFileDoesExistError(Exception):
    """Raised when function assert_file_nonexisting failed.

       This means, that:

       - the given path leads to existing file
       - OS-access-rights are too strict

    """
    pass


class UtilsFileNameValidError(Exception):
    """Raised when function is_filename_valid failed.

       This means, that:
       - the given name is not a valid path
       - the filename is not a valid filename (e.g. nullbytes)
       - OS-access-rights are too strict on out-dir

    """
    pass

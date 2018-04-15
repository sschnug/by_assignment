"""
This module provides basic utilities (IO-checks).
"""

import os
from src.exceptions import (UtilsFileDoesNotExistError,
                            UtilsFileDoesExistError,
                            UtilsFileNameValidError)


def is_filepath_valid(fp):
    """Checks if a given path leads to an existing file.

       Args:
           fp (str): path to some file to be checked.

       Returns:
           Bool: True (Yes) / False (No).

    """
    return os.path.isfile(fp)


def assert_file_existing(fp):
    """Checks if filepath leads to existing file and raises exception if not.

       Args: fp (str): filepath

       Returns:
           fp (str): original filepath

       Raises: UtilsFileDoesNotExistError if fp does not lead to existing file.

    """
    if not is_filepath_valid(fp):
        raise UtilsFileDoesNotExistError(
            'File "{}" does not exist, but needs to be.'.format(fp))

    return fp


def assert_file_nonexisting(fp):
    """Checks if filepath does not lead to existing file and raises exception
       if it does.

       Args: fp (str): filepath

       Raises: UtilsFileDoesExistError if fp does lead to existing file.

    """
    if is_filepath_valid(fp):
        raise UtilsFileDoesExistError(
            'File "{}" does exist, but must not.'.format(fp))


def assert_filename_valid(fn, out_dir):
    """Checks if a file with this name can be created in out_dir.
       This needs:
         - permission to create file in out_dir
         - file not already existing in out_dir
         - a valid filename

       This check serves as basic check for valid filenames (OS-dependent).
       As Python currently does not support this functionality out-of-the-box,
       here it's tried to create a file with this name (using the same out_dir
       as for later storage; basically assuming: it's a directory with
       necessary OS-access-rights).

       If this fails (assuming out_dir is a valid target), we interpret the
       filename as invalid.

       Will remove this test-file after. If interrupted, this function might
       pollute out_dir (no removal).

       Args:
           fn (str): filename to check.
           out_dir (str): path to some directory (where we have enough right to
                          create/write files).

       Raises:
           UtilsFileAlreadyExistingError: If file already exists
                                          (invalidates assumptions).
           UtilsFileNameValidError: If filename appears to be invalid.

    """
    full_path = os.path.join(out_dir, fn)

    try:
        assert_file_nonexisting(full_path)
    except UtilsFileDoesExistError:
        raise
    except ValueError:
        # This catches for example null-byte errors
        raise UtilsFileNameValidError(
            'File with name "{}" could not be created in dir "{}"'
            .format(fn, out_dir))

    try:
        # More safe check (than above ValueError catch) for valid filenames
        f = open(full_path, 'w')
        f.close()
        os.remove(full_path)
    except Exception as e:
        raise UtilsFileNameValidError(
            'File with name "{}" could not be created in dir "{}"'
            .format(fn, out_dir))

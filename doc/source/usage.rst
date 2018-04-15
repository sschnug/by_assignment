.. _usage:

=====
Usage
=====

Prerequisites
=============
- ```python3``` is available through commandline (PATH set)
    - assumption: python 3.6
- ```config.ini``` exists in basedir and is a valid ini-file with a valid target-directory
    - e.g. ```TARGET_DIR=/home/sascha/Downloads/test_script/``` (absolute path)
    - e.g. ```TARGET_DIR=example_out``` (relative path)
    - Given ```config.ini``` is ready to be used
- Some URL-input-file is provided and readable
    - Given ```example_data/url_file.txt``` is ready to be used

Run Tests
=========
Run:

.. code-block:: none

    python3 -m unittest test/test*.py

Output:

.. code-block:: none

    ...........................
    ----------------------------------------------------------------------

    Ran 27 tests in 1.232s

    OK

Run Program
===========
Run (from basedir):

.. code-block:: none

    python3 run.py -i PATH_TO_INPUT

or with verbose-mode:

.. code-block:: none

    python3 run.py -i PATH_TO_INPUT -v

Example
-------

Input: ```example_data/links.txt```

.. code-block:: none

    https://storage.googleapis.com/blueyonder_assignment/python-pseudocode.jpg
    https://storage.googleapis.com/blueyonder_assignment/while-loop-animation-python.gif


Configuration: ```config.ini```:

.. code-block:: none

    [output]
    TARGET_DIR=example_out

Run (from basedir):

.. code-block:: none

    python3 run.py -i example_data/links.txt

Output:

    ~

Run:

.. code-block:: none

    python3 run.py -i example_data/links.txt -v

Output:

.. code-block:: none

    Read input-file...
    ...success
    Check URLs
    ...success
    Download "https://storage.googleapis.com/blueyonder_assignment/python-pseudocode.jpg" -> "example_out/python-pseudocode.jpg"
    ...success
    Download "https://storage.googleapis.com/blueyonder_assignment/while-loop-animation-python.gif" -> "example_out/while-loop-animation-python.gif"
    ...success

.. WARNING::
    Calling the script twice, given the same configuration, (if the first run was successfull:) will lead to an exception in the second run, as downloaded files are already present!

Status-codes
============
The script returns a status-code based on potential errors observed. See ApiDoc
for more information.

A stacktrace is outputted to *stderr* in the case of an error.

.. code-block:: none

    0:   no error
    1:   CLIParseError
    2:   UtilsFileDoesNotExistError
    3:   UtilsFileDoesExistError
    4:   UtilsFileNameValidError
    5:   ConfigParserParseError
    6:   ConfigParserParseErrorSection
    7:   ConfigParserParseErrorKey
    8:   InputParserParseError
    9:   URLInferFilenameError
    10:  URLParsingError
    11:  DownloaderDownloadError
    100: any other non-explicitly handled error

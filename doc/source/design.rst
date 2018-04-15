.. _design:

======
Design
======

General principles
==================
No usage of external libraries. Only Python's *standard-library* is used, except for the documentation which is based on sphinx_.

Code follows *pep8* and *docsstrings* are following Google-Style_ (sphinx setup with *napoleon-extension* to handle these).

This project is assumed to run with **Python 3.6**.

If external libraries would be used, the following would be good candidates:

- Requests_
- pytest_

Functionality is splitted into modules. See section ```ApiDoc```.

Standard-library components used
================================
- ```sys```
- ```stacktrace```
- ```argparse```: CLI
- ```configparser```: parsing of config.ini
- ```os```: paths & urls
- ```urllib```: general network-functionality
    - ```urllib.request.urlretrieve``` main download-function
- ```unittest```: only for testing
- ```tempfile```: only for testing
- ```shutil```: only for testing
- ```secrets```: only for testing

Overview of components / repository
===================================
- ```run.py```: CLI to run
- ```src/```: code of modules
- ```test/```: code of tests
- ```doc/```: sphinx-based documentation
- ```config.ini```: example config.ini (used to select output-directory)
- ```example_data/url_file.txt```: example url-link file
- ```example_out```: empty directory; used in example config.ini

Assumptions / Functionality
===========================
The following assumptions are used, partially due to the task being incompletely specified:

Packaging
---------
- No setuptools-like deployment

Server
------
- There is no need to avoid server-side timeouts or geoblocking (used to combat crawlers)
- URLs are ready to be retrieved without redirects or looking for ```content-disposition``` headers

URLs
----
- Filenames can be inferred from URLs
    - using os.path's basename
- Output-directory must not have any existing file equal to the inferred filename
    - At start of script
    - Basically means: Output-directory is clean

CLI/Functionality
-----------------
- The CLI exactly takes one argument (input-file)
    - No output-directory or other things
    - Exception: verbose-mode ```-v``` & help ```-h```
- Output-directory is given in configuration-file
    - Assumed to be existing in base-dir
- Custom-exceptions are mapped to status-codes, as documented in section ```Usage```

Exception-handling
------------------
- Various custom-exceptions raised

Downloads
---------
- No support for resuming downloads (would assume a lot on the server)

Internal flow
=============
- CLI parsing
- Input-file parsing
    - Basic URL checks for all URLs (before attempting to download)
- Downloading one by one

Any failure in any component will lead to early-stopping (no rollback!).

Test design
===========
(Unit-)Tests are heavily based on python's ```tempfile``` module and contain tests which are:

- indeterministic (entropy-pool used)
    - e.g. ```test_input_parser.py``` using module ```secrets```
- indeterministic in terms of side-effects / filesystem-status
    - e.g. creating tempfile which results in pseudo-random filenames
        - assuming there is no file given that name + some simple suffix like ```1```

Indeterministic tests are marked (docstrings) and the failure-probability is negligible, while
the approach allows more simple code.

.. _sphinx: http://www.sphinx-doc.org
.. _Requests: http://docs.python-requests.org
.. _pytest: https://docs.pytest.org
.. _Google-style: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

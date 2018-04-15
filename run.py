""" This file is the basic entry to use the program """

import sys
import traceback
from src.exceptions import *
from src.run_script import run


def out_traceback_and_exit(status_code):
    traceback.print_exc(file=sys.stderr)
    sys.exit(status_code)


def main():
    """Main function: takes arguments and calls src/run_script.run()

       The following status-codes are possible (see exception-docs):

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

    """
    try:
        run(sys.argv)
    except CLIParseError:
        out_traceback_and_exit(1)
    except UtilsFileDoesNotExistError:
        out_traceback_and_exit(2)
    except UtilsFileDoesExistError:
        out_traceback_and_exit(3)
    except UtilsFileNameValidError:
        out_traceback_and_exit(4)
    except ConfigParserParseError:
        out_traceback_and_exit(5)
    except ConfigParserParseErrorSection:
        out_traceback_and_exit(6)
    except ConfigParserParseErrorKey:
        out_traceback_and_exit(7)
    except InputParserParseError:
        out_traceback_and_exit(8)
    except URLInferFilenameError:
        out_traceback_and_exit(9)
    except URLParsingError:
        out_traceback_and_exit(10)
    except DownloaderDownloadError:
        out_traceback_and_exit(11)
    except Exception as e:
        out_traceback_and_exit(100)

    return sys.exit(0)  # All good


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Detect multiple languages and lint appropriately.

Philosophy:
    * Treat warnings as errors
    * Fix if possible
    * process should be automatic - interactive option needs to be specified

Usage:
    python wash.py [-fi] [--output <type>]
    python wash.py -h | --help
Options:
    -h, --help              Show this help
    -i, --interactive       Allow interactive fixing of errors, if supported
    -n, --no-change         Do not fix errors/warnings/change automatically
                            (default is to fix in place)
    -o, --output <type>     Specify output type (tty, json), if supported
    -w, --wrap              Wrap to line length guidelines for $language
"""
import glob
import re

from lint_c import lint_c
from lint_md import lint_md
from lint_py import lint_py
from lint_sh import lint_sh


def get_matching_files(regex, filelist):
    """Get a list of files and return the ones that match the regex."""
    ext_re = re.compile(regex)
    return list(filter(ext_re.search, filelist))


def main():
    """Pass files of a type to the appropriate linter for analysis."""
    # options = docopt.docopt(__doc__)
    options = []
    files = glob.glob("**/*", recursive=True)

    lint_c(get_matching_files(r"\.[ch][px]?[px]?$", files), options)
    lint_md(get_matching_files(r"\.md$", files), options)
    lint_py(get_matching_files(r"\.py.?$", files), options)
    lint_sh(get_matching_files(r"\..{0,2}sh$", files), options)


if __name__ == "__main__":
    main()

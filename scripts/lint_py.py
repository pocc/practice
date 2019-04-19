"""Lint python files with the following libraries:
    * black
    * flake8
    * flake8-bugbear
    * pylint

"""
import subprocess as sp


def lint_py(files):
    sp.call(flake8, pylint, black)


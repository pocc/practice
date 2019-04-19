"""Lint sh files with shellshock."""
import subprocess as sp


def lint_sh(sh_files):
    """Lint sh files with shellshock."""
    sp.call(shellcheck sh_files)


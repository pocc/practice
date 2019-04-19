"""Lint markdown files with prettier."""
import subprocess as sp


def lint_md(files, options):
    """Lint markdown files with prettier."""
    cmds = ["prettier"] + files
    if not options["--no-change"]: 
        cmds += ["--write"]
    if options["--wrap"]:
        cmds += ["--prose-wrap", "always"]
    sp.call(cmds)

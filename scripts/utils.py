"""Utilities shared by other linters."""
import shutil
import subprocess as sp


def comment_spellcheck(filename, options=['--report-only']):
    """Checks comment spelling with scspell (`pip install scspell3k`)."""
    if not shutil.which("scspell"):
        raise Exception("scspell is not installed! Use"
                        "\n\n\tpip install scspell3k\n")
    cmd_list = ["scspell", "--report-only", filename]
    spell_errors = sp.run(cmd_list, stderr=sp.STDOUT, text=True).stdout
    if spell_errors:
        print(spell_errors)


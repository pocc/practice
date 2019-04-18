# Lint with oclint, clang-tidy, and clang-format
# oclint will identify errors while clang-* will fix in place
import glob
import json
import os
import pprint
import re
import subprocess as sp

# Required to avoid compile database errors
COMPILE_OPTS = ["--", "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"]


def call_oclint(c_files):
    cmd_list = ["oclint",
                "-enable-clang-static-analyzer",
                "-enable-global-analysis",
                "-report-type", "json"] + c_files + COMPILE_OPTS
    oclint_output = sp.check_output(cmd_list)
    json_regex = re.compile(r".*?({.*}).*?")
    oclint_json = json.loads(re.search(json_regex, oclint_output)[0])

    return oclint_json["violation"] + oclint_json["clangStaticAnalyzer"]


def call_clang_tidy():
    cmd_list = ["clang_tidy",
    oclint_output = sp.check_output(cmd_list)


def call_clang_format():
    return []

def lint():
    c_files = glob.glob("*.c")

    violations = []
    violations += call_oclint(       c_files )
    violations += call_clang_tidy(   c_files )
    violations += call_clang_format( c_files )
    if violations:
        pprint.pprint(violations)

lint()

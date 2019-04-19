# Lint with oclint, clang-tidy, and clang-format
# oclint will identify errors while clang-* will fix in place
# 
# On Macos, use `brew install oclint llvm` to get these.
import glob
import json
import os
import pprint
import re
import subprocess as sp

# Required to avoid compile database errors
COMPILE_OPTS = ["--", "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"]
C_STYLE = "Google"

def call_clang_format(c_files):
    cmd_list = ["clang-format", "-i", "--style=" + C_STYLE] + c_files
    sp.call(cmd_list)


def call_clang_tidy(c_files):
    # Warnings-as-errors requires checks and to work, both flags need * glob
    cmd_list = ["clang-tidy", "-quiet", "-fix", "-fix-errors", 
            "-checks=*", "-warnings-as-errors=*"] + c_files + COMPILE_OPTS
    
    _pipe = sp.Popen(cmd_list, stdout=sp.PIPE, stderr=sp.STDOUT)
    output = _pipe.communicate()[0].decode('utf-8')
    has_issues = not bool(re.match(r"^\d+ warnings generated\.$", output))
    if has_issues:
        # Running clang-tidy twice to preserve ANSI escape codes for errors
        # -checks=* forces a line about number of warnings for system files,
        # when desired behavior is to print text only on errors 
        # This time, call it and do not process stdout as there are errors.
        sp.call(cmd_list)
        
    # Delete plist filename.plist generated by clang-tidy 
    for filename in c_files:
        plist_file = filename[:-1] + "plist"
        if os.path.exists(plist_file):
            os.remove(plist_file) 


def call_oclint(c_files):
    cmd_list = ["oclint",
                "-enable-clang-static-analyzer",
                "-enable-global-analysis",
                "-report-type", "json"] + c_files + COMPILE_OPTS
    
    _pipe = sp.Popen(cmd_list, stdout=sp.PIPE, stderr=sp.STDOUT)
    oclint_output = _pipe.communicate()[0].decode('utf-8') or '{}'
    violations = json.loads(oclint_output)
    has_issues = violations["clangStaticAnalyzer"] or violations["violation"]
    if has_issues:
        pprint.pprint(violations)


def lint_c(c_files):
    call_clang_format( c_files )
    call_clang_tidy( c_files )
    call_oclint( c_files )


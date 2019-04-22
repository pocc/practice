project('sumdiff', 'c')
src = ['sumdiff.c']
executable('sumdiff', sources : src)

lint_warnings = ['python', '../../scripts/lint_c.py'] + src
run_target('lint', command : lint_warnings, lint_spelling)

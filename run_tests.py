#!/usr/bin/env python

from subprocess import check_call
from sys import executable

cmds = [
    ['flake8', 'crashlog.py', 'test_crashlog.py'],
    [executable, '-m', 'pytest', '-v'],
]

for cmd in cmds:
    print(' '.join(cmd))
    check_call(cmd)

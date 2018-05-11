from InputManager import *


impmod = {
    'hi': 'hello',
    'help': 'helpme',
    'bye': 'goodbye'
}

# Importing algorithms
for pyname in impmod:
    imp_cmd(pyname, r'TestingRes\{}.py'.format(impmod[pyname]))


from ImpCmd import *

# Running imported algorithms
for cmd in impmod:
    run_cmd(cmd, None)

# base code for ImpCmd.py
"""
# imports

def run_cmd(cmd, lib):
    if cmd is None:
        return None
# cmds
    else:
        print(cmd, 'not found')
"""

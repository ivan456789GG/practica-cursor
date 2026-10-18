# pythonrc.py

import readline
import rlcompleter
import os

readline.parse_and_bind('tab: complete')

if 'libedit' in readline.__doc__:
    readline.parse_and_bind('bind ^I rl_complete')
else:
    readline.parse_and_bind('bind ^I rl_complete')

os.environ['PYTHONSTARTUP'] = '.pythonrc.py'
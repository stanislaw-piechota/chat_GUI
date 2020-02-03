import sys
from cx_Freeze import setup, Executable
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
    filename = 'client.py'
    executables = [
        Executable(filename, base=base)
    ]
    setup(name='client.exe',
           version='1.1',
           description='chat program',
           executables=executables
    )

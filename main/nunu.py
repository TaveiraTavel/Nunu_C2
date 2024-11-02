#!/bin/bash
from auxiliary.commands import execute
from os import environ
from auxiliary.interface import * 
import readline

print("""
 _   _
| \\ | |_   _ _ __  _   _
|  \\| | | | | '_ \\| | | |
| |\\  | |_| | | | | |_| |
|_| \\_|\\__,_|_| |_|\\__,_|

v1.0
""")

try:
    while True:
        inp = input(f"Nunu {info(environ.get('MODE', ''))}> ")
        args = inp.split()
        if len(args) >= 1:
            ret = execute(args)
            print(ret)
        
except KeyboardInterrupt:
    print("\nIt's okay, we'll play later.\n")
    

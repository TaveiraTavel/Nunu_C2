from auxiliary.interface import *

class Help:
    general = f"""
{info('General Commands\n-------------------')}
{bold('help')} : displays this menu
{bold('mode')} : alternates between INFECTION and CONTROL
{bold('exit')} : leaves the program
"""

    infection = f"""
{info('Infection Commands\n-------------------')}
{bold('set')} : defines payload variables
{bold('unset')} : undefines payload variables
{bold('options')} : verify payload variables
{bold('make')} : generates a payload to infect the target
{bold('wait')} : wait for a session based on the current parameters
"""

    control = f"""
{info('Control Commands\n-------------------')}
{bold('agents')} : list all availables agents
{bold('use')} : indicates agents to be controlled
{bold('cmd')} : executes the specified command when requested
{bold('kill')} : kills the actual agent
"""

class Options:
    def payload(payload):
        return f"""
{info('Payload Options\n-------------------')}
{bold('LHOST')}: {payload.lhost}
{bold('LPORT')}: {payload.lport}
{bold('RHOST')}: {payload.rhost}
{bold('CHANNEL')}: {payload.channel}
"""


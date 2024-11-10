from channels.icmp import *
from modules.control import *

class Payload:

    def __init__(self, lhost='_________', lport='___', rhost='_________', channel='____'):
        self.lhost = lhost
        self.lport = lport
        self.rhost = rhost
        self.channel = channel

    def setLHOST(self, lhost):
        self.lhost = lhost

    def setLPORT(self, lport):
        if self.channel != 'ICMP':
            self.lport = lport

    def setRHOST(self, rhost):
        self.rhost = rhost

    def setCHANNEL(self, channel):
        self.channel = channel
        if channel == 'HTTP':
            self.lport = 80
        if channel == 'DNS':
            self.lport = 53
        if channel == 'ICMP':
            self.lport = '-'
    
#    def make(self):

    def init(self, lhost, lport, rhost, channel):
        if channel == 'ICMP':
            Icmp().wait(lhost, rhost)
        
        Agent(self).save()


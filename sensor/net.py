# Standard library dependencies.
import multiprocessing as mp

# Third-party dependencies.
from scapy.all import *


class PicklablePacket:
    """A container for scapy packets that can be pickled (in contrast
    to scapy packets themselves)."""
    def __init__(self, pkt):
        self.contents = str(pkt)
        self.time = pkt.time

    def __call__(self):
        """Get the original scapy packet."""
        pkt = Ether(self.contents)
        pkt.time = self.time
        return pkt


class PacketProcessor(mp.Process):
    """ A class the processes packets and finds """

    def __init__(self, pkt_queue):
        mp.Process.__init__(self)
        self.pkt_queue = pkt_queue

    def run(self):
        while True:
            next_pkt = self.pkt_queue.get()
            try:
                print(next_pkt)
            except Exception as e:
                print("Failed!")
                print(e)
        return


class PacketSniffer(mp.Process):
    """ A class that sniffs a specified interface for packets. """

    def __init__(self, pkt_queue, interface='eth0'):
        mp.Process.__init__(self)
        self.interface = interface
        self.pkt_queue = pkt_queue

    def pkt_handler(self, pkt):
        """ Hand the packet off to another process for processing. """
        self.pkt_queue.put(PicklablePacket(pkt))
        print('PacketSniffer pushed --->')

    def run(self):
        sniff(prn=self.pkt_handler, store=0)


class NetworkMonitor(object):

    def __init__(self):
        pkts = mp.Queue()
        self.pp = PacketProcessor(pkts)
        self.ps = PacketSniffer(pkts)

    def start(self):
        self.pp.start()
        self.ps.start()
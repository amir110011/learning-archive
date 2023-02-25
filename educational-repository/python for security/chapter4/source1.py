from scapy.all import *

def packet_callback(packet):
    print packet.show()


#start our sniffer
sniff(prn=packet_callback,count=1)



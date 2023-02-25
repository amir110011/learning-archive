import optparse
from scapy.all import *
def findBing(pkt):
    if pkt.haslayer(Raw):
        payload = pkt.getlayer(Raw).load
        if 'GET' in payload:
            if 'bing' in payload:
                r = re.findall(r'(?i)\?q=(.*?)\&', payload)
                if r:
                    search = r[0].split('&')[0]
                    search = search.replace('q=', '').replace('+', ' ').replace('%20', ' ')
                    print '[+] Searched For: ' + search


conf.iface = "mon0"
try:
    print 'Starting'
    sniff(filter='tcp port 80', prn=findBing)
except KeyboardInterrupt:
    exit(0)


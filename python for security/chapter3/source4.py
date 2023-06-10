import socket
import os
import struct
from ctypes import *
from netaddr import IPNetwork,IPAddress
import threading
import time
host = "192.168.111.1"
subnet = "192.168.111.0/24"
magic_message = "PYTHONRULES!"
# our IP header
class IP(Structure):
    _fields_ = [
    ("ihl", c_ubyte, 4),
    ("version", c_ubyte, 4),
    ("tos", c_ubyte),
    ("len", c_ushort),
    ("id", c_ushort),
    ("offset", c_ushort),
    ("ttl", c_ubyte),
    ("protocol_num", c_ubyte),
    ("sum", c_ushort),
    ("src", c_ulong),
    ("dst", c_ulong)
    ]
    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)
    def __init__(self, socket_buffer=None):
        #map protocol constants to their names
        self.protocol_map = {1:"ICMP", 6:"TCP", 17:"UDP"}
        # human readable IP addresses
        self.src_address = socket.inet_ntoa(struct.pack("<L",self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L",self.dst))
        # human readable protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)


class ICMP(Structure):
    _fields_ = [
    ("type", c_ubyte),
    ("code", c_ubyte),
    ("checksum", c_ushort),
    ("unused", c_ushort),
    ("next_hop_mtu", c_ushort)
    ]
    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)
    def __init__(self, socket_buffer):
        pass


def udp_sender(subnet,magic_message):
    time.sleep(5)
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for ip in IPNetwork(subnet):
        try:
            sender.sendto(magic_message,("%s" % ip,65212))
        except:
            pass


def main():
    t = threading.Thread(target=udp_sender, args=(subnet, magic_message))
    t.start()
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
    socket_protocol = socket.IPPROTO_ICMP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind(( host, 0 ))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    # continually read in packets and parse their information
    while 1:
        raw_buffer = sniffer.recvfrom(65565)[0]
        ip_header = IP(raw_buffer[0:20])
        
        offset = ip_header.ihl * 4
        buf = raw_buffer[offset:offset + sizeof(ICMP)]
        icmp_header = ICMP(buf)



        # check for the type 3 and code and within our target subnet
        if icmp_header.code == 3 and icmp_header.type == 3:
            if IPAddress(ip_header.src_address) in IPNetwork(subnet):
                if raw_buffer[len(raw_buffer) - len(magic_message):] == magic_message:
                    print("Host up: %s" % ip_header.src_address)

if __name__ == '__main__':
    main()

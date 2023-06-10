from socket import getservbyport, socket, AF_INET, SOCK_STREAM


ip = input('enter ip: ')

for i in range(1, 64739):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(1)
    r = sock.connect_ex((ip, i))
    if r == 0:
        print("open: ", i, " ", getservbyport(i))

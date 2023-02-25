import socket

ip = input('enter class ip: ')
for i in range(1, 256):
    try:
        live = socket.gethostbyaddr(ip+str(i))
        print("ip live: ", ip + str(i), " ", live[0])
    except:
        print("ip none: ", ip + str(i))

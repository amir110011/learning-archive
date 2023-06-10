from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util import randpool
import pickle
import socket
import sys
#generate the RSA key
blah = randpool.RandomPool()
RSAKey = RSA.generate(1024, blah.get_bytes)
 
RSAPubKey = RSAKey.publickey()
 
#setup your ip and port 
host = ''
port = 12121
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)
 
print "Server is running on port %d " % port
 
while 1:
  clientsock, clientaddr = s.accept()
  print "a connection from ", clientsock.getpeername()
  #sending the public key to the client
  clientsock.send(pickle.dumps(RSAPubKey))
 
  rcstring = ''
  while 1:
    buf = clientsock.recv(1024)
    rcstring += buf
    if not len(buf):
      break
  clientsock.close()

  encrypted = pickle.loads(rcstring)
  print RSAKey.decrypt(encrypted)

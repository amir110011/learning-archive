from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util import randpool
 
import pickle
import socket
 
host = 'localhost'
port = 12121
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
 
rcstring = s.recv(2048)

publickey = pickle.loads(rcstring)
 
print publickey
 
secretText = publickey.encrypt("Hello, this is the end of this book.",32)

s.sendall(pickle.dumps(secretText))
s.close()



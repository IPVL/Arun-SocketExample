__author__ = 'arun'
# Echo server program
import socket
import sys

HOST = None               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = None
#address_family = [addr[0] for addr in socket.getaddrinfo(bind_addr[0], bind_addr[1], socket.AF_UNSPEC, socket.SOCK_STREAM) if addr[0] in (socket.AF_INET, socket.AF_INET6)][0]
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        print "Server "
        print "af : ", af
        s = socket.socket(socket.AF_INET6, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print 'could not open socket'
    sys.exit(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()
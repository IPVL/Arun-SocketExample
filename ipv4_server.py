__author__ = 'arun'
# Echo server program
import socket
HOST = '0:0:0:0:0:FFFF:C0A8:01F3'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print "\n\n"
print "s.family: ", s.family
print "Hello I am arun from server."
print "s.type: ", s.type
print "s.proto: ", s.proto
print "s.fileno: ", s.fileno
print "\n"
conn, addr = s.accept()
print 'Connected by', addr
print "conn : ", conn
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()














# Echo server program
# import socket
# import sys
# HOST = '0.0.0.0'                 # Symbolic name meaning all available interfaces
# PORT = 50007              # Arbitrary non-privileged port
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(1)
#
# print "\n\n"
# print "s.family: ", s.family
# print "s.type: ", s.type
# print "s.proto: ", s.proto
# print "s.fileno: ", s.fileno
#
# print "\n"
# conn, addr = s.accept()
# print 'Connected by', addr
# print "conn : ", conn
#
# while 1:
#     data = conn.recv(1024)
#     if not data: break
#     conn.sendall(data)
# conn.close()

# HOST = ''                 # Symbolic name meaning all available interfaces
# PORT = 50007              # Arbitrary non-privileged port
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print "s.family: ", s.family
# print "s.type: ", s.type
# print "s.proto: ", s.proto
# print "s.fileno: ", s.fileno
# s.bind((HOST, PORT))
# s.listen(1)
# HOST = None               # Symbolic name meaning all available interfaces
# PORT = 50007              # Arbitrary non-privileged port
# s = None
# for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
#                               socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
#     af, socktype, proto, canonname, sa = res
#     print "af  : ", af
#     print "socktype: ", socktype
#     print "proto : ", proto
#     print "canonname : ", canonname
#
#     try:
#         s = socket.socket(af, socktype, proto)
#     except socket.error as msg:
#         s = None
#         continue
#     try:
#         s.bind(sa)
#         s.listen(1)
#     except socket.error as msg:
#         s.close()
#         s = None
#         continue
#     break
# if s is None:
#     print 'could not open socket'
#     sys.exit(1)
# conn, addr = s.accept()
# print 'Connected by', addr
# while 1:
#     data = conn.recv(1024)
#     if not data: break
#     conn.send(data)
# conn.close()
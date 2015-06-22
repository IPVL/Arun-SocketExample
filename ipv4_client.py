__author__ = 'arun'
# Echo client program
import socket
HOST = '192.168.1.243' #'192.168.1.243'    # The remote host
PORT = 60007              # The same port as used by the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for x in range(0, 130000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "\n\n"
    print "s.family: ", s.family
    print "s.type: ", s.type
    print "Hello I am akkas from client."
    print "s.proto: ", s.proto
    print "s.fileno: ", s.fileno

    s.connect((HOST, PORT))
    s.sendall('Hello, world ')
    data = s.recv(1024)
    print 'Received', repr(data) , x
    s.close()

















# __author__ = 'arun'
# # Echo client program
# import socket
#
# HOST = '0.0.0.0.0.0.0.1'    # The remote host
# PORT = 50007              # The same port as used by the server
# s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# try:
#     s.connect((HOST, PORT))
#     print "Connected."
#     s.sendall('Hello, world')
#     data = s.recv(1024)
#     s.close()
#     print 'Received', repr(data)
# except Exception:
#     print "There is an error. "
#     HOST = "0.0.0.0"
#     PORT = 50007
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((HOST, PORT))
#     print "Connected."
#     s.sendall('Hello, world')
#     data = s.recv(1024)
#     s.close()
#     print 'Received', repr(data)
#




















# Echo client program
# import socket
# import sys
#
# HOST = '0:0:0:0'    # The remote host
# PORT = 50007              # The same port as used by the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
# print "\n\n"
# print "s.family: ", s.family
# print "s.type: ", s.type
# print "s.proto: ", s.proto
# print "s.fileno: ", s.fileno
# s.connect((HOST, PORT))
#
#
#
# s.sendall('Hello, world')
# data = s.recv(1024)
# s.close()
# print 'Received', repr(data)
#
# HOST = "0:0:0:0:0:0:0:1"
# PORT = 50007
# for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
#     af, socktype, proto, canonname, sa = res
#     print "af : ", af
#     print "socket.AF_INET6 : ", socket.AF_INET6
#     print "socktype : ", socktype
#     print "proto : ", proto
#     try:
#         s = socket.socket(af, socktype, proto)
#     except socket.error as msg:
#         s = None
#         continue
#     try:
#         s.connect(sa)
#     except socket.error as msg:
#         print "msg : ", msg
#         s.close()
#         s = None
#         continue
#     break
# if s is None:
#     print 'could not open socket'
#     sys.exit(1)
# s.sendall('Hello, world')
# data = s.recv(1024)
# s.close()
# print 'Received', repr(data)
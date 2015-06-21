#!/usr/bin/env python
import socket

# Connect to an IPv4 address on port 5000
#host = '0.0.0.0'
host = '0.0.0.0'
port = 5012
sockaddr = (host, port)                   

# Create an IPv4 socket and connect
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
conn = sock.connect(sockaddr)
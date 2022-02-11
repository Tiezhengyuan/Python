#!/usr/bin/python


import  sys
import socket

#pass arguments
host, port = None, None
if len(sys.argv) == 2:
    host = sys.argv[1]
    print(host)
elif len(sys.argv) == 3:
    host = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except:
        raise Exception("error: integer for port")
    if port<1 or port>65525:
        print("error: port should be 1-65535")
        sys.exit(2)
    print(host, port)
else:
    print("Usage: python rest_api.py <host> <port> ")
    sys.exit(1)

#connect
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
reply = s.recv(10000)
s.close()
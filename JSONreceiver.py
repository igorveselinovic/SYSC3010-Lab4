# Source: https://pymotw.com/2/socket/udp.html

import socket
import sys
import json

PACKET_SIZE = 100

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

while True:
    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(PACKET_SIZE)
    if not len(buf):
        break
    print(json.loads(buf))


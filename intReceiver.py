# Source: https://pymotw.com/2/socket/udp.html

import socket
import sys
import time

PACKET_SIZE = 100

textport = sys.argv[1]
textn = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
n = int(textn)
server_address = ('localhost', port)
s.bind(server_address)

for i in range(n):

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(PACKET_SIZE)
    if not len(buf):
        break
    print ("Received %s bytes from %s: %s" % (len(buf), address, buf ))


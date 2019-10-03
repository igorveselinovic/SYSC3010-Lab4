# Source: https://pymotw.com/2/socket/udp.html

import socket
import sys
import time
import random

host = sys.argv[1]
textport = sys.argv[2]
textn = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
n = int(textn)
server_address = (host, port)
msg_count = 1

for i in range(n):
    data = str(random.randrange(100))
    s.sendto(data.encode('utf-8'), server_address)


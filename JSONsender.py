# Source: https://pymotw.com/2/socket/udp.html

import socket
import sys
import json

host = sys.argv[1]
textport = sys.argv[2]

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print(x)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

for i in range(10):
    y = json.dumps(x)
    s.sendto(y.encode('utf-8'), server_address)
    x['age'] += 1

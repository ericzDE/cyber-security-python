# -*- coding: utf-8 -*-

import socket

host = 'www.google.com'
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send("GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

res = client.recv(4096)

print(res)
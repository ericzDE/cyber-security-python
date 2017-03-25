# -*- coding: utf-8 -*-

import socket

host = '0.0.0.0'
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send("Hello")

res = client.recv(4096)

print(res)
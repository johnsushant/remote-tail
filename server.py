#!/usr/bin/env python

import socket
from tailf import tailf

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 8080)
print("Starting up on port 8080")
sock.bind(server_address)
sock.listen(1)

while True:
    print("Waiting for connection")
    connection, client_address = sock.accept()
    try:
        # Recieve input file to be tailed from client
        input_file = connection.recv(1024)
        print('Connection from', client_address)
        # Handle Tail Infinitely until connection is closed
        while True:
            for line in tailf(input_file):
                print(line)
                connection.sendall(line)
    except socket.error:
        connection.close()
    finally:
        connection.close()
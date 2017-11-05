#!/usr/bin/env python

import socket
import thread

# Setup server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 8080)
print("Starting up on port 8080")
sock.bind(server_address)
sock.listen(20)
print("Waiting for first connection")

# Handle individual connection
def socketthread(connection):
    while True:
        try:
            # Recieve input file to be tailed from client
            input_file = connection.recv(1024)
            print('Connection from', client_address)
            # Handle Tail infinitely - This is blocking
            with open(input_file) as f:
                # First Loop to reach end of file
                while True:
                    line = f.readline()
                    if not line:
                        break
                # Second Loop to read new lines
                while True:
                    line = f.readline()
                    if line:
                        print(line)
                        connection.sendall(line)
        except socket.error:
            connection.close()
        finally:
            connection.close()

# Code to create thread when new connection is made
while True:
    connection, client_address = sock.accept()
    thread.start_new_thread(socketthread,(connection,))
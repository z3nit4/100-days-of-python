# SOCKETS

# A socket is the endpoint of a communication channel. Communication in a network have two endpoints a server and a client. 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket using IPv4
s.bind(('127.0.0.1', 55555))
s.listen()

while True:
    client, address = s.accept()
    print(f"Connected to {address}.")
    client.send("You are connected!".encode())
    client.close()


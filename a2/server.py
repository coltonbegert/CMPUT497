#!/usr/bin/python           # This is server.py file

# www.tutorialspoint.com/python/python_networking.htm

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 6666                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
counter = 0
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   while True:
    #   c.send(b'test')
        message = c.recv(1024)
        if not message: break
        if len(message) > 0:
            counter += 1
            print(message.decode("ascii"))
        if counter == 25:
            c.send("this is a test")
   # c.send(b'test')
   # print(c.recv(512))
   c.close()                # Close the connection

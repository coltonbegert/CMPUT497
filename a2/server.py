#!/usr/bin/python           # This is server.py file

# www.tutorialspoint.com/python/python_networking.htm

import socket               # Import socket module
import threading
import sys

c = ""
# thread for user messages
def get_input():
    while True:
        message = raw_input()
        # print (message)
        c.send(message)


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 6666                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   counter = 0
   # start thread to listen for user commands
   t = threading.Thread(target = get_input)
   t.daemon = True
   t.start()
   while True:

        # print messages from client
        message = c.recv(1024)
        if not message: break
        if len(message) > 0:
            print(message.decode("ascii"))
        # if counter == 10:
        #     counter = 0
        #     c.send("buzz bitch")

   # c.send(b'test')
   # print(c.recv(512))
   c.close()                # Close the connection

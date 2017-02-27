#!/usr/bin/python           # This is server.py file

# www.tutorialspoint.com/python/python_networking.htm

import socket               # Import socket module
import threading
global c
def get_input():
    while True:
        message = raw_input()
        c.send(str(message))

def print_messages():
    global c
    while True:
     #   c.send(b'test')
         message = c.recv(1024)
         if not message: break
         if len(message) > 0:
             print(message.decode("ascii"))

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 6666                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
counter = 0
while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    t = threading.Thread(target=print_messages)
    t.daemon = True
    t.start()

    t2 = threading.Thread(target=get_input)
    t2.daemon = True
    t2.start()


    # var = raw_input()
    # c.send(b'test')
    # print(c.recv(512))
    c.close()                # Close the connection

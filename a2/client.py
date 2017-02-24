#!/usr/bin/python           # This is client.py file
# https://www.tutorialspoint.com/python/python_networking.htm
import socket               # Import socket module
import time
import datetime
import thread
# from scapy.all import *

def print_socket(interface, mac, rssi):
    print 'test'

global s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 6666                 # Reserve a port for your service.

s.connect((host, port))
# print (s.recv(1024))
# s.send(b'ack')
a_lock = thread.allocate_lock()
with a_lock:
    message = ""
    currentTime = time.time()
    # message += datetime.datetime.strptime(time.time(), "YYYY-MM-DD HH:MM:SS.")
    message += str(datetime.datetime.utcnow())
    message += "\n"
    # message = bytes(str(message),"ascii")
    s.send(message)

# for i in range(1, 20):
#     message = ""
#     currentTime = time.time()
#     # message += datetime.datetime.strptime(time.time(), "YYYY-MM-DD HH:MM:SS.")
#     message += str(datetime.datetime.utcnow())
#     message += "\n"
#     # message = bytes(str(message),"ascii")
#     s.send(message)
# while True:

    # print(s.recv(1024))
s.close()                     # Close the socket when done

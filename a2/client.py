#!/usr/bin/python           # This is client.py file
# https://www.tutorialspoint.com/python/python_networking.htm
import socket               # Import socket module
import time
import datetime
import thread
from scapy.all import *
import wifi_sniffer.py

def print_socket(interface, mac, rssi):
    message = str(datetime.datetime.utcnow()) + " " + str(interface) + " " + str(mac) + " " + str(rssi)
    print message
    global s
    global a_lock
    with a_lock:
        s.send(message)

global s
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 6666                 # Reserve a port for your service.

s.connect((host, port))
# print (s.recv(1024))
# s.send(b'ack')
global a_lock
a_lock = thread.allocate_lock()
# with a_lock:
#     message = ""
#     currentTime = time.time()
#     # message += datetime.datetime.strptime(time.time(), "YYYY-MM-DD HH:MM:SS.")
#     message += str(datetime.datetime.utcnow())
#     message += "\n"
#     # message = bytes(str(message),"ascii")
#     s.send(message)
print_socket("colton1", "12:34:56:78", -76)

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

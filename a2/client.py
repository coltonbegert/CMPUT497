#!/usr/bin/python           # This is client.py file
# https://www.tutorialspoint.com/python/python_networking.htm
import socket               # Import socket module
import time
import datetime
import threading
from scapy.all import *
# import wifi_sniffer

observedclients = []


def print_socket(interface, mac, rssi):
    message = str(datetime.datetime.utcnow()) + " " + str(interface) + " " + str(mac) + " " + str(rssi)
    print message
    global s
    global a_lock
    with a_lock:
        s.send(message)
def sniffmgmt(p):
    print "world"
    # Define our tuple (an immutable list) of the 3 management frame
    # subtypes sent exclusively by clients. I got this list from Wireshark.
    stamgmtstypes = (0, 2, 4)
    # Make sure the packet has the Scapy Dot11 layer present
    if p.haslayer(Dot11):
        # Check to make sure this is a management frame (type=0) and that
        # the subtype is one of our management frame subtypes indicating a
        # a wireless client
        if p.type == 0 and p.subtype in stamgmtstypes:
            extra = p.notdecoded
            rssi = -(256-ord(extra[-4:-3]))
            # print "WiFi signal strength:", rssi, "dBm of", p.addr2, p.info
            # message = str(datetime.datetime.utcnow()) + " " + interface + " " + str(p.addr2) + " " + str(rssi)
            # print message
            # global s
            # global a_lock
            # with a_lock:
            #     s.send(message)
            # print_socket("wlan0", p.addr2, rssi)

            # We only want to print the MAC address of the client if it
            # hasn't already been observed. Check our list and if the
            # client address isn't present, print the address and then add
            # it to our list.
            # if p.addr2.upper() in yannis and 0:
            #     print "YANNIS IS HERE GET DOWN" + p.addr2
            if p.addr2 not in observedclients:
                # print p.addr2
                observedclients.append(p.addr2)

def start_wifi_sniff():
    print "hello"
    interface = "mon0"
    sniff(iface=interface, prn=sniffmgmt)
if __name__ == "__main__":
    global s
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 6666                 # Reserve a port for your service.

    s.connect((host, port))
    # print (s.recv(1024))
    # s.send(b'ack')
    global a_lock
    # a_lock = thread.allocate_lock()
    a_lock = threading.RLock()
    # wifi_interface = "mon0"
    # thread.start_new_thread(sniff, (iface=wifi_interface, prn=sniffmgmt))
    # try:
    #     thread.start_new_thread(start_wifi_sniff, ())
    # except:
    #     print "massive failure"

    t = threading.Thread(target = start_wifi_sniff)
    t.start()
    # with a_lock:
    #     message = ""
    #     currentTime = time.time()
    #     # message += datetime.datetime.strptime(time.time(), "YYYY-MM-DD HH:MM:SS.")
    #     message += str(datetime.datetime.utcnow())
    #     message += "\n"
    #     # message = bytes(str(message),"ascii")
    #     s.send(message)
    # print_socket("colton1", "12:34:56:78", -76)

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

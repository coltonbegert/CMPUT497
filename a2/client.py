#!/usr/bin/python           # This is client.py file
# https://www.tutorialspoint.com/python/python_networking.htm

# Fantastic resource that I pulled most of this code from
# https://pen-testing.sans.org/blog/2011/10/13/special-request-wireless-client-sniffing-with-scapy

# BLE SCANNER sample code
# http://ianharvey.github.io/bluepy-doc/scanner.html

import socket               # Import socket module
import time
import datetime
import threading
from scapy.all import *
from bluepy import btle
# import wifi_sniffer

observedclients = []
hci = 0
mon = 2

client = ""
strength = ""

# handles sending all messages to the server
def print_socket(interface, mac, rssi):
    message = str(datetime.utcnow()) + " " + str(interface) + " " + str(mac) + " " + str(rssi)
    # print message
    global s
    global a_lock
    # with a_lock:
    if client != "" and strength != "":
        if str(mac).lower() == client.lower() and rssi >= strength:
            # s.send(message)
            print "BUZZZZZ"
            s.send("! found buzz command: " + message)

    s.send(message)
# This is the BLE scanning section.
class ScanPrint(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        # self.opts = opts

    # on discovery print the message to the server
    def handleDiscovery(self, dev, isNewDev, isNewData):
        # print "hello"
        print_socket("hci1", dev.addr, dev.rssi)
# this is the function that gets run on a separate thread
def start_ble_sniff():
    scanner = btle.Scanner(hci).withDelegate(ScanPrint())
    devices = scanner.scan(0)

# Handles the wifi packet sniffing
def sniffmgmt(p):
    # print "world"
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
            print_socket("wlan0", p.addr2, rssi)

            # We only want to print the MAC address of the client if it
            # hasn't already been observed. Check our list and if the
            # client address isn't present, print the address and then add
            # it to our list.
            # if p.addr2.upper() in yannis and 0:
            #     print "YANNIS IS HERE GET DOWN" + p.addr2
            if p.addr2 not in observedclients:
                # print p.addr2
                observedclients.append(p.addr2)

# thread that is run to sniff wifi
def start_wifi_sniff():
    print "hello"
    interface = "mon" + str(mon)
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
    # semaphore for socket locking
    a_lock = threading.RLock()


    #start the threads for sniffing
    t = threading.Thread(target = start_wifi_sniff)
    t.daemon = True
    t.start()
    t2 = threading.Thread(target = start_ble_sniff)
    t2.daemon = True
    t2.start()
    while True:
        # time.sleep(1)
        # with a_lock:
        # Recieve messages from the server
        message = s.recv(1024)
        if len(message) > 0:
            print (message)
            command = message.split(' ')
            # if it is a command -> use it
            if len(command) == 3 and command[0] == "buzz":
                s.send("! " + message)
                client = command[1]
                strength = int(command[2])

    s.close()                     # Close the socket when done

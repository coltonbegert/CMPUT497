# Fantastic resource that I pulled most of this code from
# https://pen-testing.sans.org/blog/2011/10/13/special-request-wireless-client-sniffing-with-scapy



# The previous line ensures that this script is run under the context
# of the Python interpreter. Next, import the Scapy functions:
from scapy.all import *
import time
import datetime
# import client
# Define the interface name that we will be sniffing from, you can
# change this if needed.
interface = "mon0"
# Next, declare a Python list to keep track of client MAC addresses
# that we have already seen so we only print the address once per client.
observedclients = []

# yannis = ["68:D9:3C:50:F8:5E", "6C:40:08:8A:20:52", "74:23:44:EB:BC:DF", "D0:7E:35:DB:1E:B0"]

# The sniffmgmt() function is called each time Scapy receives a packet
# (we'll tell Scapy to use this function below with the sniff() function).
# The packet that was sniffed is passed as the function argument, "p".
def sniffmgmt(p):
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
            print_socket(interface, p.addr2, rssi)

            # We only want to print the MAC address of the client if it
            # hasn't already been observed. Check our list and if the
            # client address isn't present, print the address and then add
            # it to our list.
            # if p.addr2.upper() in yannis and 0:
            #     print "YANNIS IS HERE GET DOWN" + p.addr2
            if p.addr2 not in observedclients:
                # print p.addr2
                observedclients.append(p.addr2)
# With the sniffmgmt() function complete, we can invoke the Scapy sniff()
# function, pointing to the monitor mode interface, and telling Scapy to call
# the sniffmgmt() function for each packet received. Easy!
sniff(iface=interface, prn=sniffmgmt)
# while True:
#     print(test)

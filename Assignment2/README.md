lauri.xn--vsandi-pxa.com/2016/09/wifi-sniffer.html

## Required packages
sudo apt-get install aircrack-ng
sudo apt-get install libbluetooth-dev bluez python-pip
sudo apt-get install python-pip libglib2.0-dev
pip install scapy
sudo apt-get install libboost-python-dev
sudo apt-get install libboost-thread-dev
pip install gattlib
pip install git+https://github.com/IanHarvey/bluepy.git

## running
```bash
sudo ifconfig
sudo airmon-ng start wlx....(from infconfig) -> creates an interface on mon0 (or monX)
sudo hciconfig dev -> hciX is our ble interface
sudo python server.py

on new terminal:
sudo python client.py
```

In client.py there are two variables at the top called hci and mon. These need the interface numbers from hciutil and armon-ng.


## About
The server listens on port 6666 for a client to send it messages. It has the ability to listen for command line input the "buzz" the client. commands will be broken up if there are lots of incoming messages but hitting enter will still send the command.

buzz ::::: -db is a command that can be entered in the server and the client will respond by printing buzz when the mac address is found with a rssi >= the db sent by the command. a server comment will also be printed every time the client buzzes.

client.py is what runs to do the sniffing. There are 3 threads. 1 for wifi, 1 for ble and 1 to listen to the server for commands. the program starts up and if the interfaces are correctly installed and specified in the top of the program, it will begin sniffing. The ble captures all active ble communications not devices in discovery mode. it will print buzz when the command is received and the conditions are met. It can sniff ble and wifi simultaneously.

## Resources Used
socket code
https://www.tutorialspoint.com/python/python_networking.htm


Fantastic resource that I pulled most of this code from
https://pen-testing.sans.org/blog/2011/10/13/special-request-wireless-client-sniffing-with-scapy


BLE SCANNER sample code
http://ianharvey.github.io/bluepy-doc/scanner.html

special thanks to bluepy and scapy!

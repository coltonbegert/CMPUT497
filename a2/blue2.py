
# import bluetooth
from bluepy import btle
import time
import datetime

class ScanPrint(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        # self.opts = opts

    def handleDiscovery(self, dev, isNewDev, isNewData):
        # if isNewDev:
        #     status = "new"
        # elif isNewData:
        #     if self.opts.new: return
        #     status = "update"
        # else:
        #     if not self.opts.all: return
        #     status = "old"
        #
        # if dev.rssi < self.opts.sensitivity:
        #     return

        # print ('    Device (%s): %s (%s), %d dBm %s' %
        #           (status,
        #            ANSI_WHITE + dev.addr + ANSI_OFF,
        #            dev.addrType,
        #            dev.rssi,
        #            ('' if dev.connectable else '(not connectable)') )
        #       )
        print " " + str("hci1") + " " + str(dev.addr) + " " + str(dev.rssi)
        # for (sdid, desc, val) in dev.getScanData():
        #     if sdid in [8,9]:
        #         print ('\t' + desc + ': \'' + ANSI_CYAN + val + ANSI_OFF + '\'')
        #     else:
        #         print ('\t' + desc + ': <' + val + '>')
        # if not dev.scanData:
        #     print ('\t(no data)')
        # print
while True:
    scanner = btle.Scanner(1).withDelegate(ScanPrint())
    devices = scanner.scan(0)

# while True:
#     service = DiscoveryService("hci1")
#     devices = service.discover(2)
#
#     print "scan done"
#     # print devices.items()
#     for dev in devices:
#         print dev
#         # address = dev[0]
#         # print address
#         request = GATTRequester(dev)
#         response = GATTResponse()
#         while not response.received():
#             time.sleep(0.1)
#         print response
#         # for i in dev:
#         #     print i
#
# # target_name = "My Phone"
# # target_address = None
# #
# # nearby_devices = bluetooth.discover_devices()
# # ble_devices = bluetooth.discover_devices
# # print nearby_devices
# #
# # for bdaddr in nearby_devices:
# #     print bdaddr
# #     if target_name == bluetooth.lookup_name( bdaddr ):
# #         target_address = bdaddr
# #         break
# #
# # if target_address is not None:
# #     print "found target bluetooth device with address ", target_address
# # else:
# #     print "could not find target bluetooth device nearby"

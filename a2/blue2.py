
# import bluetooth
from gattlib import DiscoveryService, GATTRequester, GATTResponse

while True:
    service = DiscoveryService("hci1")
    devices = service.discover(2)

    print "scan done"
    print devices.items()
    for dev in devices:
        print dev
        # address = dev[0]
        # print address
        request = GATTRequester(dev)
        response = GATTResponse()
        while not response.received():
            time.sleep(0.1)
        print response
        # for i in dev:
        #     print i

# target_name = "My Phone"
# target_address = None
#
# nearby_devices = bluetooth.discover_devices()
# ble_devices = bluetooth.discover_devices
# print nearby_devices
#
# for bdaddr in nearby_devices:
#     print bdaddr
#     if target_name == bluetooth.lookup_name( bdaddr ):
#         target_address = bdaddr
#         break
#
# if target_address is not None:
#     print "found target bluetooth device with address ", target_address
# else:
#     print "could not find target bluetooth device nearby"


# import bluetooth
from gattlib import DiscoveryService

service = DiscoveryService("hci0")
devices = service.discover(2)

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

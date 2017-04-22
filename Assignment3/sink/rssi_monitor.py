import smbus
import sys
import time
import subprocess
import re
bus = smbus.SMBus(1)
address = 0x38
   
def cc2():
	#cap = []
	bus.write_byte(address, 0x70)
	time.sleep(0.1)
        cap = bus.read_i2c_block_data(address,0x00, 4)
	humid = ((((cap[0] & 0x3F) *256) + cap[1]) *100)/16383.0
	temp = (((cap[2] & 0xFF) * 256) + (cap[3] & 0xFC))/4.0/16384.0 * 165.0 - 40.0
	#print(humid, temp)
	#print cap
	return [humid, temp]
def rssi():
	command = 'sudo iwlist wlan0 scan'
	grep_command = 'grep -B 2 "Wifi-RSSI test"'
	valid_rssi = False
	while not valid_rssi:
		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
#	print output
		if "Wifi-RSSI test" in output:
			valid_rssi = True
	rssi_pos = output[0:output.find("Wifi-RSSI test")].rfind("Signal level")
	rssi_val = output[rssi_pos + 13:output.find(" dBm", rssi_pos)]
	return rssi_val
def main():
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		filename = "chipcap.csv"

	with open(filename, 'w') as f:
		i = 0
		while True:
			i += 1
			cap = cc2()
			RSSI = rssi()
			output = []
			output.append(str(time.time()))
			output.append(str(cap[0]))
			output.append(str(cap[1]))
			output.append(RSSI)	
			f.write(",".join(output) + '\n')
			print ",".join(output)
			time.sleep(1)
main()

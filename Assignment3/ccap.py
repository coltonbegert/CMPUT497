import smbus
import sys
import time
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
	return -1
def main():
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		filename = "chipcap.csv"

	with open(filename, 'w') as f:
		i = 0
		while True and i < 10:
			i += 1
			cap = cc2()
			RSSI = rssi()
			output = []
			output.append(str(time.time()))
			output.append(str(cap[0]))
			output.append(str(cap[1]))
			output.append(str(RSSI))	
			f.write(",".join(output) + '\n')
			time.sleep(1)
main()

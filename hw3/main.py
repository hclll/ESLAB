from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
import struct

MSG_LOCK = 0x10

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n=0
recommended_n = -1
for dev in devices:
    print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi))
    for (adtype, desc, value) in dev.getScanData():
        print ("  %s = %s" % (desc, value))
        if "Galaxy Note4" in value:
            recommended_n = n
    n += 1
if recommended_n != -1:
    print ("Recommend number {}".format(recommended_n))
number = input('Enter your device number: ')
print('Device', number)
print(devices[number].addr)
print("Connecting...")
dev = Peripheral(devices[number].addr, 'random')
print("Services...")
for svc in dev.services:
    print(str(svc))
try:
    testService= dev.getServiceByUUID(UUID(0xfff0))
    for ch in testService.getCharacteristics():
        print(str(ch))
        
    
    ch3= dev.getCharacteristics(uuid=UUID(0xfff3))[0]
    if (ch3.supportsRead()):
        print(ch3.read())
    
    ch4= dev.getCharacteristics(uuid=UUID(0xfff4))[0]
    
    msg1 = "Hi! We're b07901xxx"
    msg2 = "034.157.112! XD"
    #msg = struct.pack("hello", MSG_LOCK)
    #dev.writeCharacteristic(0xfff4, bytearray([0x66, 0x67]), wait_for_response=True)
    ch4.write(msg1.encode('ascii'))
    ch4.write(msg2.encode('ascii'))
    print("\"{}\" writed.".format(msg1))
    print("\"{}\" writed.".format(msg2))
    
    
    ch= dev.getCharacteristics(uuid=UUID(0xfff1))[0]
    if (ch.supportsRead()):
        print(ch.read())
        
    
    
        
finally:
    dev.disconnect()

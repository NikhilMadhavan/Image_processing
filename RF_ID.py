import serial
port = serial.Serial('/dev/ttyAMA0',9600,timeout=1)
while(1):
    rcv=port.readline()
    print(rcv)

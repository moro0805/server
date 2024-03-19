import serial

ser = serial.Serial('/dev/ttyACM0.',9600,timeout=None)
line = ser.readline()
print(line) 
ser.close()
import sys
sys.path.append("/Users/諸川博之/AppData/Local/Programs/Python/Python311/Lib/site-packages")
import serial 
import datetime 
import requests 

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10) 
data = {}   
is_first = True 

while True: 
    now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M') 
    lux = ser.readline().decode('utf-8').splitlines() 
    print("テスト出力" + lux)
    data['time'] = now 

    data['lux'] = lux 
    if is_first: 
        is_first = False 
    else: 
        print(data) # 17123の部分はserver.pyのmy_portにする 
        response = requests.post('http://160.16.210.86:21124/lux', data=data) 
        print(response) 

ser.close()
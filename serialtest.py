import serial 

# シリアル通信を行うためのオブジェクトを作成 
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=10) 

# 最初に受信するデータは値がおかしいので無視 
is_first = True 

while True: 

# シリアル通信で受け取ったデータをUTF-8にデコードし,表示する 
    lux = ser.readline().decode('utf-8') 
    if is_first: 
        is_first = False 
    else: 
        print(lux) 

ser.close() 
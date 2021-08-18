import serial
from threading import Thread
import time

def main():
    global s
    s = serial.Serial('COM3', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False,
                    rtscts=False)

    if not s.isOpen():
        print("was closed")
        s.open()

    t1 = Thread(target=readSerial)
    time.sleep(2)
    t1.start()

def readSerial():

    try:
        count = 0
        fs = open("accel1K_usb.txt","w")
        while count<1000:
            res = s.readline()
            res = (res.rstrip()).lstrip()
            res = res.decode("utf-8")
            data = res.split(",")
            if count>=2:
                data = [int(x) for x in data]
                print(data,file=fs)
            # print(data)
            count +=1
            print(data,file=fs)
        fs.close()
    finally:
        s.close()

if __name__ == "__main__":
    main ()
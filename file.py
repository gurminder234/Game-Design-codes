from threading import Thread
import socket, traceback
import matplotlib.pyplot as plt
import numpy as np
data1 = []

def main():

    host = '0.0.0.0'
    port = 5555
    global soc
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.bind((host, port))

    t1 = Thread(target=readSerial)
    t1.start()

def readSerial():
    try:
        count = 0
        fs = open("accel1K.txt", "w")
        while count < 1000:
            print('waiting...')
            message, address = soc.recvfrom(1024)
            # print("received message: %s" % message)
            print(message)
            res = message
            res = (res.rstrip()).lstrip()
            res = res.decode("utf-8")
            data = res.split(",")

            data = [float(x) for x in data[2:5]]
            print(data,file=fs)
            count +=1
        fs.close()
    finally:
        print("exit")
if __name__ == "__main__":
    main()




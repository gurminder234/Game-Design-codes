import random
import numpy as np
import socket
import matplotlib.pyplot as plt


host = "0.0.0.0"  # '#'127.0.0.1'
port = 5555
global soc
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((host, port))
x_data = []
y_data = []
z_data = []
count=0
window_size= 70
skip_size= 40
thresh = 12.0
last_checked=0
start_w = 0
end_w = window_size
is_valid = False

def get_min_max(window):
    min_window = min(window)
    max_window = max(window)
    min_index = window.index(min_window)
    max_index = window.index(max_window)
    diff = max_window - min_window
    return diff,max_index,min_index

while count<1000:
    #print('waiting...')
    message, address = soc.recvfrom(1024)
    # print(message)
    # print("received message: %s" % message)
    res =message
    res = (res.rstrip()).lstrip()
    res = res.decode("utf-8")
    data = res.split(",")

    data = [float(x) for x in data[2:5]]
    #print(data)
    x_data.append(data[0])
    y_data.append(data[1])
    z_data.append(data[2])
    count+=1
    if(count>window_size and (end_w-start_w)>=window_size and len(x_data)>=end_w):
        window_x = x_data[start_w:end_w]
        window_z = z_data[start_w:end_w]
        print("window length:", len(window_x))
        delta_x,max_i_x,min_i_x = get_min_max(window_x)
        delta_z,max_i_z,min_i_z = get_min_max(window_z)

        if delta_x > delta_z:
            dir='x'
            delta = delta_x
            min_index = min_i_x
            max_index = max_i_x
        else:
            dir='z'
            delta = delta_z
            min_index = min_i_z
            max_index = max_i_z

        if delta > thresh :
            if min_index<max_index:
                if dir=='x':
                    print("left", delta)
                else:
                    print("down",delta)
            else:
                if dir=='x':
                    print("right", delta)
                else:
                    print("up",delta)
            is_valid=True
        last_checked=count
        plt.plot([last_checked]*20,list(range(20)),'k-')
        plt.plot([last_checked-window_size]*40,list(range(-20,20)),'y-')

        if is_valid:
            start_w += window_size
            end_w += window_size
        else:
            start_w += skip_size
            end_w += skip_size

plt.plot(x_data,'r')
# plt.plot(y_data,'g')
plt.plot(z_data,'b')
plt.show()
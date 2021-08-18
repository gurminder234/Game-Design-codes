import matplotlib.pyplot as plt
import numpy as np
data = []

f = open('accel1K.txt','r')
for line in f:
    line = line[1:-2]
    line = line.split(',')
    data.append(line)
f.close()

x = []
for i in data:
    x.append(float(i[0]))
y = []
for i in data:
    y.append(float(i[1]))
z = []
for i in data:
    z.append(float(i[2]))
t = np.array(range(len(data)))
plt.plot(t,x,'g',label='x acc')
plt.plot(t,y,'r',label='y acc')
plt.plot(t,z,'b',label='z acc')
plt.legend()
plt.show()

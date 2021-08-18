from threading import Thread
import socket, traceback
import matplotlib.pyplot as plt
import numpy as np

host = '0.0.0.0'
port = 5555
global soc
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((host, port))


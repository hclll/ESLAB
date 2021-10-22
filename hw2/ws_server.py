#!/usr/bin/env python3
import socket
import numpy as np
import json
import time
import random
import ast

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.shape_base import block

mode = 2

# mode: 
## 1: colorbar
## 2: color the newest one


# 3D figure
fig = plt.figure()
ax = fig.gca(projection='3d')


HOST = '192.168.233.211'
PORT = 62023

sample_num = 0
x = []
y = []
z = []
t = []

plt.ion()
plt.show()
plt.draw()
plt.pause(0.01)


# Standard loopback interface address
# Port to listen on (use ports > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print('Received from socket server : ', data)
            if data[0] == '{':
                new_data = ast.literal_eval(data)
                sample_num = new_data["s"]
                x.append(new_data["x"])
                y.append(new_data["y"])
                z.append(new_data["z"])
                t.append(sample_num)
                if mode == 1:
                    img = ax.scatter(x, y, z, c = t, cmap=plt.cool())
                    if sample_num == 1: 
                        cb = plt.colorbar(img)
                    cb.remove()
                    cb = plt.colorbar(img)
                elif mode == 2:
                    if (sample_num > 1):
                        l.remove()
                        ax.scatter(x[sample_num-2], y[sample_num-2], z[sample_num-2], c = "grey")
                    l = ax.scatter(x[sample_num-1], y[sample_num-1], z[sample_num-1], c = "red", label = str(sample_num))
                    ax.legend()

                
                
                plt.draw()
                plt.pause(0.01)
                









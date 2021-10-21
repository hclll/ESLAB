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

# 3D figure
fig = plt.figure()
ax = fig.gca(projection='3d')


HOST = '192.168.233.211'
PORT = 65443

sample_num = 0
x = []
y = []
z = []

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
                print(new_data)
                if (sample_num > 0):
                    ax.scatter(x[sample_num-1], y[sample_num-1], z[sample_num-1], label=str(sample_num-1))
                sample_num = new_data["s"]
                x.append(new_data["x"])
                y.append(new_data["y"])
                z.append(new_data["z"])

                ax.scatter(x[sample_num-1], y[sample_num-1], z[sample_num-1], label=str(sample_num-1))
                # ax.scatter(x2, y2, z2, c=z2, cmap='Blues', marker='o', label='My Points 2')

                # ax.legend()
                plt.draw()
                plt.pause(0.01)
                









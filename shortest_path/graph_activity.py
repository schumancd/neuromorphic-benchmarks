#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('activity.log')

fig, ax = plt.subplots()

ax.scatter(data[:,0], data[:,1], s=10, c='black', marker='.')
ax.set_xlabel('Time')
ax.set_ylabel('Neuron ID')
ax.set_title('Spike Raster for Provided Shortest Path Network')

plt.show()

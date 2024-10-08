"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle

from quiz_2_sta_function import compute_sta


FILENAME = 'data_c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho = data['rho']

print(rho)

# Fill in these values
sampling_period = 2
num_timesteps = 150

spike_triggered_average = compute_sta(stim, rho, num_timesteps)


time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, spike_triggered_average)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()
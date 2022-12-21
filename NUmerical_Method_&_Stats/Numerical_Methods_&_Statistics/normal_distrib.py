# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:48:07 2022

@author: dhpcap
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
#Generate a data x-axis
x = np.arange(-3, 3, 0.001)
# 1) plot normal distribution mu= 0 and sd=1
plt.plot(x, norm.pdf(x, 0, 1))

# 2) multiple normal distributions
plt.plot(x, norm.pdf(x, 0, 1), label='μ: 0, σ: 1')
plt.plot(x, norm.pdf(x, 0, 1.5), label='μ:0, σ: 1.5')
plt.plot(x, norm.pdf(x, 0, 2), label='μ:0, σ: 2')
plt.legend()
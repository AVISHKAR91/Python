# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:25:04 2022

@author: dhpcap
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


sns.distplot(random.binomial(n=15, p=0.5, size=2000), hist=True, kde=False)

plt.show()




from scipy.stats import poisson

poisson.pmf(k=5, mu=3)

poisson.cdf(k=4,mu=7)

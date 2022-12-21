# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:37:20 2022

@author: dhpcap
"""

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

print("Sahil kamble")

import plotly
import plotly.offline as py
import plotly.graph_objects as graph

trace0 = graph.Scatter(
    x=[1,2,3,5],
    y=[10,15,11,11],
    name='data1'
  )

trace1=graph.Scatter(
    x=[1,2,3,4],
    y=[16,5,11,9],
    name="data2"
    )

data=[trace0,trace1]

py.offline.plot(data, filename='basic-line', auto_open=True)
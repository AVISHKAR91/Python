# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:27:21 2022

@author: dhpcap
"""

import plotly
from plotly.graph_objects import Scatter, Layout

plotly.offline.plot({
    "data":[Scatter(x=[10,20,30,40], y=[4,3,2,1])],
    "layout":Layout(title="This is First plotly Example")
    })


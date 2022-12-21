# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:21:14 2022

@author: dhpcap
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    return 'Hello, World!, have a nice day'

app.run(debug=True)
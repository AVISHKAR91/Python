# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:17:15 2022

@author: dhpcap
"""

s= "avishkargaikwad"
print(id(s))

s="pankajgharde"
print(id(s))

s=10
h=10
print(id(s), id(h))
h=30
print(s is h)
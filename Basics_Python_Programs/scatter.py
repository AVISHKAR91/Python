# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 08:58:39 2022

@author: dhpcap
"""

import matplotlib.pyplot as plt

enrollment=[10,20,30,40,50,80,23,40,18,22]

students = [0,10,20,30,40,50,70,77,80,100]

#x=[10,40]
#y=[40,22]

plt.scatter(enrollment,students,label="This is scatter chart",color="green",marker="*",s=250)#s=marker size
plt.plot(enrollment,students,color="red",label="students data")
plt.grid()
plt.xlabel("Enrollment")
plt.ylabel("Students")
plt.legend()
plt.title("This my first in matplotlib graph\n This is on the next line")
plt.show()
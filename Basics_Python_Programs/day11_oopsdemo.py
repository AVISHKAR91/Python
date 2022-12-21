# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 18:22:43 2022

@author: dhpcap
"""

class Person:
    def __init__(self, pid=0, name="", mobile=""):
        self.__pid=pid
        self.__name=name
        self.__mobile=mobile
    def __str__(self):
        return f"Id: {self.__pid} Name :{self.__name} Mobile :{self.__mobile}"
    
    def set_pid(self, pid):
        self.__pid=pid
    def set_name(self, name):
        self.__name=name
    def set_mobile(self, mob):
        self.__mobile=mob
        
    def get_pid(self):
        return self.__pid
    def get_name(self):
        return self.__name
    def get_mobile(self):
        return self.__mobile
    
p=Person(100, "Ranjahn", "1111111")
print(p)
print(p.get_name())
nmob=input("Enter new mobile number:")
p.set_mobile(nmob)
print(p)

B=Person(300, "Avishkar", "9999999")
print(B)

id=int(input("Enter id:"))
name=input("Enter Name:")
contact=input("Enter Contact Number:")
B.set_pid(id)
B.set_name(name)
B.set_mobile(contact)
print(B)
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:52:45 2022

@author: dhpcap
"""

class Person:
    def __init__(self, id, name, mobile, dept):
        self.__id=id
        self.__name=name
        self.__mobile=mobile
        self.__dept=dept
        
    def __str__(self):
        return f"Id : {self.__id}\n Name: {self.__name}\n Mobile : {self.__mobile}\n Department : {self.__dept}\n"
    
    def set_pid(self, id):
        self.__id=id
    def set_name(self, name):
        self.__name=name
    def set_mobile(self, mobile):
        self.__mobile=mobile
        
    def get_pid(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_mobile(self):
        return self.__mobile
    

class SalariedEmp(Person):
    def __init__(self, id="", name="", mobile="",  dept="", desg="",sal=""):
        super().__init__(id, name, mobile, dept)
        self.__desg=desg
        self.__sal=sal
        
    def __str__(self):
        return super().__str__()+f"designation: {self.__desg}\n Salary:{self.__sal}"
    def set_desg(self,desg):
        self.__desg=desg
    def set_sal(self, sal):
        self.__sal=sal
    def get_desg(self):
        return self.__desg
    def get_sal(self):
        return self.__sal
    def calc_Sal(self):
         return self.__sal+0.10*self.__sal+0.15*self.__sal-0.08*self.__sal               
     
class ContractEmp(Person):
    def __init__(self, id="", name="", mobile="",  dept="",hr_chrges="", no_hrs="" ):
        super().__init__(id, name, mobile, dept)
        self.__hr_chrges=hr_chrges
        self.__no_hrs=no_hrs
        
    def __str__(self):
        return super().__str__()+f" Hrs: {self.__hr_chrges}\n Charges : {self.__no_hrs} "
    def set_hr_chrges(self,hr_chrges):
        self.__hr_chrges=hr_chrges
    def set_no_hrs(self, no_hrs):
        self.__no_hrs=no_hrs
    def get_hr_chrges(self):
        return self.__hr_chrges
    def get_no_hrs(self):
        return self.__no_hrs
    def calc_Sal(self):
         return self.__hr_chrges*self.__no_hrs
     
s=SalariedEmp(11,"Avishkar","80576867","Research","Project Manager",90000)
print(s)       

c=s=ContractEmp(11,"Avishkar","80576867","Research","8hrs","900/day")
print(c)
       

       
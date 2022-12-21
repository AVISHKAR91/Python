# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:07:03 2022

@author: dhpcap
"""

class person:
    def __init__(self, id,name,mob):
        self.__id=id
        self.__name=name
        self.__mob=mob
    def __str__(self):
        return f"Id : {self.__id}\n Name: {self.__name}\n Mobile:{self.__mob}\n"
    def set_id(self,id):
        self.__id=id
    def set_name(self,name):
        self.__name=name
    def set_mob(self,mob):
        self.__mob=mob
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_mob(self):
        return self.__mob
    
class SalariedEmp(person):
    def __init__(self, id, name, mob, desg, sal):
        super().__init__(id, name, mob)
        self.__desg=desg
        self.__sal=sal
        
    def __str__(self):
        return super().__str__()+f"Desgnation:{self.__desg}\n Salary:{self.__sal}\n"
    def set_desg(self,desg):
        self.__desg=desg
    def set_sal(self, sal):
        self.__sal=sal
    def get_desg(self):
        return self.__desg
    def get_sal(self):
        return self.__sal
    
    def calSal(self):
        print("in salaried emp calcsal")
        return self.__sal+0.10*self.__sal+0.15*self.__sal-0.08*self.__sal 
    
class ContractEmp(person):
    def __init__(self, id, name, mob, hrs, charges):
        super().__init__(id, name, mob)
        self.__hrs=hrs
        self.__charges=charges
        
    def __str__(self):
        return super().__str__()+f"No of hours:{self.__hrs}\n Charges:{self.__charges}"
 
    def set_hrs(self, hrs):
        self.__hrs=hrs
    def set_charges(self, charges):
        self.__charges=charges
    def get_hrs(self):
        return self.__hrs
    def get_charges(self):
        return self.__charges
    def calSal(self):
        print("in contract emp calcsal")
        return self.__charges*self.__hrs
    
if __name__=="__main__":
    s=SalariedEmp(1, "Gomati", 7858955, "Clurk", 80000)
    print(s)
    c=ContractEmp(2, "Avishkar", 70386569895, 8, 500)
    print(c)
    
    p=person(100, "Rajan", 7890)
    print(p)
    print(p.get_name())
    nmob=input("Enter mob no:")
    p.set_mob(nmob)
    print(p)
    
    p1=person(101,"Rashmi","222222")
    print(p1.get_name())
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
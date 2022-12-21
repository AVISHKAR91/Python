# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:35:18 2022

@author: dhpcap
"""

from demo__oops import *


def addnewEmployee(ch):
    id=int(input("Enter id:"))
    name=input("Enter name:")
    mob=input("Enter Mob:")
    
    if ch==1:
        desg=input("Enter Designation:")
        sal=int(input("Enter salary:"))
        s=SalariedEmp(id, name, mob, desg, sal)

    else:
        hrs=int(input("Enter No of Hours:"))
        charges=int(input("Enter charges:"))
        s=ContractEmp(id, name, mob, hrs, charges)
    lst.append(s)

def displayincome(id):
    for emp in lst:
        if emp.get_id()==id:
            return emp.calSal()
    return None
        
def displayall():
    for emp in lst:
        print(emp)
        
def displaySalariedEmp():
    for emp in lst:
        if isinstance(emp, SalariedEmp):
            print(emp)
            
def displayContractEmp():
    for emp in lst:
        if isinstance(emp, ContractEmp):
            print(emp)

lst=[SalariedEmp(11,"Revati","33333","designer",2345667),ContractEmp(12,'rajan','4444',10,2000)]
        
    
choice=0
while choice!=7:
    choice = int(input('''
                       1.Add New Employee
                       2.Display income of Employee by id
                       3.display all
                       4.display only salaried Employee
                       5.Display only Contract Employee
                       6.delete Employee
                       7.display by Name
                       8.Exit
                       Enter Your choice:
                       '''))
    if choice==1:
        ch=int(input(f"1. Salried\n 2. Contract"))
        addnewEmployee(ch)
    elif choice ==2:
        id=int(input("Enter Id:"))
        amt=displayincome(id)
        if amt!=None:
            print("income:", amt)
    elif choice == 3:
        displayall()
    elif choice ==4:
        displaySalariedEmp()
    elif choice == 5:
        displayContractEmp()
    elif choice == 6:
        id =int(input("Enter id for delete Employee:"))
        status=deleteEmp(id)
        if status ==1:
            print("FOund and Deleted")
        elif status ==2:
            print("Found but Not Deleted")
        else:
            print("Not Deleted")
        
    elif choice ==7:
        print("Thank You for visiting")
    else:
        print("Wrong Choice")
            
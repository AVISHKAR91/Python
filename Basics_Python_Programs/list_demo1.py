# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:04:31 2022

@author: dhpcap
"""

#design a system to manage list of course names in CDAC
def addnewcourse():
    cname=input("enter new course")
    lst.append(cname)
    return True

def displayall():
    for num,cname in enumerate(lst,1):  #[(1,'DAC')]
        print(f"{num} ---> {cname}")

def deletecourse(cname):
    if cname in lst:
        ans=input(f"do you want to delete {cname}(y/n)?")
        if ans=="y":
            lst.remove(cname)
            return 1
        else:
            return 2
    else:
        return 3
    
def modifyname(ocname,ncname):
    if ocname in lst:
        ans=input(f"do you really want to modify {ocname} {ncname}(y/n)?")
        if ans=="y":
            pos=lst.index(ocname)
            lst[pos]=ncname
            return 1
        else:
            return 2
    else:
        return 3
    
    
def displayperticular(cname)
    if cname in lst:
        pos=lst.index(cname)
        print(lst[pos])




lst=['DAC','DHPCAP']
choice=0

while choice!=7:
    
    choice=int(input("""1.add new course\n 2.delete the course\n 3.display all courses\n 4.modify course name\n 5.display a prticular course name\n 6.sort the courses\n 7.exit"""))
    
    if choice==1:
        status=addnewcourse()
        if status:  #status==True
            print("data added successfully")
    elif choice==2:
        cname=input("enetr course to delete")
        status=deletecourse(cname)
        if status==1:
            print("deleted successfully")
        elif status==2:
            print("found but not deleted")
        else:
            print("not found")
    elif choice==3:
        displayall()
    elif choice==4:
        ocname=input("enetr old cname")
        ncname=input("enetr new name")
        status=modifyname(ocname,ncname)
        if status==1:
            print("modified successfully")
        elif status==2:
            print("found but not modified")
        else:
            print("not found")
            
    elif choice==5:
        displayperticular(cname)
        
    elif choice==6:
        sort()
            
    elif choice==7:
        print("Thank you for visiting......")
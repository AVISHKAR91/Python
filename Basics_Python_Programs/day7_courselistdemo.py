# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:20:19 2022

@author: dhpcap
"""

#design a system to manage list of course names in CDAC
def addnewcourse():
    cname=input("enter new course:")
    lst.append(cname)
    return True

def displayall():
    for num,cname in enumerate(lst,1):  #[(1,'DAC')]
        print(f"{num} ---> {cname}\n")

def deletecourse(cname):
    if cname in lst:
        ans=input(f"do you want to delete {cname}(y/n)?:")
        if ans=="y":
            lst.remove(cname)
            return 1
        else:
            return 2
    else:
        return 3
    
def modifyname(ocname,ncname):
    if ocname in lst:
        ans=input(f"do you really want to modify {ocname} {ncname}(y/n)?:")
        if ans=="y":
            pos=lst.index(ocname)
            lst[pos]=ncname
            return 1
        else:
            return 2
    else:
        return 3

lst=['DAC','DHPCAP']
choice=0
while choice!=7:
    print("""1. add new course\n2. delete the course\n3. display all courses\n4. modify course name\n5. display a prticular course name\n6. sort the courses\n7. exit""")
    choice=int(input("\n Enter Choice:"))
    if choice==1:
        status=addnewcourse()
        if status:  #status==True
            print("data added successfully")
    elif choice==2:
        cname=input("enetr course to delete:")
        status=deletecourse(cname)
        if status==1:
            print("deleted successfully")
        elif status==2:
            print("found but not deleted")
        else:
            print("not found")
    elif choice==3:
        displayall()
        print()
    elif choice==4:
        ocname=input("enetr old cname:")
        ncname=input("enetr new name:")
        status=modifyname(ocname,ncname)
        if status==1:
            print("modified successfully")
        elif status==2:
            print("found but not modified")
        else:
            print("not found")
            
    else:
        print("Thank you for visiting......")
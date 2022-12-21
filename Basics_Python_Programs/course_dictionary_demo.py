# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:47:34 2022

@author: anilk
"""

def addnewcourse():
    cname=input("enetr new course")
    num=int(input("number of participants"))
    #v=d.setdefault(cname,num)
    if cname in d.keys():
        return False
    else:
        d[cname]=num
        return True
    
def  deletecourse(cname):
     if cname in d.keys():
         ans=input(f"do you want to delete the course {cname}(y/n)?")
         if ans=='y':
             d.pop(cname)
             return 1
         else:
             return 2
     else:
        return 3

def modifycourse(oname,nname):
    if oname in d.keys() and nname not in d.keys():
        d[nname]=d[oname]
        d.pop(oname)
        return True
    else:
        return False

def displayall():
    for k,v in d.items():
        print(f"{k}---->{v}")
        
def displayallgreatern(n):
    for k,v in d.items():
        if v>n:
            print(f"{k}---->{v}")
            

d={'DAC':240,'DAI':40}
choice=0
while choice!=8:
    choice=int(input("""
                     1. add new course
                     2. delete existing course
                     3. modify name of existing course
                     4. display all courses
                     5. display all courses with participants > n
                     6. find all courses with x number of participants
                     7. check whether the course exists
                     8. exit
                     """))
    if choice==1:
        status=addnewcourse()
        if status:
            print("course added")
        else:
            print("course already exists")
    elif choice==2:
        cname=input("enetr course name to delete")
        status=deletecourse(cname)
        if status==1:
            print("deleted successfully")
        elif status==2:
            print("exists but not deleted")
        else:
            print("not exists")
    elif choice==3:
        oname=input("enetr old name")
        nname=input("enetr NEW name")
        status=modifycourse(oname,nname)
        if status:
            print("modified successfully")
        else:
            print("wrong values")
    elif choice==4:
        displayall()
    elif choice==5:
        n=int(input("enter value of n"))
        displayallgreatern(n)
    elif choice==6:
        print(d)
    elif choice==7:
        cname=input("enter course name:")
        if cname in d.keys():
            print("Exist")
        else:
            print("Not Exist")
        
    elif choice==8:
        print("Thanks for visiting......")
          
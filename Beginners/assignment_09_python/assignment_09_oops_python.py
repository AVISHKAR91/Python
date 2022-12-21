# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:59:11 2022

@author: dhpcap
"""

class students:
    def __init__(self, id, name="", m1="",m2="",m3="" ):
        self.__id=id
        self.__name=name
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3
    def __str__(self):
        return f"Id:{self.__id}\n Name:{self.__name}\n M1:{self.__m1}\n M2:{self.__m2}\n M3:{self.__m3}\n"
    def set_id(self,id):
        self.__id=id
    def set_name(self,name):
        self.__name=name
    def set_m1(self,m1):
        self.__m1=m1
    def set_m2(self,m2):
        self.__m2=m2
    def set_m3(self,m3):
        self.__m3=m3
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_m1(self):
        return self.__m1
    def get_m2(self):
        return self.__m2
    def get_m3(self):
        return self.__m3
    
class PhdStudent(students):
    def __init__(self, id, name="", m1="",m2="",m3="",thesis_sub="",grade=0 ):
        super().__init__(id, name, m1,m2,m3)
        self.__thesis_sub=thesis_sub
        self.__grade=grade
        
    def __str__(self):
        return super().__str__()+f"Thesis Subject :{self.__thesis_sub}\n Grade:{self.__grade}"
    def get_name(self):
        return self.__name
    def set_thesis(self,thesis_sub):
        self.__thesis_sub=thesis_sub
    def set_grade(self,grade):
        self.__grade=grade
    def get_thesis(self):
        return self.__thesis_sub
    def get_grade(self):
        return self.__grade
    def calc_percentage(self):
        percent=(self.__m1+self.__m2+self.__m3+self.__m4+self.__grade*10)/5
        return percent
    
class MscStudent(students):
    def __init__(self, id, name="", m1=0,m2=0,m3=0,special_sub="",m4=0 ):
        super().__init__(id, name="", m1="",m2="",m3="")
        self.__special_sub=special_sub
        self.__m4=m4
        
    def __str__(self):
        return f"Special Subject :{self.__special_sub}\n M4:{self.__m4}"
    def get_name(self):
        return self.__name
    def set_specialSub(self,special_sub):
        self.__special_sub=special_sub
    def set_m4(self,m4):
        self.__m4=m4
    def get_specialSub(self):
        return self.__special_sub
    def get_m4(self):
        return self.__m4
    def calc_percentage(self):
        percent=(self.__m1+self.__m2+self.__m3+self.__m4)/4
        return percent
    
#p=PhdStudent(11,"Avishkar",40,50,60,"reserach_physics",8)
#print(p)

std = []


def addStudent():
    c = input("""
                p for Phd Student
                m for Msc Student
                
            Enter Course : 
              """)
    if c=='p':
        #name="", pid=0, m1=0, m2=0, m3=0, ths="", gd=0
        std.append(PhdStudent(int(input("id: ")), input("Name : "), int(input("M1 : ")), int(input("M2 : ")),
                              int(input("M3 : ")), input("Thesis : "), int(input("Grade : "))))
        print("Student data added successfully......")
    elif c=='m':
        #name="", pid=0, m1=0, m2=0, m3=0, spsub="", m4=0
        std.append(MscStudent(int(input("id : ")), input("Name : "), int(input("M1 : ")), int(input("M2 : ")),
                              int(input("M3 : ")), input("Special Subject : "), int(input("M4 : "))))
        print("Student data added successfully......")
    else:
        print("wring course try next time....")

def subjectMod():
    name = input("Enter name of Student : ")
    for s in std:
        if s.get_name()==name:
            s.set_specialSub(input("Enter new subject : "))
    else:
        print(f"Studen {name} not found")

def percentage():
    name = input("Enter name of student : ")
    for s in std:
        if s.get_name()==name:
            print(s.calc_percentage())
            break
    else:
        print(f"Student {name} not found")

def display():
    for s in std:
        print(s)    
        
ch = 0
while ch!=5:
    ch = int(input("""
              1. Add new student
              2. Modify special subject of msc student
              3. Calculate percentage of a student
              4. Display all
              5. Exit
              
        Enter Choice : 
          """))
    if ch==1:
        addStudent()
    elif ch==2:
        subjectMod()
    elif ch==3:
        percentage()
    elif ch==4:
        display()
    else :
        print("Logout successfully......")
    
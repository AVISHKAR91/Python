# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 19:07:46 2022

@author: anilk
"""

def addnewemployee():
    empid=int(input("Enter id:"))
    ename=input("Enter name:")
    sal=float(input("Enter salary:"))
    cursor.execute("insert into employee values(?,?,?)",(empid,ename,sal))
    con.commit();
    
    
def deleteemployee(empid):
    cursor.execute("delete from employee where empid=?",(empid))
    con.commit();

def updateemployee(empid, ename,sal):
    cursor.execute("update employee set ename=?, sal=? where empid=?;",(empid, ename, sal))
    con.commit();
    
    
def displayall():
    cursor.execute("select * from employee");
    for row in cursor.fetchall():
        print(row[0],row[1],row[2])
       
        
def displaybyid(empid):
    cursor.execute("select * from employee where empid=?", (empid,));
    row=cursor.fetchone()
    print(row[0],row[1],row[2])
    
import sqlite3
con=sqlite3.connect("mydb.db")
cursor=con.cursor();
#displayall()

choice =0
while choice!=6:
    choice=int(input("""
                     1.add
                     2.delete
                     3.update
                     4.display all
                     5.display by id
                     6.exit
                     """
                     "Enter your choice:"))
    if choice==1:
        addnewemployee()
    elif choice==2:
        empid=int(input("Enter id:"))
        deleteemployee(empid)
    elif choice==3:
        empid=int(input("Enter id:"))
        ename=input("Enter name:")
        sal=float(input("Enter salary:"))
        updateemployee(empid, ename, sal)
    elif choice==4:
        displayall()
    elif choice==5:
        empid=int(input("Enter id:"))
        displaybyid(empid)
    elif choice == 6:
        cursor.close()
        con.close()
        print("Thank you for visiting...")
    else:
        print("wrong choice")
        


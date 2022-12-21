# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:36:48 2022

@author: dhpcap
"""

import sqlite3
con=sqlite3.connect("mytable.db")
cursor=con.cursor()


    
def addstudent():
    id=int(input("Enter id:"))
    name=input("Enter name:")
    std=int(input("Enter standard:"))
    cursor.execute("insert into Student values(?,?,?)",(id,name,std))
    con.commit();
    
def deletestudent(id):
    cursor.execute("delete from Student where id=?",(id,))
    con.commit();
def updatestudent(id, name,std):
    cursor.execute("update Student set name=?, std=? where id=?;",(id, name, std,))
    con.commit();
def displaybyid(id):
    cursor.execute("select * from Student where id=?", (id,));
    row=cursor.fetchone()
    print(row[0],row[1],row[2])
def displayall():
    cursor.execute("select * from Student")
    for row in cursor.fetchall():
        print(row[0],row[1],row[2])
        
choice=0
while choice!=6:
    choice=int(input('''
                     1.add
                     2.delete
                     3.update
                     4.displayall
                     5.display by id
                     6.exit
                     Enter choice:
                     '''))
    if choice==1:
        addstudent()
    elif choice==2:
        id=int(input("Enter id:"))
        deletestudent(id)
    elif choice==3:
        id=int(input("Enter id:"))
        name=input("Enter name:")
        std=int(input("Enter Standard:"))
        updatestudent(id, name, std)
    elif choice==4:
        displayall()        
    elif choice==5:
       id=int(input("Enter id:"))
       displaybyid(id)
    elif choice ==6:
        cursor.close()
        con.close()
        print("Thank for visiting")
    else:
        print("Wrong choice")
                
               
    
        
                     
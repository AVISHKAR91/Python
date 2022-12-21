# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:31:31 2022

@author: dhpcap
"""
'''
1.write a regex to get only the part of the email before the "@" sign excluding the "@" sign.
example myemail@google.com o/p myemail
'''

import re
mail = "mye12mail@google.com"
a=re.search("m(.*?)l", mail,re.I)
print(a)
if a!=None:
    print("Found")
    print(a.group())
    print(a.span())
else:
    print("Not Found")
    
'''
2.only the lines that start with a number or any 2 aplphbates
'''
b=re.search("2(.*)", mail, re.I)
print(b)
if b!=None:
    print("Found")
    print(b.group())
    print(b.span())
else:
    print("Not Found")

'''
3.Write a python program to accept mobile number and validate it. it should  contain exactly 10 digits
''' 
import re # Importing re module
n=input('Enter Mobile number :')  # Reading input from the user
r=re.fullmatch('[0-9][0-9]{9}',n) # calling fullmatch function by passing pattern and n
if r!=None: # checking whether it is none or not 
     print('Valid Number')
else:
     print('Not a valid number')
     
'''
4.Write a python program to accept user name and password  and validate it. username should contain only alphabets
 or digits and password length should be 8, starts with alphabet and should contain atleast one special character($,@) .
accept username and password from user and validate it. if it is valid then display message welcome to our application. 
otherwise ask to reenter.
(allows maximum 3 attempts to accept password

 '''
'''
username = input("Enter Username:")
password = input("Enter Password:")

if username == re.match("^[A-Za-z0-9_-]*$"):
    print("Match")
else:
    print("Not Match")

     
     

def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif not password.isdigit():
            print("Make sure your password has a number in it")
        elif not password.isupper(): 
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password seems fine")
            break

validate()
'''

def checkUsername(username):
    if username.isalnum():
        return True
    else:
        return False
    
def checkPasswd(password):
    if len(password)==8:
        if password[0].isalpha():
            if "$" in password:
                return True
            elif "#" in password:
                return True
            else:
                return False
        else:
            print("Password not start with alphabet")
            return False
    else:
        print("Password length should be 8")
        return False
    



username = input("Enter Username:")
password = input("Enter Password:")
if checkUsername(username):
    print("Username is ok or valid password")
else:
    print("Username wrong")
    
if checkPasswd(password):
    print("Password is ok or valid")
else:
    print("Password Wrong or Not Valid")




























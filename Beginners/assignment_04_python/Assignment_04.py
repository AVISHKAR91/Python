# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:10:33 2022

@author: dhpcap

"""

'''
1. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.

3. Modify the above question to allow student to sit if he/she has medical cause. Ask
user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

'''
total_num = int (input("Enter No. of classes are held:"))
attend_num = int (input("Enter No. of classes are attended:"))
medical_cause = input("have any mediacl cause(y/n)")

per = attend_num/total_num*100

print("Percentage of class attended is:", per,"%")

if(per >75 and medical_cause == 'n'):
    print("You are allowed to sit in exam")
else:
    print("You are  not allow to sit in exam")
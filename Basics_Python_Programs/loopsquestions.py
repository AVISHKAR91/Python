# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 00:07:32 2022

@author: dhpcap
"""

#Print the first 10 natural numbers
i = 1
while i<=10:
    print(i)
    i=i+1    
    
    
#print the pattern

rows = 5

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j,end='')
    print('')  

#PRINT THE STAR PATTERN

rows = 5

for i in range(0, rows+1):
    for j in range(i+1,0):
        print("*" ,end='')
    print('')    
    
    
    
    
# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)    
    


# programme in multiplication 

n =2

for i in range(1,11,1):
    product = n*i
    print(product)    


# print the number tuple

numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)


#Count the total number of digits in a number

num = 2232312

count = 0

while num!=0:
    
    num = num // 10
    
    
    count = count + 1
print("total digits are:", count)    



# ptrint the pattern

n = 5
k = 5

for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()  
    
# reverse the number

list1 = [10, 20, 30, 40, 50]
    
new_list = reversed(list1)

print(list(new_list))

# Display numbers from -10 to -1 using for loop

for num in range(-10 ,0, 1):
    print(num)


    
#-------------------------------------------------------

for i in range(6):
    print(i)
else:
    print("Done!")    

#---------------------------------------------------#

    
    
    
    
    
    
        
    
    
    

























          
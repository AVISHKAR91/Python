'''
5. Print the output of following statements
If
x = 2
y = 5
z = 0
then find values of the following expressions:
a. x == 2
b. x != 5

c. x != 5 && y >= 5
d. z != 0 || x == 2
e. !(y < 10)

'''

x=2
y=5
z=0

print(x==2)
print(x!=5)
print(x!=5 and y>=5)
print(z!=0 or x==2)
print (not(y<10))


'''
6. Accept number from user and check whether it is divisible by 5 and 11
if divisible then display appropriate message.

'''

num = int (input("Enter a number:"))
if (num%5==0 and num%11==0):
    print(f"{num} is divisible by both 5 and 11")
else:
    print(f"{num} is not divisible  by both 5 and 11")
    




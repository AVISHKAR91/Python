
"""

def factorial(n=5):
    '''this function returns factorial of a number'''
    f=1
    for i in range(1,n+1):  #1,2,3,4,5,6
        f=f*i
    return f


x=int(input("enetr x"))
term=int(input("enetr terms"))
s=1;
print(f"{s}",end=" ")
for i in range(1,term): #1,2,3,4
  
     a=x**i
     f=factorial(i)
     print(f"+{x}^{i}/{i}!",end="")
     s=s+(a/f)
print(f"= {s}")

"""

n=int(input("Enter the range of number:"))
sum=0
p=9
for i in range(1,n+1):
    sum += p
    p=(p*10)+9
print("The sum of the series = ",sum)

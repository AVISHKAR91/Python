lst = [10, 12, 13]
for index,num in enumerate(lst):
    print(f"{index}-------->{num}")
    
lst = [10,20,30]
names=["pune","Mumbai","kolhapur","hyderabad"]

for num,nm in zip(lst,names): 
    print(f"{num}-------->{nm}")


for num in sorted(lst):
    print(num) 
print(lst)    

for num in reversed(lst):
    print(num)
print(lst)    




lst = [10,12,11,15,33,53,32,22,21,43]
lst1 = []

for num in lst:
    lst1.append(num*num)
    
lst1 = [num*num for num in lst ] 

lst1=list(map(lambda x:x*x,lst))#map function uses the reduced the syntax
print(lst1)
      

lst1=[]
for num in lst:
    if num>10:
        lst1.append(num)
        

#list comprehnsive operator
lst1=[num for num in lst if num>10 and num%3==0]
print(lst1)
    
#functional programming
lst2=list(filter(lambda x:x>10 and x%3==0,lst))
print(lst2)
#both are working are same



words=["hello","welcome","aaaa","try","test","te"]
#find a list of words with length 4
lst3 = list(filter(lambda x:len(x)>=4,words))
print(lst3)

lst4=list(filter(lambda x:x.startwith("we"),words))


from functools import  reduce
ans=reduce(lambda x,y:x+y,lst)
print("addition:",ans)


lst=["python","perl","java","c++"]
s=reduce(lambda x,y:x+y[0:2],lst,"")
print(s)















    



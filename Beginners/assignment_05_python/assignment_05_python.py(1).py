# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:26:50 2022

@author: dhpcap
"""


# 1. Given a string of odd length greater than 7, return a new string made of the middle three
# characters of a given String
# Given:
# str1 = "RakeshzipPetabb"
# Output
# zip
# str2 = "JazzbonAyxx"
# Output
# bon

str1 = "RakeshzipPetabb"
l=len(str1)
mid = l//2
print(str1[(mid-1):(mid+2)])
str2 = "JazzbonAyxx"
l=len(str2)
mid = l//2
print(str2[(mid-1):(mid+2)])


# 2. Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
# Given:
# s1 = "Ault"
# s2 = "Kelly"
# Expected Output:
# AuKellylt

def append_middle(s1, s2):
    print("Original Strings are", s1, s2)
    mi = int(len(s1) / 2)
    x = s1[:mi:]
    x = x + s2
    x = x + s1[mi:]
    print("After appending new string in middle:", x)

append_middle("Ault", "Kelly")


# 3. two strings, s1, and s2 return a new string made of the first, middle, and last characters each
# input string
# Given:
# s1 = "America"
# s2 = "Japan"
# Expected Output:
# AJrpan
# solution:
def mix_string(s1, s2):
    first_char = s1[0] + s2[0]
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char
    print("Mix String is ", res)

s1 = "America"
s2 = "Japan"
mix_string(s1, s2)

# 4. Given an input string with the combination of the lower and upper case arrange characters
# in such a way that all lowercase letters should come first.
# solution:
    
str1 = "PytHONStudy"
lower = []
upper = []
for char in str1:
 if char.islower():
  lower.append(char)
 else:
  upper.append(char)
sorted_string = ''.join(lower + upper)
print("arranging characters giving precedence to lowercase letters:")
print(sorted_string)


# 5. create a third-string made of the first char of s1 then the last char of s2, Next, the second
# char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the
# result.

# Given:
# s1 = "Abc"
# s2 = "Xyz"
# Expected Output:
# AzbycX

s1 = "Abc"
s2 = "Xyz"


# 6. Find all occurrences of “USA” from right to left in a given string ignoring the case. also
# Given:
# str1 = "Welcome to USA. usa awesome, isn't it?

str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"
temp_str = str1.lower()
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)
str1 = "Welcome to USA. usa awesome, isn't it?"
print(str1.rfind("USA"))
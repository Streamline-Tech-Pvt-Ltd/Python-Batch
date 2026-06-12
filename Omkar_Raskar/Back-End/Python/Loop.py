#06/01/2026

#Loop :
#1. A loop in python is a way to executes a set of statements repeatly.
#2. Loop is used to repeat a block of code until this given condition is true.

"""3. Loops are used to execute a block of code repeatedly until a specific condition is met.
4. Loops in Python are used to repeat actions efficiently."""

#Two Main Types Of Loop :
#1. for loop
#2. while loop
##
#3. do-while loop


#1. for loop : 
#A. The for loop is used to iterate over a sequence (list, tuple, string, set, dictionary, range).
#B. or, Other iterable objects executing a block of code once for each item in the sequence. 

"""It allow to execute a block of code repeatedly, 
once for each item in the sequence."""

#C. Syntax :
"""
for i in range()
statements
"""

"""
Key Points

1.Executes code for each element in a sequence
2.Works with range() for numeric iteration
3.Loop variable takes value one by one
4.Ends automatically when sequence ends
"""
#D. Example :
"""for i in range(1,6):
    print(i)
"""

"""n = 4
for i in range(n):
    print(i)"""
    
"""fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print(fruit, end=" ")"""
    
#F. Class Example :
"""for i in range(10):
    print(i)"""
    
"""for i in range(11):
    print(i)"""
 
 #Starting point 1 And Stop   
"""for i in range(1,11):
    print(i)"""
    
"""for i in range(11,31):
    print(i)"""
    
#Print Horizantal in (end = " ")
"""for i in range(1,101):
    print(i, end = " ")"""
    
#Print odd number using a for loop
"""for i in range(1,11,2):
    print(i)"""
    
#Print even number using a for loop
"""for i in range(2,11,2):
    print(i)"""
    
#Print any Table 2 using for loop
"""for i in range(1,11):
    print(i*2)"""

"""Logic Define :s
 i*2
 1*2 = 2
 2*2 = 4
 3*2 = 6
 4*2 = 8
 5*2 = 10
 6*2 = 12
 7*2 = 14
 8*2 = 16
 9*2 = 18
 10*2 = 20
 """   

#Print Table 8   
"""for i in range(1,11):
    print(i*8) """  
    
#Input Fuction
"""num = input("Enter Number :")
print(type(num))"""

"""n = int(input("Enter Number :"))
for i in range(n):
    print(i)"""


"""n = int(input("Enter Number :"))
for i in range(1,11):
    print(i*n)"""
 
 
 
#Home Work :
    
#Print name in 5 times using user input
"""name = input("Enter Your Name :")
for i in range(5):
    print(name)"""

#Print a odd number
"""n = int(input("Enter Your Odd Number : "))
for i in range(1,101,2):
    print(i)"""

#Print a even number
"""n = int(input("Enter Your Even Number : "))
for i in range(2,101,2):
    print(i)"""
    

#07/01/2026

#Factorial Number : Multiplication of up to this Number,
#5! =1*2*3*4*5

"""fact = 1
for i in range(5):
    fact = fact * (i + 1)
print(fact)"""

"""Factorial Logic :
fact = fact * (i + 1)
     = 1 * (0 + 1) = 1
     = 1 * (1 + 1) = 2
     = 2 * (2 + 1) = 6
     = 6 * (3 + 1) = 24
     = 24 * (4 + 1) = 120"""
     
"""n = int(input("Enter Number :"))
fact = 1
for i in range(n):
    fact = fact * (i + 1)
    print(fact)"""
    
#Natural Number : 1,2,3,4,5,....
#Whole Number : 0,1,2,3,4,5,....
#Integer Number : ....-3,-2,-1,0,1,2,3,....

#Sum of natural number using for loop
"""n = 7
sum = 0
for i in range(1,8):
    sum = sum + i
    print(sum)"""
    
"""Natural Number Logic :
    sum = sum + i
        = 0 + 1 = 1
        = 1 + 2 = 3
        = 3 + 3 = 6
        = 6 + 4 = 10
        = 10 + 5 = 15
        = 15 + 6 = 21 
        = 21 + 7 = 28"""
 
#Sum of natural number using for loop (user input)       
"""n = int(input("Enter Number :"))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
    print(sum)"""
    
#2. While Loop :
#A. The while loop in python execute a block of code 
# repeatedly as long as a specified condition remains true.
#B. The while loop executes code as long as a condition is True.
#C. With the while loop we can execute a set of statements as long as a condition is true.
#D. Syntax :

"""i = Starting Point
while condition:
    statements"""
# i = 2 - Itrator
#looping process - Iteration

#E. Example :
"""i = 1
while i <= 5:
    print("Hello") 
    i += 1"""
    
"""i = 0 
while i <= 10:
    print(i)
    i = i + 1"""

"""i = 0 
while i < 11:
    print(i)
    i = i + 1"""
    
#Any Table using user input 
"""n = int(input("Enter Number :"))
i = 1
while i <= 10:
    print(i * n)
    i += 1"""
    
    
# Home Work :
#1. Print Even and Odd number using while loop.
"""n = int(input("Enter Odd Number :"))
i = 1
while i < 11:
    print(i)
    i += 2
    
n = int(input("Enter Even Number :"))
i = 0
while i < 11:
    print(i)
    i += 2"""
    
#2. Print Sum of Natural Numbers using while loop.
"""n = int(input("Enter Number :"))
sum = 0
i = 1
while i < 8:
    print(sum)
    sum = sum + i
    i += 1"""
    
#3. Print Factorial Number using while loop.
"""n = int(input("Enter Number :"))
fact = 1
i = 1
while i <= 5:
    fact = fact * i
    i += 1
    print(fact)"""
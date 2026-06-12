# 01/01/2026

#Tuple :
#1. A tuple is an ordered, immutable collection of elements in Python.
#(Immutability : Tuples cannot be modified after creation (no add, remove, or change)).

#2. Tuple are used to store multiple items in a single variable.
#3. Syntax:
#  Tuples are written using parentheses ().
# Example :

tuple = (1,2,3,4,5)
print(tuple)

"""Advantages of Tuple
Faster than lists
Memory efficient
Data safety due to immutability

Disadvantages of Tuple
Cannot modify elements
Less flexible compared to lists

Use Cases
Fixed data
Function return values
Dictionary keys
Read-only data storage"""

tup = (1,2,3,4,5,"India","True")
print(type(tup))

tup = (1,2,3,4,5,"India","True")
print(tup[:])


tup = (1,2,3,4,5,"India","True")
print(tup[::-1])


tuple = (1,2,3,4,5,"India","True")
print(tuple[3:6])

#Method Of Tuple :

#1. count():
#A. Returns the number of times a specified value occurs in a tuple.
#B. Does not change the tuple.

tup =(1,2,3,4,5,6,3,5,3,2,2,4)
tup = tup.count(2)
print(tup)

#2. index(): 
#A. Searches the tuple for a specified value and returns the position of where it was found.
#B. Raises error if element is not found.

tup = (1,2,4,5,6,34,"India","True")
tup = tup.index("India")
print(tup)

#3. concatenation():
#A. Used to join two or more tuples into one tuple.
#B. Creates a new tuple (original tuples are unchanged).
#C. Uses the + operator.

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)

#4. Repitation():
#A. Used to repeat a tuple multiple times
#B. Creates a new tuple with repeated elements
#C. Uses the * operator with an integer

t1 = (1,2,3)
t = t1 * 3
print(t)

tup = (20,32,31,45,36,22,11,"True",[3,4,6,"Apple"],10)
print(type(tup))

print(tup[-2])

print(tup[-2][2])

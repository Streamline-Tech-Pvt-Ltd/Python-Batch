# 02/01/2026

#Set :
#1. A set is an unordered, mutable collection of unique elements in Python.
#2. Sets are used to store multiple items in a single variable.
#3. A set is a collection of non-repitative elements(Duplicates are not allowed).
#4. Syntax :
# Sets are written using curly braces {} or the set() function.
# Example :

s = {1, 2, 3}
print(s)
print(type(s))

"""Advantages
Fast membership testing
Automatically removes duplicates
Useful for mathematical operations

Disadvantages
Unordered
Cannot access elements by index

Use Cases
Removing duplicates
Membership testing
Mathematical set operations
Data comparison"""

s={4,5,8,9,4,"kiki","India"}
print(type(s))

a = {}
print(type(a))

b = set()
print(type(b))

s1 = {2,3,4,2,5,6,7}
print(s1)

#Method Of Set :
s2 = {"India","australia","canada"}
print(type(s2))


#1. add() : 
#A. Adds one element to the set.
s2 = {"India","australia","canada"}
s2.add("USA")
print(s2)


#2.clear() :
#A. Removes all the elements from the set.
set1 = {1,3,2,4,5,7}
set1.clear()
print(set1)


#3. copy() :
#A. Returns a copy of the set.
n = {1,2,3}
n1 = n.copy()
print(n1)

set = {"Omkar","Pratik","Rohit","Avi"}
set1 = set.copy()
print(set1)


#4. difference() : 
#A. Returns a set containing the difference between two or more sets.
#B. Returns elements present in first set but not in second.
x = {"apple","banana","orange"}
y = {"google","Microsoft","apple"}
print(x.difference(y))
print(y.difference(x))

a1 = {1,2,5,8}
b1 = {4,7,9,2}
print(a1.difference(b1))
print(b1.difference(a1))


#5. intersection() :
#A. Returns a set, that is the intersection of two other sets.
#B. Returns a set with common elements.
x = {"apple","banana","orange"}
y = {"google","Microsoft","apple"}
print(x.intersection(y))
print(y.intersection(x))

a = {1,2,3}
b = {5,6,7}
print(a.intersection(b)) #These two set are not common values/element, returns empty set.


#6. union() :
#A. Returns a set containig the union of sets.
#B. Returns a new set with elements from both sets.
#C. Combine two sets.
x = {"apple","banana","orange"}
y = {"google","Microsoft","apple"}
print(x.union(y))
print(y.union(x))

a = {1,2,3}
b = {5,6,7}
print(a.union(b))
print(b.union(a))

#7. isdisjoint() :
#A. Returns whether two sets have a intersection or not.
#B. Checks if sets have no common elements.
#C. Answer must be (True/False).
# True = Diffferent elements.
# False = Same elements.

#They are differnt values.
s1 = {6,8,9,7}
s2 = {1,2,3,4}
print(s1.isdisjoint(s2))

#They are common element.
x = {"apple","banana","orange"}
y = {"google","Microsoft","apple"}
print(x.isdisjoint(y))

##################################

#Frozenset : 
#1. A frozenset is an immutable version of a set in Python.
#2. Once created, its elements cannot be changed.
#3. It is similar to set, but once a frozenset is created, its elements cannot modified.
#4. Syntax :
# frozenset is created using the frozenset() function.
#5. Example :
fs = frozenset([1, 2, 3])
print(fs)

#Duplicate elements are automatically removed.
my_frozen = frozenset([1,2,2,3,4])
print(my_frozen)

#You cannot add, remove, or update elements.
a = ["apple","mango"]
b = frozenset(a)
b[a] = "orange"
print(b)    #They will be error show



""""Advantages
Data safety due to immutability
Can be used as dictionary keys
Suitable for fixed collections

Disadvantages
Cannot modify elements
Less flexible than set

Use Cases
Fixed data collections
Dictionary keys
Preventing accidental modification
Mathematical operations with constant sets"""

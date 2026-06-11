# 01/01/2026

#Dictionary :
#1. A dictionary is an ordered, mutable collection of data stored in key–value pairs.
#(Mutable : You can change, add, or remove elements after the dictionary is created).

#2. Dictionaries are used to store data values in key:value pairs.
#3. Duplicates are not allowed.
#4. Syntax :
# Dictionaries are written using curly braces {}.
# Example :

dict = { "Name" : "Omkar","Age" : 23}
print(dict)

"""Advantages
Fast data retrieval
Flexible and efficient
Easy to represent real-world data

Disadvantages
More memory usage
Keys must be unique

Use Cases
Student records
Employee details
JSON data handling
Configuration settings"""

d ={"key" : "value", "key1" : "value1"}
print(type(d))

dict = {1 : "Apple", 2 : "Orange", 3 : "Banana"}
print(type(dict))

a = {}
print(type(a))

#Method Of Dictionary :

"""Key Characteristics

Dictionary is Mutable: You can alter its contents.
Add new key: value pairs.
Update values for existing keys.
Delete key: value pairs.

Dictionary Keys are Immutable: Keys must be hashable, so they can't be changed while they're keys.
Allowed Keys: Strings, numbers, tuples (immutable sequences).
Not Allowed Keys: Lists, sets (mutable types)."""


#1. keys() : (keys hi immutable aahe)
#A. Returns all the keys of the dictionary.

dict1 = {1 : "Apple", 2 : "Orange", 3 : "Banana"}
print(dict1.keys())

#2. values() : (values hi mutable aahe)
#A. Returns all values of the dictionary.
#B. Values can be duplicated.

dict1 = {1 : "Apple", 2 : "Orange", 3 : "Banana"}
print(dict1.values())

#3. items() : 
#A. Returns a list containing a tuple for each key value pairs.
#B. Returns key–value pairs as tuples.

dict1 = {1 : "Apple", 2 : "Orange", 3 : "Banana"}
print(dict1.items())

#4. copy() : 
#A. Returns a shallow copy of the dictionary.

dict = {1 : "Python", 2 : "Java", 3 : "c", 4 : "C++"}
print(dict.copy())

#5. clear() :
#A. Removes all elements from the dictionary.

dict = {1 : "Python", 2 : "Java", 3 : "c", 4 : "C++"}
print(dict.clear())

#6. update() :
#A. Adds or updates elements
#B. Can merge two dictionaries
#C. Modifies original dictionary

dict = {1 : "Python", 2 : "Java", 3 : "c", 4 : "C++"}
dict.update({4 : "DSA"})
print(dict)

dict = {1 : "Python", 2 : "Java", 3 : "c", 4 : "C++"}
dict.update({4 : "DSA", 2 : "HTML"})
print(dict)

#7. pop() :
#A. Removes the element with the specified key

dict = {1 : "Python", 2 : "Java", 3 : "c", 4 : "C++"}
dict.pop(2)
print(dict)

dict = {1 : "Python", 2 : "Java", 3 : "c", 4 : "C++"}
dict.pop(4)
print(dict)

#8. popitem() :
#A. Removes and returns the last inserted key–value pair.

dict = {1 : "Python", 2 : "Java", 3 : "c", 4 : "C++"}
dict.popitem()
print(dict)

dict = {1 : "Python", 1 : "Java", 3 : "c", 4 : "C++"}
print(dict)
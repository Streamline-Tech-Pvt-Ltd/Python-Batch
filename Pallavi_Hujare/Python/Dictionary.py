# Dictionary - Dictionary is a collection of key-value pairs in a single variable.
#dictionary is denoted by {}
#dictionary is mutable but the keys are immutable
#dictionary is ordered
#duplicate keys are not allowed in a dictionary

d1 = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(type(d1))

#dictionary methods

#1. keys() - keys method is used to return a list of all the keys in a dictionary.

dict = {1:"c", 2:"c++", 3:"java", 4:"python"}
print(dict.keys())

#2. values() -Values methods id used to return a list of all the values in a dictionary

dict = {1:"c", 2:"c++", 3:"java", 4:"python"}
print(dict.values())

#3. items() - items() method is used to return a list of all the key-value pairs in a dictionary.
dict = {1:"c", 2:"c++", 3:"java", 4:"python"}
print(dict.items())

#4. update() - update method is used to update the value of a specified key in a dictionary.
dict = {1:"c", 2:"c++", 3:"java", 4:"python"}
dict.update({1:"JS"})
print(dict)

#5. clear() - clear() method is used to remove all the key-value pairs from a dictionary.
dict = {1:"c", 2:"c++", 3:"java", 4:"python"}
dict.clear()
print(dict)

#6. copy() - copy() method is used to create a copy of a dictionary.
dict = {1:"c", 2:"c++", 3:"java", 4:"python"}
dict1 = dict.copy()
print(dict1)
print(dict)

#7. popitem() -  used to remove and return the last inserted key-value pair from a dictionary as a tuple (key, value).
dict = {1:"c", 2:"c++", 3:"java", 4:"python"}
dict.popitem()
print(dict)

#8. pop() - method for dictionaries is used to remove a key-value pair by its key and return the value. If the key is not found, you can provide a default value to avoid a KeyError.

dict = {1:"c", 2:"c++", 3:"java", 4:"python"}
dict.pop(1)
print(dict)

d1 = {1:"c++", 2:"c++", 3:"java", 4:"python"}
print(d1)
# 31/12/2025

#List :
#1. A list is an ordered, mutable collection of elements in Python.
"""Mutable :
Lists can be changed after creation (add, remove, modify elements)."""

#2. List is container to store a set of values of any data types.
#3. Duplicates are allowed. 
#4. Syntax :
#  Lists are written using square brackets [].
# Example :

l = [1,2,3,4,5,6]
print(l)

"""Advantages
Dynamic size
Easy to modify
Supports various operations

Disadvantages
Slower than tuples
More memory usage

Use Cases
Storing multiple values
Data processing
Stack and queue implementation
Iteration and looping"""


#Example 1. 
l = [1,2,3,4,"India",5,6,8.8,"x+7j"]
print(l[:])

#Example 2. 
l = [1,2,3,4,"India",5,6,8.8,"x+7j"]
print(type(l))

#Example 3. 
l = [1,2,3,4,"India",5,6,8.8,"x+7j"]
print(l[0])
print(l[-3])
#print(l[-4][-2])
#print(l[-4][2])
#print(len(l)) #Length hi 1 index ni start hote.
#print(l[:7])

l = [1,2,3,4,"India",7,8,"x+7j"]
print(l[2:6])

l = [2,6,4,3,6,11,9,24]
print(l[0:4])


#Method Of List :

l = []
print(type(l))

#1. append() :
#A. Adds an elements at the end of the list.(One element).

list = [2,6,4,3,6,11,9,24]
list.append("True")
print(list)

#2. insert() :
#A. Insert the value of the list.
#B. Insert an element at the specified position

list = [2,6,4,3,6,11,9,24]
list.insert(2,"false")
print(list)

list = [2,6,4,3,6,11,9,24]
list.insert(4,40)
print(list)

#3. extend() :
#A. Adds elements from another list to the end of the current list.
#B. Adds multiple elements to the list.

l1 = [1,2,3,4]
l2 = [5,6,7,8]
l1.extend(l2)
print(l1)

l1 = [1,2,3,4]
l2 = [5,6,7,8]
l2.extend(l1)
print(l2)

#4. pop() :
#A. Removes and returns the element at the specified position.
#B. (or the last element if no index is specified).

list1 =[20,42,30,46,80,68]
list1.pop(2)
print(list1)

#5. remove() :
#A. Removes the item with the specified value.

list1 =[20,42,30,46,80,68]
list1.remove(20)
print(list1)


#6. clear() :
#A. Removes all elements from the list
list1 =[20,42,30,46,80,68]
list1.clear()
print(list1)


#7. sort() :
#A. Sort the list.
#B. Arrange in ascending order.

list2 =["Apple","Orange","Cat","Bat"]
list2.sort()
print(list2)

#8. sort(reverse=True) :
#A. Arrange in descending order.

list2 =["Apple","Orange","Cat","Bat"]
list2.sort(reverse=True)
print(list2)

list1 =[20,42,30,46,80,68,90]
list1.sort(reverse=True)
print(list1)

#9. reverse() :
#A. Reverses the order of the list elements in place.

list1 =[20,42,30,46,80,68,90]
list1.reverse()
print(list1)

#10. index() :
#A. Returns the index of the first occurrence of the specified value.
#B. Raises ValueError if the value is not found.

list1 =[20,42,30,46,80,68,90]
print(list1.index(46))

#11. count() :
#A. Returns the number of occurrences of the specified value.

list1 =[20,42,30,46,80,68,90,20]
print(list1.count(20))

#12. copy() :
#A. Returns a shallow copy of the list.

list1 =[20,42,30,46,80,68,90]
list2 = list1.copy()
print(list2)

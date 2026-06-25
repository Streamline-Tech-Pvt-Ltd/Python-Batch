# Sequence Data Types

# 1.List : List is a comma separated by elements within a square brakets[].
Ex:[1,2,3,4,5]
 
 # List is a collection of items which are ordered and changeable.
 # 1.list is a mutable it can be changed
 # 2.list is order. it means the order of the elements is preserved.
 # 3.It alllows duplicate members.

 # List Operations
 # List Operations are actions that can be performed on lists, such as adding, removing, updating, searching, and combining elements.
 
# 1.Creating the list
fruits = ["Apple","Mango","Banana"]
print(fruits)
 
# 2.Accessing Elements
print(fruits[0])
print(fruits[2])

# 3.Updating Elements
fruits[1] = "Orange"
print(fruits)

# 4.Adding Elements
# append()
# adds an element at the end.
fruits.append("Banana")
print(fruits)

# 5.insert()
# adds an element at a specific position.
fruits.insert(2,"orange")
print(fruits)

# 6. remove()
# remove a specific element.
fruits.remove("Banana")
print(fruits)

# 7. pop()
# Removes an element by index.
 fruits.pop(0)
 print(fruits)

# 8. delete()
# Delets on element or entire list.
del fruits[1]
print(fruits)

# 9. extend()
# Adds Multiple Elements.
fruits.extend(["Grape","Mango","Pineapple"])
print(fruits)

# 10.sort()
# method is used to arrange the elements of a list in ascending or descending order.
fruits.sort()
print(fruits)

# 11. reverse()
# method is used to reverse the order of elements in a list.
fruits.reverse()
print(fruits)

# 12.count()
# is used to count how many times a specific element appears in a list, tuple, or string.
print(fruits.count("Mango"))

# 13.copy()
# method is used to create a copy (duplicate) of a list.
new_fruits = fruits.copy()
print(fruits)
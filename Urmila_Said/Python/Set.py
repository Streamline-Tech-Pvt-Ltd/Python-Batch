# Set data types:set()

# Set - Set are used to store a multiple data types in a single variable.
# mutable, unordered, unindexed
# dublicate values are not allowed
# set is denoted by {}

s1 = {1,2,3,4,5,6}
print(type(s1))

#1. clear() : Removes all elements from the set.
s1 = {1,2,3,4,5,"apple"}
s1.clear()
print(s1)

#2. copy() :Creates a copy of the set.
s1 = {1,2,3,4,5,"apple"}
s2 = s1.copy() 
print(s2)
print(s1)

#3. difference()- Returns elements present in the first set but not in the second
s1 = {"Apple","Mango","Banana"}
s2 = {"Microsoft","Amazon","Apple"}
print(s1.difference(s2))
print(s2.difference(s1))

#4.intersection()- Returns common elements.
s1 = {"Apple","Mango","Banana"}
s2 = {"Microsoft","Amazon","Apple"}
print(s1.intersection(s2))
print(s2.intersection(s1))

#5. union()-Combines two sets.
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.union(set2))

#6. isdisjoint() - The isdisjoint() method checks whether two sets have no common elements.
# true = If both sets have no common elements
# false = If both sets have at least one common element

s1 = {1,2,3,4}
s2 = {4,5,6}
print(s1.isdisjoint(s2))

#7. add() :Adds a single element to the set.
set1 = {1,2,3,4}
set1.add(5)
print(set1)


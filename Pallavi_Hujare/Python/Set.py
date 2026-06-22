# Set - Set are used to strore a multiple data types in a single variable.
#mutable, unordered, unindexed
#dublicate values are not allowed
#set is denoted by {}

s1 = {1,2,3,4,5,6}
print(type(s1))

#set methods

#1. clear() -
s1 = {1,2,3,4,5,"apple"}
s1.clear()
print(s1)   #set()

#2. copy()
s1 = {1,2,3,4,5,"apple"}
s2 = s1.copy() 
print(s2)
print(s1)

#3. difference()-
s1 = {"Apple","Mango","Banana"}
s2 = {"Microsoft","Amazon","Apple"}
print(s1.difference(s2))
print(s2.difference(s1))

#4.intersection()-
s1 = {"Apple","Mango","Banana"}
s2 = {"Microsoft","Amazon","Apple"}
print(s1.intersection(s2))
print(s2.intersection(s1))

#5. union()-
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.union(set2))

#6. isdisjoint() - 
# true = different values
#false = common values

s1 = {1,2,3,4}
s2 = {4,5,6}
print(s1.isdisjoint(s2))

#7. add()
set1 = {1,2,3,4}
set1.add(5)
print(set1)
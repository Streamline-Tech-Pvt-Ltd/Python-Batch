# Tuple - Tuple is a collection of multiple data items in a simgle variable.
# Tuple is denoted by ()
#Tuple is immutable
#tuple is ordered

tuple1 = (1,2,3,4,5,6,7,"India","Pune",[1,2,3])
print(type(tuple))
print(tuple1[: : -1]) #reverse the tuple
print(tuple1[:]) # all tuple elements
print(len(tuple1))
print(tuple1[9][1])

#tuple methods
#1. index() - index() method is used to return the index of the first occurrence of the specified value.
tuple1 = (1,2,3,4,5,6,7,"India","Pune",[1,2,3])
print(tuple1.index("India"))

#2. concatenation - we can add one or more tuples

t1 = (1,2,3)
t2 = (4,5,6)
t = t1 + t2
print(t)

#3. repetition - we can repeat a tuple for a specified number of times using the * operator.
t3 = (1,2,3)
t4 = t3 * 2
print(t4)

t = t4 * 2
print(t)

#4. count() - count() method is used to count the number of occurrences of a specified value in a tuple.
tuple1 = (1,2,3,4,2,4,1,1,5,3,6)
print(tuple1.count(2))


t1 =("Apple","Bannana","Pinnapple","Graphs","Coconut")
print(t1[1])
print(t1[3])
# list:- list is a comma seprated by elements within a square brakets.[]
# Ex:- [1,2,2,3,4,5]
        # 0,1,2,3,4
        #-4,-3,-2,-1


# list is a collection of items which are ordered and changeable.
# 1. list is mutable.it can be changed.
# 2. list is ordered.it means the order of the elements is preserved.
# 3. it allows duplicate members.

# Method	                Purpose

# append()           	Add one item at end
# extend()	        Add multiple items
# insert()	       Add item at specific index
# pop()	            Remove item by index
# remove()	         Remove item by value
# clear()	            Remove all items
# count()	            Count occurrences
# copy()	            Create copy of list
# sort()	             Sort list
# reverse()	         Reverse list order



l1 = [1,2,2,2,3,4,5]
print(l1)


l1.append(2)
print(l1)  #[1, 2, 2, 2, 3, 4, 5, 2]

l1.extend([6,7,8,9,10])
print(l1)    #[1, 2, 2, 2, 3, 4, 5, 2, 6, 7, 8, 9, 10]

l1.insert(2,0)
print(l1)    #[1, 2, 0, 2, 2, 3, 4, 5, 2, 6, 7, 8, 9, 10]

l1.pop(5)
print(l1)  #[1, 2, 0, 2, 2, 4, 5, 2, 6, 7, 8, 9, 10]

l1.clear()
print(l1)  #[ ]

l1 = [1,2,2,2,3,4,5]
print(l1)

l1.remove(5)
print(l1) #[1, 2, 2, 2, 3, 4]


print(l1.count(2))  #3

l1.copy()
print(l1) #[1, 2, 2, 2, 3, 4]

l2 = [1,2,20,4,5,2,10,9,7]

l2.sort()
print(l2) # [1, 2, 2, 4, 5, 7, 9, 10, 20]

l2.reverse()
print(l2)  # [20, 10, 9, 7, 5, 4, 2, 2, 1]


#Additional functions 
# index()            	Returns the index of a specified value
# len()	            Returns the number of elements in the list
# min()	            Returns the smallest element
# max()	            Returns the largest element
# sum()	            Returns the sum of all elements
# sorted()	        Returns a new sorted list without changing the original list
# del	                Deletes an element or entire list
# in	                Checks if an element exists in the list
# not in	            Checks if an element does not exist in the list


# Examples

l1 = [1,2,3,4,5]

#index()
print(l1.index(3))
# Output: 2

# len()
print(len(l1))
# Output: 5

# min()
print(min(l1))
# Output: 1

# max()
print(max(l1))
# Output: 5

# sum()
print(sum(l1))
# Output: 15
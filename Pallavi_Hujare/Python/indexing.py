#indexing:- indexing is used to access the single elements of the list.
#  Indexing means accessing elements of a sequence (like a list, tuple, string) using their position (index).

# Python uses zero-based indexing: first element is at index 0.
# Negative indexing starts from the end: last element is -1.
#Ex.  

l1 = [1,2,3,4,5,6]
print(l1[2])   #3
print(l1[-4])  #3
print(l1[-5])  #2


l1 = [1,2,3,[4,5,6],7]
print(l1[-2][-1])
# Output: 6


name = "Pallavi"
print(name[5])
# Output: v

l1 = [100,200,300,400,500]
print(l1[4])
# Output: 500

l1 = [1,2,3,[4,5,6],7]
print(l1[3][2])
# Output: 6


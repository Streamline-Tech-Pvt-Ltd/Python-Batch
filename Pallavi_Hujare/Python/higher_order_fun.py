# Higher order Functions
# # function that work with other function

#map() 
# used to apply function to every element of a list
num = [1,2,3,4,5,6,7,8,9]
result= list(map(lambda x : x * x,num))
print(result)

#filter
# used to filter condition based on a condition
num = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda x:x%2 == 0,num))
print(even)

#reduce
#  reduce a list to a single value
from functools import reduce
number = [1,2,3,4,5]
result = reduce(lambda a, b : a + b,number)
print(result)

#map()
num = [1,2,3,4,5,6,7,8,9]
result= list(map(lambda x : x * x,num))
print(result)

#filter
num = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda x:x%2 == 0,num))
print(even)

#reduce
from functools import reduce
number = [1,2,3,4,5]
result = reduce(lambda a, b : a + b,number)
print(result)

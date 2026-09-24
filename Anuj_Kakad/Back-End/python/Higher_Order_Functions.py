# Examples Of map() Higher Order function:-

# Example 1: Square of numbers
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * x, numbers))

print(result)


print()
# Example 2: Double the numbers
numbers = [10, 20, 30, 40]

result = list(map(lambda x: x * 2, numbers))

print(result)


print()
# Example 3: Convert names to uppercase
names = ["anuj", "rahul", "amit"]

result = list(map(lambda x: x.upper(), names))

print(result)


print()
# Examples on filter() Higher order Function:-

# Example 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)


print()
# Example 2: Find numbers greater than 10
numbers = [5, 12, 8, 20, 15]

result = list(filter(lambda x: x > 10, numbers))

print(result)


print()
# Example 3: Filter names starting with "A"
names = ["Anuj", "Rahul", "Amit", "Sneha"]

result = list(filter(lambda x: x.startswith("A"), names))

print(result)


print()
# Examples on reduce() higher Order Function:-

# Example 1: Sum of numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)


print()
# Example 2: Product of numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x * y, numbers)

print(result)


print()
# Example 3: Find the largest number
from functools import reduce

numbers = [10, 25, 8, 40, 15]

result = reduce(lambda x, y: x if x > y else y, numbers)

print(result)


# 4 
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = 0

for num in list3:
    res = res + num

print(res)


from functools import reduce

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
res = reduce(lambda a, b: a + b, list3)

print(res)

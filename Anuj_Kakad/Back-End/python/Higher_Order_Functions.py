list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = 0

for num in list3:
    res = res + num

print(res)


from functools import reduce

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
res = reduce(lambda a, b: a + b, list3)

print(res)

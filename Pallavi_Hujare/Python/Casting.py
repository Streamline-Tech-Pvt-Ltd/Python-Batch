# Type Casting: Convert a one data type into another data type.

# types of casting:
# 1. Implicit type-casting: Automatically convert one data type to another
# int -> float
# n1 = 10
# n2 = 10.5
# print(type(n1 + n2))
 
# int -> complex
# n1 = 10
# c = 2 + 2j
# print(n1 + c)

# float -> int
# n1 = 10.5
# n2 = 20
# print(type(n1 + n2))
# print(n1 + n2)

# float -> complex
# n1 = 10.5
# c = 2 + 2j
# print(n1 + c)




# 2. Explicit type-casting: Manually convert one data type to another using a function.
# function: int()
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()


# 1. int()

# str -> int
num = "100"
print(int(num))          # 100



# 2. float()
# str -> float
num = "10.5"
print(float(num))        # 10.5



# 3. str()
# int -> str
age = 20
print(str(age))          # '20'

name = "Rahul"
print(name + str(age))   # Rahul20



# 4. list()
# str -> list
name = "Pallavi"
print(list(name))
# ['P', 'a', 'l', 'l', 'a', 'v', 'i']

# tuple -> list
t = (1, 2, 3)
print(list(t))
# [1, 2, 3]

# set -> list
s = {1, 2, 3}
print(list(s))
# [1, 2, 3]

# dict -> list
d = {"name": "Pallavi", "age": 20}
print(list(d))
# ['name', 'age']


# 5. tuple()

# list -> tuple
l = [1, 2, 3]
print(tuple(l))
# (1, 2, 3)


# 6. set()

# list -> set
l = [1, 2, 2, 3]
print(set(l))
# {1, 2, 3} # Duplicate values are removed automatically.


# 7. dict()

# list of tuples -> dict
data = [("name", "Pallavi"), ("age", 20)]
print(dict(data))
# {'name': 'Pallavi', 'age': 20}


# 8. bool()

# int -> bool
print(bool(1))     # True
print(bool(0))     # False

# str -> bool
print(bool("Python"))   # True
print(bool(""))         # False



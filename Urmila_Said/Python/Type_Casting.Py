# Type Casting: Convert a one data type into another data type.

# types of casting:
# 1. Implicit type-casting: Automatically convert one data type to another
# 2. Explicit type-casting: Manually convert one data type to another using a function.
# function:
# int()
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()


# Implicit type casting function
# int -> float
# int -> complex
# float -> int
# float -> complex

# n1 = 10
# n2 = 10.5
# print(type(n1 + n2))

# n1 = 10
# c = 2 + 2j
# print(n1 + c)

# n1 = 10.5
# n2 = 20
# print(type(n1 + n2))
# print(n1 + n2)

# n1 = 10.5
# c = 2 + 2j
# print(n1 + c)

# Explicit type casting

# name = "Rahul"
# age = 20
# print(name + str(age))

# l1 = (1,2,3,4,5)
# print(type(list(l1)))

# stu_name = [("name","Pallavi"),("name1","Pallavi")]
# print(dict(stu_name))

# s1 = [1,2,3,2,4,4,4,5]
# print(set(s1))

# # Practice example

# Implicit type casting

# a = 10
# b = 20.5
# print(a + b) 
# O/P :30.5    ( Convert float)

# a = 20
# b = 2 + 3j
# print(a + b)
# O/P: (22+3j)   (Convert complex data type)

# a = 50.5
# b = 10
# print(a + b)
# O/P: 60.5          (Convert float)

# a = 5 + 5j
# b = 20
# print(a + b)
# O/P: (25+5j)          (Convert complex)

# a = 10.15
# b = 5 + 15j
# print(a + b)
# O/P: (15.15+15j)        (Convert Complex)


# Explicit Type Casting

# name = "Urmila"
# age = 21
# print(name + str(age))
# O/P: Urmila21

# name = "Urmila"
# marks = 90.5
# print(name + str(marks))
# O/P: Urmila90.5

# a = 45.5
# print(int(a))
# print(type(a))
# O/P: 45                (Convert float into int))
#      <class 'float'>

# a = 50
# print(float(a))
# print(type(a))
# O/P : 50.0                 (Convert int into float)
#       <class 'int'>

# name = "Urmila"
# print(list(name))
# print(type(name))
# O/P: ['U', 'r', 'm', 'i', 'l', 'a']        (Convert string into list)
#      <class 'str'>

# num = [10,20,30]
# print(tuple(num))
# print(type(num))
# O/P :(10, 20, 30)            (Convert list into tuple)
#      <class 'list'>

# num = [1,2,3,4,5,6,2,3,4,1]
# print(set(num))
# print(type(num))
# O/P: {1, 2, 3, 4, 5, 6}        (Covert list into set)
#      <class 'list'>

# student = (("Name","Urmila"),("Age",21),("Coure","Computer Science"))
# print(dict(student))
# print(type(student))
# O/P: 'Name': 'Urmila', 'Age': 21, 'Coure': 'Computer Science'}    (Convert tuple into dict)
#       <class 'tuple'>

# print(bool("Python"))
# O/P: True


# Higher Order Function: A function that works with another function is called a Higher Order Function.
# A Higher Order Function (HOF) is a function that takes another function as an argument or returns a function as a result.

# Some Higher order function in python
# map()
# filter()
# sorted()
# reduce() (from the functools module)

# 1. map()
# Used to apply a function to every element of a list.

# num = [1,2,3] 
# result = list(map(lambda x:x + 5,num))
# print(result)

# 2.filter()
# Used to filter elements based on a condition.

# num = [2,4,3,5,1,5,6]
# square = list(filter(lambda x: x%2 == 0,num))
# print(square)

# 3. reduce() 
# reduce a list to a single value

# from functools import reduce
# num = [1,2,3,4,5]
# num = (reduce(lambda  a,b : a + b,num))
# print(num)

# 3. sorted()
# Accepts a function through the key parameter.

# words = ["banana", "kiwi", "apple", "mango"]
# result = sorted(words, key=len)
# print(result)



# Types of variable: 
# 1. Local variable: Local vairable is used inside a function.

# def my_fun():

#     name = "Sai" #local variable

#     print(name)
# my_fun()
# print(name) #outside a function not work


# 2. Global variable : Global variable is used outside a function.

# name = "Pallavi" # global variable

# def my_fun():

#     print(name)

# my_fun()
# print(name)


# global keyword:

# Stu_name = "Pallavi"
# def change():
#     global Stu_name

#     name = "Urmila"

#     print(name)
    
# change()

# print(Stu_name)

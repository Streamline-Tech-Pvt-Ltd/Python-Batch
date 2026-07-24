# Function: A function is a collection of statements and a set of instructions.
# function run only when it is called.

# Syntax - 
    #    def function_name(parameters): #define/create a function
    #         statements

    #     function_call(arguments) #calling function

# parameters : is the variable listed inside the parenthesis in the function definitation.
    #def add(a,b): # a,b is a parameters

# Arguments: is the value that is sent to the function when it is called.
    # add(10,2) # 10 and 2 is arguments


# def my_fun():
#     print("Hello world!")

# my_fun()
# my_fun()
# my_fun()

# def add(a,b):
#     # print("The addition of a and b is :", a + b)
#     return a + b , a - b

# addition = add(10,2)
# print("The addition of a and b is :", addition)

#difference between print and return

# Types of function : 
# 1. Built-in function : already define in python. print(),len(),return()...
# 2. User-defined function : Created by user.
# 3. Lambda function : one line function.
# 4. Recursive function : These are function that call themselves within their definition.

# 1. Built-in function :

# print("Welcome")

# print(len("Welcome"))

# def square(a):
#     return a * a
# sq = square(2)
# print("The square is:",sq)

# def even_odd(num):
#     if num % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")

# even_odd(3)

#Practice question:
#Q1.print Arithematic operators using function
# def arithmetic(a, b):
#     print("Addition =", a + b)
#     print("Subtraction =", a - b)
#     print("Multiplication =", a * b)
#     print("Division =", a / b)
#     print("Modulus =", a % b)
# arithmetic(15,25)

#Q2.print a number is natural or not using a function
# def check_natural(n):
#     if n > 0:
#         print("Natural Number")
#     else:
#         print("Not Natural Number")
# check_natural(2)

    
#3.Create a function to find maximum of two numbers.
# def maximum(a,b):
#     if a > b:
#         return a
#     else:
#         return b    
# max_no = maximum(10,20)
# print("The Maximum no is:", max_no)
    

#4.Create a function to calculate area of circle.
# def area_circle(r):
#     area = 3.14 * r * r
#     return area
# result = area_circle(5)
# print("Area of circle:",result)

    
#5.Create a function to check prime number..
# def prime(num):

#      if num <= 1:
#          return "Not prime Number"
    
#      for i in range(2, num):
#          if(num % i == 0):
#              return "Not prime number"
      
#      return "Prime Number"
        
# print(prime(2))

        
#6.Find a factorial
#n = int(input("Enter a number: "))
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact
# print(factorial(n))


# 3. Lambda function: one line , small function.
#    Lambda function is a small anonymous (nameless) function in Python. 
#    It is created using the lambda keyword and is used for short, simple operations.
# Syntax :   lambda arguments : expression;

# add = lambda a,b : a + b
# print(add(10,2))

# square = lambda x : x*x
# print(square(2))


#4. Recursive function: A recursive function is a function that calls itself to solve a problem. 
# Instead of using loops (for or while), recursion solves a problem by breaking it into smaller subproblems.

# Print a factorial number using recursive function.
# def factorial(n):
    
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     print(fact)

# factorial(5)

# def factorial(n):
#   if n == 1 or n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# Practice Question:
# Write a lambda function to check whether a number is even or odd.
# n = 7
# check = lambda n :"Even" if n % 2 == 0 else "Odd"
# print(check(n))

# Write a lambda function to find the larger of two numbers. 
# a = 2
# b = 20
# max = lambda a, b: a if a > b else b
# print("Larger Number:", max(a,b))

# larger = lambda a,b : a < b
# print(larger(10,20))

# Write a lambda function to multiply two numbers.
# multiplication = lambda a,b: a * b
# print(multiplication(5,2))

# Write a recursive function to print numbers from 1 to N.
# def numbers(n):
#     if n == 0:
#         return
#     numbers(n - 1)
#     print(n)    
# numbers(10)

# Write a recursive function to calculate the sum of first N natural numbers.
# def sum_n(n):
#     if n == 0:
#         return 0
#     return n + sum_n(n - 1)
# print(sum_n(5))

# Write a recursive function to calculate the power of a number.
# def power(a, b):
#     if b == 0:
#         return 1
#     return a * power(a, b - 1)
# print(power(5,5))
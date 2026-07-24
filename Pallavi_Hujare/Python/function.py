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

#Q1.print Arithematic operators using fun

# def arithmatic_operation(a,b):
#     print("The addition of a and b is:",a + b)
#     print("The Substraction is:",a - b)
#     print("The Multiplication is :", a* b)
#     print("The dividetion is:",a / b)
# arithmatic_operation(2,2)


#Q2.print a number is natural or not using a fun

# def natural_Number(a):
#     if a >=1:
#         print("Number is Natural")
#     else:
#         print("Not a Natural Number")
# natural_Number(1)
    

#3.Create a function to find maximum of two numbers.
# def Max_No(a , b):
#     if(a>b):
#         print(a)
#     else:
#         print(b)
# Max_No(10,1)
#4.Create a function to calculate area of circle.

#4.Create a function to calculate area of circle.
# def area_circle(r):
#     area = 3.14 * r * r
#     return area
# result = area_circle(5)
# print("Area of circle:",result)

#5.Create a function to check prime number.

# def Prime_Number(a):
#      if a <= 1:
#          print("Number is Not Prime")
#          return
#      for i in range(2, a):
#          if a % i == 0:
#              print("Number is Not Prime")
#              return
#      print("Number is Prime")
# Prime_Number(2)

# Lambda function: one line , small function.
# Lambda function is also known as anonymous function.

# Syntax :   lambda arguments : expression;

# add = lambda a,b : a + b
# print(add(10,2))

# square = lambda x : x*x
# print(square(2))

# Recursive function: a function that call itself.

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     print(fact)

# factorial(5)
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# Practice Question:
# Write a lambda function to check whether a number is even or odd.
# even_or_odd = lambda a: "Even" if a % 2 == 0 else "Odd"
# print(even_or_odd(3))

# Write a lambda function to find the larger of two numbers.
# larger_no = lambda a , b: "a is Larger" if a > b else "b i Larger"
# print(larger_no(3,7))

# Write a lambda function to multiply two numbers.
# Multiplication = lambda a, b : a * b
# print(Multiplication(2,2))


# Write a recursive function to print numbers from 1 to N.
# def num(n):
#     i = 1
#     while(i <= n):
#         print(i)
#         i = i + 1
# print(num(10))


# Write a recursive function to calculate the sum of first N natural numbers.

# def sum_n(n):
#     if n == 1:          
#         return 1
#     else:
#         return n + sum_n(n - 1)
# print(sum_n(2))


# Write a recursive function to calculate the power of a number.

# def power(base, exp):
#     if exp == 0:
#         return 1
#     else:
#         return base * power(base, exp - 1)
# print(power(2,2))
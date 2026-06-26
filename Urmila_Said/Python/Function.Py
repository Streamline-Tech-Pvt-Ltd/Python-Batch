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
def check_prime(n):
     if n <= 1:
         return False
     for i in range(2, n):
         if n % i == 0:
             return False
        
#6.Find a factorial
#n = int(input("Enter a number: "))
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact
# print(factorial(n))
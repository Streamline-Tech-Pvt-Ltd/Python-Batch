#  Exception Handling : 
# Exception Handling is a mechanism in Python used to handle runtime errors without stopping the execution of the program.
# eval -- without take int float in input



#****************Practice******************
# print("Welcome To Bank of Maharastra")
# balance = 5000000
# while True:
#     try:
#         withdraw_amount = int(input("Enter amount : "))
#         pin = int(input("Enter 4 digit pin : " ))
#         if withdraw_amount <= balance:
#             balance -= withdraw_amount
#             print("Your Available balance is : ",balance)
#             print("Transection is Complited Successfully ")
#             print("*****Thank you*****")
#         else:
#             print("Inssuficcient Balence")
#             print("Transection is Complited")
#             print("*****Thank you******")
#     except ValueError:
#        print("Invalid input")
#        print("Please try again")
#        print("*****Thank you******")


# What is an Exception?

# An Exception is an event that occurs during program execution and interrupts the normal flow of the program.

# Examples:
# Divide by zero
# File not found
# Wrong input
# Invalid index
# Invalid key


#ZeroDivisionError
try:
    a = 20
    b = 0
    print(a / b)
except:
    print("Division by zero is not allowed")


# ValueError
try:
    age = int(input("Enter Age: "))
except:
    print("Please enter numbers only")

# IndexError
list1 = [10,20,30]
try:
    print(list1[5])
except:
    print("Index does not exist")

#NameError
print(total_amount)

#ImportError
from math import square

#AttributeError
name = "Python"
name.append("3")

# KeyError
student = {"name":"Pallavi"}
try:
    print(student["age"])
except:
    print("Key not found")

# FileNotFoundError
try:
    file = open("data.txt")
except:
    print("File does not exist")

# Multiple except Blocks
# Different exceptions can be handled separately.

# try:
#     number = int(input("Enter Number: "))
#     print(100 / number)
# except ValueError:
#     print("Invalid Number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else Block
# The else block runs only if no exception occurs.
# Syntax

# try:
#     pass
# except:
#     pass
# else:
#     pass

# finally Block
# The finally block always executes, whether an exception occurs or not.
# Syntax

# try:
#     pass
# except:
#     pass
# finally:
#     pass

# Example

# try:
#     print(10/0)
# except:
#     print("Error")git status
# finally:
#     print("Program Finished")

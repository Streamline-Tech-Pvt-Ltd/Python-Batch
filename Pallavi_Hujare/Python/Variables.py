#Date : 11/06/2026


# Variables in Python
#type of container where we can store the value

# Rule 1: Variable name should start with A-Z, a-z, or _
name = "Pallavi"
print(name)

_name = "Pallavi"
print(_name)

# Rule 2: Variable names are case-sensitive
Name = "Pallavi"
name = "Hujare"

print(Name)  # Pallavi
print(name)  # Hujare

# Rule 3: Special characters are not allowed
# Invalid:
# @name = "Pallavi"
# print(@name)

# Rule 4: Spaces are not allowed
# Invalid:
# my name = "Pallavi"
# print(my name)

# Correct:
my_name = "Pallavi"
print(my_name)

# Rule 5: Variable name cannot start with a number
# Invalid:
# 1Name = "Pallavi"

# Correct:
name1 = "Pallavi"
print(name1)

# Rule 6: Keywords cannot be used as variable names
# Invalid:
# if = "Pallavi"
# print(if)

# Correct:
student_name = "Pallavi"
print(student_name)


#Naming Conventions (Cases)

# snake_case (recommended for variables)  #*******Variables & Functions → snake_case
pallavi_hujare = "Python Student"

# camelCase
pallaviHujare = "Web Developer"

# PascalCase (used for classes)
class PallaviHujare:
    pass

# UPPER_CASE (used for constants)
PALLAVI_HUJARE = "Constant Value"




#*******Variables & Functions → snake_case


#Keyword: A keyword is a reserved word in Python that has a predefined meaning and cannot be used as an identifier (variable name, function name, or class name).
         #Examples: if, else, for, while, True, False, class, def, return.

#Check All Python Keywords
import keyword
print(keyword.kwlist)

'''['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
  'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']'''




#f-String in Python

#Definition:
 #An f-string (formatted string) is used to insert variables or expressions directly inside a string using {} brackets.

#Syntax
#   f"Text {variable}" 

#Example 1: Variable

name = "Pallavi"
print(f"My name is {name}")  #My name is Pallavi





#Input Function in Python

#Definition

# The input() function is used to take input from the user through the keyboard.

# Syntax
# variable_name = input("Enter value: ")
# Example 1: Taking Name as Input

name = input("Enter your name: ")
print("Name:", name)

# Input:
# Pallavi

# Output:
# Name: Pallavi



#Example 2: Taking Number Input
num = int(input("Enter a number: "))
print(num)

# Input:
# 10

# Output:
# 10


#**********Important Note

# input() always returns data as a string.

age = input("Enter age: ")
print(type(age))

# Output:
# <class 'str'>

#To use numbers, convert them using int() or float():


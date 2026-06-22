# Practice Question

# 1.Arithmetic Operators

# Create a program that takes two numbers from the user and performs:

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modulus (%)
# Exponent (**)
# Floor Division (//)
a = int(input("Enter the First Number :"))
b = int(input("Enter the Secound Number :"))
print("Addition is :",a+b)
print("Subtraction is :",a-b)
print("Multiplication  is :",a*b)
print("Division is :",a/b)
print("Modulus is :",a%b)
print("Exponent is :",a**b)
print("Floor Division is :",a//b)
# 2: Comparison Operators

# Take two numbers from the user and compare them using:

# ==
# !=
# >
# <
# >=
# <=
a = int(input("Enter the First Number :"))
b = int(input("Enter the Secound Number :"))
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >=b)
print(a <= b)
# 3: Logical Operators

# Create a program to check student eligibility for placement.

# Conditions:

# Age must be 18 or above.
# Percentage must be 60 or above.

age = int(input("Enter your age :"))
percentage = int(input("Enter Your percentage :"))
print((age >= 18) and (percentage >= 60))

age = int(input("Enter your age :"))
percentage = int(input("Enter Your percentage :"))
print((age >= 18) or (percentage >= 60))
  
age = int(input("Enter your age :"))
percentage = int(input("Enter Your percentage :"))
print(not ((age >= 18) and (percentage >= 60)))



# Use and, or, and not operators.

# 4.Assignment Operators

# Create a variable salary = 25000 and perform:
salary = 25000
num =int(input("Enter The Salary Amount :"))

salary += num
print(salary)

salary -= num
print(salary)

salary *= num
print(salary)

salary /= num
print(salary)

salary %= num
print(salary)


# +=
# -=
# *=
# /=
# %=

# 5: Bitwise Operators

# Take two numbers:

# a = 12
# b = 5
a = 12
b = 5
print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(~ a)
print(~ b)
# Perform:

# &
# |
# ^
# ~
# <<
# >>
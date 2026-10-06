
# Operator : Operators are special symbols used to perform operations on variables and values.

# Operands : Operands are the values or variables on which an operator performs an operation.

# Ex: a + b
     # Operands: a and b
     # Operator: +


## 1. Arithmetic Operators in Python
# Arithmetic operators are used to perform mathematical calculations on numbers.

# 1.Addition (+) :Adds two values
a = 10
b = 3
print("Addition:", a + b)

# 2.Subtraction (-): Subtracts one number from another.
a = 20
b = 10
print("Substraction:",a - b)

# 3.Multiplication (*): Multiplies two numbers.
a = 5
b = 4
print("Multiplication:",a * b)

# 4.Division (/): Divides one number by another and returns a float value.
a = 10
b = 2
print("Division:",a / b)

# 5.Modulus (%): Returns the remainder after division.
a = 10
b = 3
print("Modulus:",a % b)

# 6.Exponentiation (**): Raises a number to the power of another number.
a = 2
b = 3
print("exponentiation:",a ** b)

# 7. Floor Division (//) : Returns only the integer part of the division result (removes decimal part).
a = 10
b = 3
print("Floor Division:",a // b)


a = 10
b = 2
print("Addition is :", a+b)
print("Subtraction is : ",a-b)
print("Multiplication is : ",a*b)
print("Dividation is : ",a/b)
print("Expansion is :",a**b)
print("Quotient is :",a//b)



## 2. Assignment operators : Assignment operators assign values to variables.

# 1.Simple Assignment Operator (=): The = operator assigns a value to a variable.
a = 10
b = 5

# 2.Add and Assign (+=): Adds a value and assigns the result to the same variable.
a = 10
b = 5
a += b
print(a)

# 3.Subtract and Assign (-=): Subtracts a value and assigns the result..
a = 10
b = 5
a -= b
print(a)

# 4.Multiply and Assign (*=): Multiplies and assigns the result.
a = 10
b = 5
a *= b
print(a)

# 5.Divide and Assign (/=): Divides and assigns the result..
a = 10
b = 5
a /= b
print(a)

# 6.Floor Divide and Assign (//=): Performs floor division and assigns the result.
a = 10
b = 5
a //= b
print(a)

# 7.Modulus and Assign (%=): Finds the remainder and assigns it.
a = 10
b = 5
a %= b
print(a)

# 8.Exponent and Assign (**=): Raises a number to a power and assigns the result.
a = 10
b = 5
a **= b
print(a)



## 3. Comparision operator: Comparison Operators (Relational Operators) are used to compare two values or variables. 
#    The result of a comparison is always either True or False.

# 1.Equal To (==)
a = 10
b = 10
print(a == b)

# 2.Not Equal To (!=)
a = 10
b = 20
print(a != b)

# 3.Greater Than (>)
a = 20
b = 10
print(a > b)

# 4.Less Than (<)
a = 10
b = 20
print(a < b)

# 5.Greater Than or Equal To (>=)
a = 10
b = 10
print(a >= b)

# 6.Less Than or Equal To (<=)
a = 10
b = 20
print(a <= b)



## 4.Membership Operator: Membership Operators are used to check whether a value is present in a sequence
#    such as a string, list, tuple, set, or dictionary.
# Two Membership Operator
#1.in
#2.not in

# 1.in Operator: The in operator returns True if the specified value exists in the sequence; otherwise, it returns False.
a = [10, 20, 30, 40]
print(20 in a)
print(50 in a)

# 2.not in Operator: The not in operator returns True if the specified value does not exist in the sequence; otherwise, it returns False.
a = [10, 20, 30, 40]
print(50 not in a)
print(20 not in a)



## 5.Identical Operator: Identity Operators are used to compare the memory location (identity) of two objects.
# Two Identity Operators:
#1.is
#2.is not

#1.is operator: The is operator returns True if both variables point to the same object in memory.
a = [10, 20, 30]
b = a
print(a is b)

#2.is not operator: The is not operator returns True if both variables refer to different objects.
a = [10, 20, 30]
b = [10, 20, 30]
print(a is not b)

#5. Logical operator: (and, or , not):

#and: returns true if both conditions are true
#1 = true, 0 = false

# 1 and 1 = 1
# 1 and 0 = 0
# 0 and 1 = 0
# 0 and 0 = 0

# or :  returns true if one of the condition is true

# 1 or 1 = 1
# 1 or 0 = 1
# 0 or 1 = 1
# 0 or 0 = 0

# not : reverse the result. returns false if the result is true.

# not (1) = false
# not (0) = true

x = 6
print( x > 5 and x < 10)

x = 20
print(x > 21 or x > 50)

x = 20
print(not(x > 21 or x < 50))

a = 10
print(not(a <= 15))


#6. Bitwise operator : &, |, ~, ^

a = 10
b = 4
print(a & b)

a = 10
b = 4
print(a | b)

x = 20
y = 15
print(x ^ y)

# 16 8 4 2 1 
# 1 0 1 0 0
# 0 1 1 1 1 
# ---------------
# 1 1 0 1 1 

a = 10  # --- ans -ve and +1
print(~ a)

a = 43
print(~ a)

# Left Shift (<<)-- add a number in left side
#formula = number << n
           # number * 2^n
a = 5 
b = 2
print(a << b)

# Right shift -- cut a number in right side
#formula = number << n
           # number / 2^n
a = 5 
b = 2
print(a >> b)



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

# 2: Comparison Operators

# Take two numbers from the user and compare them using:

# ==
# !=
# >
# <
# >=
# <=

# 3: Logical Operators

# Create a program to check student eligibility for placement.

# Conditions:

# Age must be 18 or above.
# Percentage must be 60 or above.

# Use and, or, and not operators.

# 4.Assignment Operators

# Create a variable salary = 25000 and perform:

# +=
# -=
# *=
# /=
# %=

# 5: Bitwise Operators

# Take two numbers:

# a = 12
# b = 5

# Perform:

# &
# |
# ^
# ~
# <<
# >>
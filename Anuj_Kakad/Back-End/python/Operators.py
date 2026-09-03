#Practice Questions on Operators:-

# 1. Arithmetic Operators:-
print("Arithmetic Operators:-")
# 1. Addition:-

a = 10
b = 20

print("The Sum of a and b is:-", a + b)

# 2. Subtraction:-

print("The Difference of a and b is:-", a - b)

# 3. Multiplication:-

print("The Product of a and b is:-", a * b)

# 4. Division:-

print("The Quotient of a and b is:-", a / b)

# 5. Modulus:-

print("The Remainder of a and b is:-", a % b)

# 6. Exponentiation:-

a = 2
b = 3
print("The Result of a raised to the power of b is:-", a ** b)

print()

# 2. Comparison Operators:-

print("Comparison Operators:-")

A = 100
B = 225

# 1. Equal to:-
print("Is A equal to B? :-", A == B)

# 2. Not Equal to:-
print("Is A not equal to B? :-", A != B)

# 3. Greater than:-
print("Is A greater than B? :-", A > B)

# 4. Less than:-
print("Is A less than B? :-", A < B)

# 5. Greater than or equal to:-
print("Is A greater than or equal to B? :-", A >= B)

# 6. Less than or equal to:-
print("Is A less than or equal to B? :-", A <= B)

print()

# 3. Logical Operators:-

print("Logical Operators:-")

# 1. And Operator:-

Age = 25
percentage = 75

# Check eligibility for placement

print("Is the candidate eligible for placement? :-", Age >= 18 and percentage >= 60)

# 2. Or Operator:-

age = 15
percentage = 59

print("Is the candidate eligible for placement? :-", age >= 18 or percentage >= 60)

# 3. Not Operator:-

print("Is the candidate not eligible for placement? :-", not (age >= 18 and percentage >= 60))

print()

# 4. Assignment Operators:-

print("Assignment Operators:-")

salary = 25000

# 1. Addition Assignment Operator:-

salary += 5000
print("The Updated Salary after Addition is:-", salary)

# 2. Subtraction Assignment Operator:-

salary -= 3000
print("The Updated Salary after Subtraction is:-", salary)

# 3. Multiplication Assignment Operator:-

salary *= 2
print("The Updated Salary after Multiplication is:-", salary)

# 4. Division Assignment Operator:-

salary /= 4
print("The Updated Salary after Division is:-", salary)

# 5. Modulus Assignment Operator:-

salary %= 1000
print("The Updated Salary after Modulus is:-", salary)

print()

# 5. Bitwise Operators:-

print("Bitwise Operators:-")

# 1. (&) AND Bitwise Operator:-

x = 10
y = 4
print("The Result of x AND y is:-", x & y)

# AND Bitwise operator Solution:-
# binary no of (x)10 =	  1 0 1 0
# 	            (y)4  =	& 0 1 0 0
# 			              _______
# 			              0 0 0 0 = 0

# 2. (|) OR Bitwise Operator:-

x = 9
y = 7
print("The Result of x OR y is:-", x | y)

# OR Bitwise operator Solution:-
# 	    9 = 1 0 0 1
# 	    7 = 0 1 1 1
# 	        _______
# 	        1 1 1 1 = 15

# 3. (^) XOR Bitwise Operator:-

x = 15
y = 10
print("The Result of x XOR y is:-", x ^ y)

# XOR Bitwise operator Solution:-
# 	    15 = 1 1 1 1
# 	    10 = 1 0 1 0
# 	         _______
# 	         0 1 0 1 = 5

# 4. (~) NOT Bitwise Operator:-

x = 94
print("The Result of NOT x is:-", ~x)

# NOT Bitwise operator Solution:-
# 	    ~x = -(x + 1)
#       ~94 = -(94 + 1)
#       ~x = -95
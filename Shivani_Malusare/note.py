1. Variables
Definition
A variable is a name used to store a value in memory.
In Python, we do not need to declare the data type of a variable. Python automatically identifies the data type.
Syntax
variable_name = value
Examples
name = "Shivani"
age = 21
marks = 85.5
Here:
name → variable
"Shivani" → string value
age → variable
21 → integer value
marks → variable
85.5 → float value
Example
name = "Shivani"
age = 21

print(name)
print(age)
Output:
Shivani
21
Dynamic Typing
Python allows the same variable to store different types of values.
x = 10
print(x)

x = "Hello"
print(x)
Output:
10
Hello
2. Keywords
Definition
Keywords are reserved words in Python that have a special meaning.
We cannot use keywords as variable names.
Common Python Keywords
Keyword
Use
if
Checks a condition
else
Executes when condition is false
elif
Checks another condition
for
Loop
while
Loop
break
Stops a loop
continue
Skips current iteration
def
Defines a function
return
Returns a value
class
Creates a class
import
Imports a module
from
Imports specific things
in
Checks membership
is
Checks object identity
and
Logical AND
or
Logical OR
not
Logical NOT
True
Boolean true
False
Boolean false
None
Represents no value
Example
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
Here, if and else are keywords.
Important
❌ You cannot use a keyword as a variable name:
if = 10
This gives a SyntaxError.





3. Operators
Definition
Operators are symbols or keywords used to perform operations on values and variables.
Example:
a = 10
b = 5

print(a + b)
Here, + is an operator.
Python has different types of operators.
A. Arithmetic Operators
Used for mathematical calculations.
Operator
Name
Example
Result
+
Addition
10 + 5
15
-
Subtraction
10 - 5
5
*
Multiplication
10 * 5
50
/
Division
10 / 5
2.0
//
Floor Division
10 // 3
3
%
Modulus
10 % 3
1
**
Exponent
2 ** 3
8
Example
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
4. Comparison Operators
Comparison operators compare two values.
The result is always True or False.
Operator
Meaning
==
Equal to
!=
Not equal to
>
Greater than
<
Less than
>=
Greater than or equal to
<=
Less than or equal to
Example
a = 10
b = 5

print(a == b)
print(a > b)
print(a < b)
print(a != b)
Output:
False
True
False
True
Important: = vs ==
= → Assignment operator
x = 10
Means: store 10 in x.
== → Comparison operator
x == 10
Means: check whether x is equal to 10.
5. Assignment Operators
Used to assign or update values.
Operator
Example
Meaning
=
x = 10
Assign
+=
x += 5
x = x + 5
-=
x -= 5
x = x - 5
*=
x *= 5
x = x * 5
/=
x /= 5
x = x / 5
%=
x %= 5
x = x % 5
//=
x //= 5
x = x // 5
**=
x **= 5
x = x ** 5
Example
x = 10
x += 5

print(x)
Output:
15
6. Logical Operators
Logical operators are mainly used to combine conditions.
and
Returns True when both conditions are True.
age = 20

print(age >= 18 and age <= 60)
Output:
True
or
Returns True when at least one condition is True.
age = 20

print(age < 18 or age >= 18)
Output:
True
not
Reverses the result.
x = True

print(not x)
Output:
False
7. Membership Operators
Membership operators check whether a value exists inside a collection such as a string, list, tuple, etc.
in
fruits = ["apple", "banana", "mango"]

print("mango" in fruits)
Output:
True
not in
fruits = ["apple", "banana", "mango"]

print("orange" not in fruits)
Output:
True
8. Identity Operators
Identity operators check whether two variables refer to the same object.
is
a = None

print(a is None)
Output:
True
is not
a = None

print(a is not None)
Output:
False
Remember:
== checks value equality, while is checks object identity.
9. Input Function
Definition
The input() function is used to take data from the user through the keyboard.
Syntax
variable = input("Message")
Example
name = input("Enter your name: ")

print("Hello", name)
If the user enters:
Shivani
Output:
Hello Shivani
Important: input() Always Returns String
By default, input() takes the entered value as a string.
age = input("Enter your age: ")

print(type(age))
If you enter 21, the output is:
<class 'str'>
10. Taking Integer Input
If you want an integer, use int().
age = int(input("Enter your age: "))

print(age)
print(type(age))
Input:
21
Output:
21
<class 'int'>
11. Taking Float Input
Use float() for decimal values.
marks = float(input("Enter your marks: "))

print(marks)
Input:
85.5
Output:
85.5
12. Multiple Inputs
You can take multiple values using multiple input() functions.
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
13. Input + Operators Example
Addition of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Addition:", sum)
Input:
Enter first number: 10
Enter second number: 20
Output:
Addition: 30
14. Simple Calculator Example
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
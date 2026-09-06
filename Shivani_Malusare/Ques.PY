Python Interview Questions & Answers
1. What is a variable in Python?
Answer:
A variable is a name used to store a value in memory.
Example:
name = "Shivani"
age = 21
2. How do you create a variable in Python?
Answer:
We create a variable by assigning a value using the = operator.
Example:
x = 10
name = "Shivani"
3. Do we need to declare the data type of a variable in Python?
Answer:
No. Python automatically identifies the data type of the value.
Example:
x = 10
name = "Shivani"
Here, Python automatically identifies x as an integer and name as a string.
4. What is dynamic typing in Python?
Answer:
Dynamic typing means we don't need to specify the data type of a variable, and the same variable can hold different types of values.
Example:
x = 10
x = "Hello"
5. What are the rules for naming a variable?
Answer:
The main rules are:
It can contain letters, numbers and _.
It cannot start with a number.
It cannot contain spaces.
It cannot be a Python keyword.
Variable names are case-sensitive.
Example:
student_name = "Shivani"   # Valid
age1 = 21                  # Valid
6. What is the difference between a variable and a value?
Answer:
A variable is the name used to store data, while a value is the actual data stored.
Example:
age = 21
Here:
age → Variable
21 → Value
7. Is Python variable case-sensitive?
Answer:
Yes. Python is case-sensitive, so uppercase and lowercase names are different.
Example:
name = "Shivani"
Name = "ABC"

print(name)
print(Name)
They are two different variables.
8. Can we change the value of a variable?
Answer:
Yes. We can change the value of a variable at any time.
Example:
x = 10
x = 20

print(x)
Output:
20
9. Can one variable store different types of values?
Answer:
Yes. Python allows a variable to store different types of values at different times.
Example:
x = 10
x = "Python"
x = 10.5
10. What is multiple variable assignment?
Answer:
Multiple variable assignment means assigning values to multiple variables in one statement.
Example:
a, b, c = 10, 20, 30
Here:
a = 10
b = 20
c = 30
Keywords
11. What are keywords in Python?
Answer:
Keywords are reserved words in Python that have a special meaning.
Example:
if age >= 18:
    print("Adult")
Here, if is a keyword.
12. Why can't we use keywords as variable names?
Answer:
Because keywords already have a special meaning in Python.
Example:
if = 10
This gives a SyntaxError.
13. Give some examples of Python keywords.
Answer:
Some common keywords are:
if, else, elif, for, while
break, continue, def, return
class, import, and, or, not
True, False, None
14. How can you find all Python keywords?
Answer:
We can use the keyword module.
Example:
import keyword

print(keyword.kwlist)
It displays the list of Python keywords.
15. What is the difference between a keyword and a variable?
Answer:
A keyword is a reserved word with a special meaning, while a variable is a name used to store a value.
Example:
age = 20

if age >= 18:
    print("Adult")
Here:
if → Keyword
age → Variable
Operators
16. What are operators in Python?
Answer:
Operators are symbols or keywords used to perform operations on values.
Example:
a = 10
b = 5

print(a + b)
Here, + is an operator.
17. What are the different types of operators in Python?
Answer:
The main types are:
Arithmetic
Assignment
Comparison
Logical
Identity
Membership
Bitwise
18. What are arithmetic operators?
Answer:
Arithmetic operators are used to perform mathematical calculations.
Examples:
+   -   *   /   //   %   **
Example:
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
19. What is the difference between / and //?
Answer:
/ performs normal division and returns a float value.
// performs floor division and returns the floor value.
Example:
print(10 / 3)
print(10 // 3)
Output:
3.3333333333333335
3
20. What is the use of % operator?
Answer:
The % operator returns the remainder of a division.
Example:
print(10 % 3)
Output:
1
Because 10 divided by 3 gives a remainder of 1.
21. What is the use of ** operator?
Answer:
The ** operator is used for exponentiation or power.
Example:
print(2 ** 3)
Output:
8
Because 2 × 2 × 2 = 8.
22. What are comparison operators?
Answer:
Comparison operators are used to compare two values. They return True or False.
Examples:
==   !=   >   <   >=   <=
Example:
a = 10
b = 5

print(a > b)
Output:
True
23. What is the difference between = and ==?
Answer:
= is an assignment operator.
== is a comparison operator.
Example:
x = 10       # Assignment

print(x == 10)   # Comparison
Output:
True
24. What are logical operators?
Answer:
Logical operators are used to combine or reverse conditions.
There are three main logical operators:
and
or
not
Example:
age = 20

print(age >= 18 and age <= 60)
Output:
True
25. Explain and, or, and not.
Answer:
and → Returns True when both conditions are True.
print(10 > 5 and 20 > 10)
Output:
True
or → Returns True when at least one condition is True.
print(10 > 5 or 20 < 10)
Output:
True
not → Reverses the result.
print(not True)
Output:
False
26. What are assignment operators?
Answer:
Assignment operators are used to assign or update values in variables.
Examples:
=   +=   -=   *=   /=   %=   //=   **=
Example:
x = 10
x += 5

print(x)
Output:
15
27. What is the difference between == and is?
Answer:
== checks whether two values are equal.
is checks whether two variables refer to the same object.
Example:
a = [1, 2]
b = a

print(a == b)
print(a is b)
Output:
True
True
28. What are membership operators?
Answer:
Membership operators check whether a value exists in a collection.
The two membership operators are:
in
not in
Example:
fruits = ["apple", "mango"]

print("mango" in fruits)
Output:
True
29. Explain in and not in.
Answer:
in checks whether a value exists in a collection.
not in checks whether a value does not exist.
Example:
fruits = ["apple", "mango"]

print("apple" in fruits)
print("orange" not in fruits)
Output:
True
True
Input
30. What is the use of input() in Python?
Answer:
The input() function is used to take input from the user through the keyboard.
Example:
name = input("Enter your name: ")

print(name)
31. What data type does input() return by default?
Answer:
The input() function always returns a string (str) by default.
Example:
age = input("Enter age: ")

print(type(age))
If we enter 21, output is:
<class 'str'>
32. How do you take an integer input from the user?
Answer:
We use int() with input().
Example:
age = int(input("Enter your age: "))

print(age)
If the user enters 21, it is stored as an integer.
33. How do you take a float input?
Answer:
We use float() with input().
Example:
marks = float(input("Enter your marks: "))

print(marks)
Input:
85.5
34. Why do we use int(input())?
Answer:
We use int(input()) when we want to take an integer from the user.
Because input() returns a string by default, int() converts that string into an integer.
Example:
age = int(input("Enter age: "))
35. What is type conversion?
Answer:
Type conversion means changing one data type into another data type.
Common functions are:
int()
float()
str()
Example:
x = "10"

y = int(x)

print(y)
print(type(y))
Output:
10
<class 'int'>
36. Write a program to take two numbers from the user and add them.
Answer:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a + b

print("Addition:", result)
Input:
Enter first number: 10
Enter second number: 20
Output:
Addition: 30
37. Write a program to take name and age as input and display them.
Answer:
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", name)
print("Age:", age)
Input:
Enter your name: Shivani
Enter your age: 21
Output:
Name: Shivani
Age: 21
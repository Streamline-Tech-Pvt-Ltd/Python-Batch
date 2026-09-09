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

# Python List, Slicing & Binary – Interview Notes

## 1. Binary

### What is Binary?

Binary is a number system that uses only two digits:

* `0`
* `1`

Computers use binary because electronic circuits work with two states: **ON (1)** and **OFF (0)**.

### Bit

A **bit** is the smallest unit of data in a computer. It can store either `0` or `1`.

### Byte

**1 Byte = 8 Bits**

Example:

```text
10101100
```

This contains 8 bits = 1 byte.

### Binary to Decimal Example

Convert `1010` into decimal:

```text
1 × 2³ + 0 × 2² + 1 × 2¹ + 0 × 2⁰

= 8 + 0 + 2 + 0

= 10
```

Therefore:

```text
Binary 1010 = Decimal 10
```

---

# 2. Python List

## What is a List?

A **List** is an ordered and mutable collection used to store multiple values in a single variable.

### Example

```python
numbers = [10, 20, 30, 40]
print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

---

# 3. Properties of Python List

Python Lists have the following properties:

### 1. Ordered

List elements maintain their insertion order.

```python
a = [10, 20, 30]
```

The order remains:

```text
10 → 20 → 30
```

### 2. Mutable

A list can be changed after creation.

```python
a = [10, 20, 30]

a[0] = 100

print(a)
```

Output:

```text
[100, 20, 30]
```

### 3. Allows Duplicate Values

Lists can contain duplicate elements.

```python
a = [10, 20, 10, 30]
```

### 4. Allows Different Data Types

A single list can contain different data types.

```python
a = [10, "Python", 20.5, True]
```

### 5. Indexed

List elements can be accessed using indexes.

```python
a = [10, 20, 30]

print(a[0])
```

Output:

```text
10
```

### 6. Supports Slicing

Lists support slicing.

```python
a = [10, 20, 30, 40, 50]

print(a[1:4])
```

Output:

```text
[20, 30, 40]
```

### 7. Dynamic Size

A list can grow or shrink during program execution.

```python
a = [10, 20]

a.append(30)

print(a)
```

Output:

```text
[10, 20, 30]
```

---

# 4. Python List Methods

## 1. append()

Adds one element at the end of the list.

```python
a = [10, 20]

a.append(30)

print(a)
```

Output:

```text
[10, 20, 30]
```

---

## 2. insert()

Adds an element at a specific index.

```python
a = [10, 20, 30]

a.insert(1, 15)

print(a)
```

Output:

```text
[10, 15, 20, 30]
```

---

## 3. extend()

Adds multiple elements to the list.

```python
a = [10, 20]

a.extend([30, 40])

print(a)
```

Output:

```text
[10, 20, 30, 40]
```

---

## 4. remove()

Removes the first occurrence of a specified value.

```python
a = [10, 20, 30]

a.remove(20)

print(a)
```

Output:

```text
[10, 30]
```

---

## 5. pop()

Removes and returns an element using its index.

```python
a = [10, 20, 30]

a.pop(1)

print(a)
```

Output:

```text
[10, 30]
```

If no index is provided, `pop()` removes the last element.

```python
a.pop()
```

---

## 6. clear()

Removes all elements from the list.

```python
a = [10, 20, 30]

a.clear()

print(a)
```

Output:

```text
[]
```

---

## 7. index()

Returns the index of the first occurrence of a value.

```python
a = [10, 20, 30]

print(a.index(20))
```

Output:

```text
1
```

---

## 8. count()

Returns the number of occurrences of a value.

```python
a = [10, 20, 10, 30, 10]

print(a.count(10))
```

Output:

```text
3
```

---

## 9. sort()

Sorts the list.

```python
a = [30, 10, 20]

a.sort()

print(a)
```

Output:

```text
[10, 20, 30]
```

Descending order:

```python
a.sort(reverse=True)
```

Output:

```text
[30, 20, 10]
```

---

## 10. reverse()

Reverses the current order of elements.

```python
a = [10, 30, 20]

a.reverse()

print(a)
```

Output:

```text
[20, 30, 10]
```

> **Important:** `reverse()` does not sort the list. It only reverses the existing order.

---

## 11. copy()

Creates a copy of the list.

```python
a = [10, 20, 30]

b = a.copy()

print(b)
```

Output:

```text
[10, 20, 30]
```

---

# 5. Python List Slicing

## Slicing Syntax

```python
list[start : stop : step]
```

Example:

```python
a = [10, 20, 30, 40, 50]
```

### Important Rule

**Start index is included, but stop index is excluded.**

---

## Example 1: `a[1:4]`

```python
a = [10, 20, 30, 40, 50]

print(a[1:4])
```

Output:

```text
[20, 30, 40]
```

---

## Example 2: `a[:3]`

```python
print(a[:3])
```

Output:

```text
[10, 20, 30]
```

It starts from the beginning.

---

## Example 3: `a[2:]`

```python
print(a[2:])
```

Output:

```text
[30, 40, 50]
```

It continues from index `2` to the end.

---

## Example 4: `a[::2]`

```python
print(a[::2])
```

Output:

```text
[10, 30, 50]
```

It takes every second element.

---

## Example 5: Reverse a List

```python
print(a[::-1])
```

Output:

```text
[50, 40, 30, 20, 10]
```

---

# 6. Negative Indexing

Python supports negative indexes.

```python
a = [10, 20, 30, 40, 50]
```

Index positions:

```text
Positive:   0    1    2    3    4
Values:    10   20   30   40   50
Negative:  -5   -4   -3   -2   -1
```

Example:

```python
print(a[-1])
```

Output:

```text
50
```

---

# 7. Important Interview Questions

## Q1. Is Python List mutable?

**Answer:** Yes, Python List is mutable.

```python
a = [10, 20, 30]

a[0] = 100

print(a)
```

Output:

```text
[100, 20, 30]
```

---

## Q2. Can a List contain duplicate values?

**Answer:** Yes.

```python
a = [10, 20, 10, 30]
```

---

## Q3. Can a List contain different data types?

**Answer:** Yes.

```python
a = [10, "Python", 20.5, True]
```

---

## Q4. What is the difference between `append()` and `extend()`?

### append()

Adds the complete object as one element.

```python
a = [1, 2]

a.append([3, 4])

print(a)
```

Output:

```text
[1, 2, [3, 4]]
```

### extend()

Adds elements individually.

```python
a = [1, 2]

a.extend([3, 4])

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

---

## Q5. Difference between `remove()` and `pop()`?

| Method     | Removes using |
| ---------- | ------------- |
| `remove()` | Value         |
| `pop()`    | Index         |

Example:

```python
a.remove(20)
```

Removes value `20`.

```python
a.pop(1)
```

Removes element at index `1`.

---

## Q6. Difference between `sort()` and `reverse()`?

### sort()

Arranges elements in ascending or descending order.

```python
a = [30, 10, 20]

a.sort()

print(a)
```

Output:

```text
[10, 20, 30]
```

### reverse()

Reverses the existing order.

```python
a = [30, 10, 20]

a.reverse()

print(a)
```

Output:

```text
[20, 10, 30]
```

---

# 8. Tricky Interview Questions

### Question 1

What is the output?

```python
a = [1, 2, 3, 4, 5]

print(a[-1])
```

**Answer:**

```text
5
```

---

### Question 2

What is the output?

```python
a = [1, 2, 3, 4, 5]

print(a[-3:])
```

**Answer:**

```text
[3, 4, 5]
```

---

### Question 3

What is the output?

```python
a = [1, 2, 3, 4, 5]

print(a[::-1])
```

**Answer:**

```text
[5, 4, 3, 2, 1]
```

---

### Question 4

What is the output?

```python
a = [10, 20, 30, 40, 50]

print(a[1:5:2])
```

**Answer:**

```text
[20, 40]
```

---

# Quick Revision

| Topic                | Important Point        |
| -------------------- | ---------------------- |
| List                 | Ordered and mutable    |
| Duplicate            | Allowed                |
| Different data types | Allowed                |
| Indexing             | Starts from `0`        |
| Negative indexing    | Starts from `-1`       |
| Slicing              | `[start:stop:step]`    |
| append()             | Adds one object        |
| extend()             | Adds multiple elements |
| insert()             | Adds at specific index |
| remove()             | Removes by value       |
| pop()                | Removes by index       |
| clear()              | Removes all elements   |
| count()              | Counts occurrences     |
| index()              | Returns index          |
| sort()               | Sorts elements         |
| reverse()            | Reverses current order |
| copy()               | Creates a copy         |
| Binary               | Uses `0` and `1`       |
| 1 Byte               | 8 bits                 |

## Interview Tip

Remember these four differences:

```text
append()  → One object
extend()  → Multiple elements
remove()  → Value
pop()     → Index
```

And:

```text
sort()    → Sorts
reverse() → Reverses
```
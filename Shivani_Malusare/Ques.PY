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

# 🐍 Python Interview Questions & Answers

## 📚 Topics Covered

* List Properties
* List Slicing
* String
* String Methods
* Dictionary
* Tuple
* Set
* `if`, `elif`, `else`

---

# 1. List Interview Questions

### Q1. What is a List in Python?

**Answer:**

A list is an ordered and mutable collection of elements in Python. It is used to store multiple values in a single variable.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

**Output:**

```text
['Apple', 'Banana', 'Mango']
```

---

### Q2. What are the properties of a List?

**Answer:**

The main properties of a list are:

1. List is ordered.
2. List is mutable.
3. List allows duplicate values.
4. List supports indexing.
5. List supports slicing.
6. List can contain different data types.
7. List can contain another list.

```python
data = [10, "Python", 20.5, True, 10]

print(data)
```

---

### Q3. Is a List mutable or immutable?

**Answer:**

A list is **mutable**, which means we can change, add, or remove elements after creating the list.

```python
numbers = [10, 20, 30]

numbers[1] = 50

print(numbers)
```

**Output:**

```text
[10, 50, 30]
```

---

### Q4. Does a List allow duplicate values?

**Answer:**

Yes, a list allows duplicate values.

```python
numbers = [10, 20, 10, 30, 20]

print(numbers)
```

**Output:**

```text
[10, 20, 10, 30, 20]
```

---

### Q5. What is List indexing?

**Answer:**

Indexing is used to access individual elements from a list.

Python uses **zero-based indexing**, so the first element has index `0`.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[2])
```

**Output:**

```text
Apple
Mango
```

---

# 2. List Slicing Interview Questions

### Q6. What is slicing in Python?

**Answer:**

Slicing is used to extract a specific portion of a sequence such as a list, tuple, or string.

### Syntax

```python
sequence[start:stop:step]
```

The `stop` index is not included.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

**Output:**

```text
[20, 30, 40]
```

---

### Q7. What is the difference between indexing and slicing?

**Answer:**

**Indexing** accesses a single element, while **slicing** accesses multiple elements.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[2])      # Indexing
print(numbers[1:4])    # Slicing
```

**Output:**

```text
30
[20, 30, 40]
```

---

### Q8. How do you reverse a list using slicing?

**Answer:**

We can use `[::-1]` to reverse a list.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])
```

**Output:**

```text
[50, 40, 30, 20, 10]
```

---

# 3. String Interview Questions

### Q9. What is a String in Python?

**Answer:**

A string is a sequence of characters enclosed inside single quotes, double quotes, or triple quotes.

```python
name = "Shivani"

print(name)
```

---

### Q10. Is a String mutable or immutable?

**Answer:**

A string is **immutable**. This means we cannot directly change an existing character in a string.

```python
text = "Python"

# text[0] = "J"   # TypeError
```

Instead, we create a new string.

```python
text = "Jython"
```

---

### Q11. Does a String support indexing and slicing?

**Answer:**

Yes. Strings support both indexing and slicing.

```python
text = "Python"

print(text[0])
print(text[1:4])
```

**Output:**

```text
P
yth
```

---

### Q12. What is negative indexing?

**Answer:**

Negative indexing is used to access elements from the end of a sequence.

```python
text = "Python"

print(text[-1])
print(text[-2])
```

**Output:**

```text
n
o
```

---

# 4. String Methods Interview Questions

### Q13. What is `upper()`?

**Answer:**

`upper()` converts all characters of a string into uppercase.

```python
text = "python"

print(text.upper())
```

**Output:**

```text
PYTHON
```

---

### Q14. What is `lower()`?

**Answer:**

`lower()` converts all characters of a string into lowercase.

```python
text = "PYTHON"

print(text.lower())
```

**Output:**

```text
python
```

---

### Q15. What is `capitalize()`?

**Answer:**

`capitalize()` converts the first character of a string to uppercase and the remaining characters to lowercase.

```python
text = "python programming"

print(text.capitalize())
```

**Output:**

```text
Python programming
```

---

### Q16. What is `title()`?

**Answer:**

`title()` converts the first character of each word into uppercase.

```python
text = "python programming language"

print(text.title())
```

**Output:**

```text
Python Programming Language
```

---

### Q17. What is `strip()`?

**Answer:**

`strip()` removes leading and trailing whitespace from a string.

```python
text = "  Python  "

print(text.strip())
```

**Output:**

```text
Python
```

---

### Q18. What is `replace()`?

**Answer:**

`replace()` is used to replace one substring with another substring.

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

**Output:**

```text
I like Python
```

---

### Q19. What is `split()`?

**Answer:**

`split()` divides a string into a list.

```python
text = "Python SQL Java"

print(text.split())
```

**Output:**

```text
['Python', 'SQL', 'Java']
```

---

### Q20. What is `join()`?

**Answer:**

`join()` combines multiple strings into a single string using a specified separator.

```python
courses = ["Python", "SQL", "Java"]

print(" - ".join(courses))
```

**Output:**

```text
Python - SQL - Java
```

---

### Q21. What is `find()`?

**Answer:**

`find()` returns the index of the first occurrence of a specified substring. If the substring is not found, it returns `-1`.

```python
text = "Python Programming"

print(text.find("Python"))
```

**Output:**

```text
0
```

---

### Q22. What is `count()`?

**Answer:**

`count()` returns the number of times a specified substring occurs in a string.

```python
text = "banana"

print(text.count("a"))
```

**Output:**

```text
3
```

---

### Q23. What is the difference between `isalpha()` and `isdigit()`?

**Answer:**

* `isalpha()` checks whether all characters are alphabets.
* `isdigit()` checks whether all characters are digits.

```python
print("Python".isalpha())
print("12345".isdigit())
```

**Output:**

```text
True
True
```

---

# 5. Dictionary Interview Questions

### Q24. What is a Dictionary in Python?

**Answer:**

A dictionary is a mutable collection that stores data in **key-value pairs**.

```python
student = {
    "name": "Shivani",
    "age": 21,
    "course": "Python"
}

print(student)
```

---

### Q25. What are the properties of a Dictionary?

**Answer:**

1. Dictionary stores key-value pairs.
2. Dictionary is mutable.
3. Keys must be unique.
4. Duplicate values are allowed.
5. Dictionary is accessed using keys.
6. Dictionary can contain different data types.
7. Dictionary can contain nested dictionaries.

---

### Q26. Are duplicate keys allowed in a Dictionary?

**Answer:**

No. Dictionary keys must be unique.

If the same key is used more than once, the latest value replaces the previous value.

```python
student = {
    "name": "Shivani",
    "name": "Sneha"
}

print(student)
```

**Output:**

```text
{'name': 'Sneha'}
```

---

### Q27. Are duplicate values allowed in a Dictionary?

**Answer:**

Yes. Duplicate values are allowed.

```python
student = {
    "math": 90,
    "python": 90
}

print(student)
```

---

### Q28. How do you access a Dictionary value?

**Answer:**

We can access a value using its key.

```python
student = {
    "name": "Shivani",
    "age": 21
}

print(student["name"])
```

**Output:**

```text
Shivani
```

---

### Q29. What is the use of `get()`?

**Answer:**

`get()` is used to retrieve the value associated with a key.

```python
student = {
    "name": "Shivani",
    "age": 21
}

print(student.get("name"))
```

**Output:**

```text
Shivani
```

---

### Q30. What are common Dictionary methods?

**Answer:**

Common dictionary methods include:

```text
keys()
values()
items()
get()
update()
pop()
popitem()
copy()
clear()
```

Example:

```python
student = {
    "name": "Shivani",
    "age": 21
}

print(student.keys())
print(student.values())
print(student.items())
```

---

# 6. Tuple Interview Questions

### Q31. What is a Tuple in Python?

**Answer:**

A tuple is an ordered and immutable collection of elements.

Tuples are generally written using parentheses `()`.

```python
student = ("Shivani", 21, "Python")

print(student)
```

---

### Q32. Is a Tuple mutable or immutable?

**Answer:**

A tuple is **immutable**, which means its elements cannot be changed after creation.

```python
numbers = (10, 20, 30)

# numbers[0] = 50   # TypeError
```

---

### Q33. Does a Tuple allow duplicate values?

**Answer:**

Yes. A tuple allows duplicate values.

```python
numbers = (10, 20, 10, 30)

print(numbers)
```

---

### Q34. What are the main Tuple methods?

**Answer:**

Tuple has two main methods:

* `count()`
* `index()`

```python
numbers = (10, 20, 10, 30)

print(numbers.count(10))
print(numbers.index(20))
```

---

### Q35. What is Tuple packing?

**Answer:**

Tuple packing means putting multiple values into a single tuple.

```python
student = "Shivani", 21, "Python"

print(student)
```

---

### Q36. What is Tuple unpacking?

**Answer:**

Tuple unpacking means assigning tuple elements to separate variables.

```python
student = ("Shivani", 21, "Python")

name, age, course = student

print(name)
print(age)
print(course)
```

---

# 7. Set Interview Questions

### Q37. What is a Set in Python?

**Answer:**

A set is an unordered and mutable collection of unique elements.

```python
numbers = {10, 20, 30}

print(numbers)
```

---

### Q38. Does a Set allow duplicate values?

**Answer:**

No. A set automatically removes duplicate values.

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

**Output:**

```text
{10, 20, 30}
```

---

### Q39. Does a Set support indexing?

**Answer:**

No. A set does not support indexing because it is unordered.

```python
numbers = {10, 20, 30}

# print(numbers[0])   # TypeError
```

---

### Q40. What is the use of `add()`?

**Answer:**

`add()` is used to add one element to a set.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

---

### Q41. What is the difference between `remove()` and `discard()`?

**Answer:**

Both methods remove an element from a set.

* `remove()` raises an error if the element does not exist.
* `discard()` does not raise an error if the element does not exist.

```python
numbers = {10, 20, 30}

numbers.remove(20)
numbers.discard(100)
```

---

### Q42. What is Set Union?

**Answer:**

Union combines all unique elements from two sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

**Output:**

```text
{1, 2, 3, 4, 5}
```

---

### Q43. What is Set Intersection?

**Answer:**

Intersection returns the common elements from two sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)
```

**Output:**

```text
{3}
```

---

# 8. if, elif, else Interview Questions

### Q44. What is a Conditional Statement?

**Answer:**

A conditional statement is used to execute different blocks of code based on whether a condition is `True` or `False`.

Python provides:

```text
if
elif
else
```

---

### Q45. What is the use of `if`?

**Answer:**

`if` is used to execute a block of code when a condition is true.

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

### Q46. What is the use of `else`?

**Answer:**

`else` executes when the `if` condition is false.

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

### Q47. What is the use of `elif`?

**Answer:**

`elif` means **else if**. It is used to check another condition when the previous condition is false.

```python
marks = 75

if marks >= 90:
    print("A+")
elif marks >= 75:
    print("A")
else:
    print("B")
```

**Output:**

```text
A
```

---

### Q48. Is `else` compulsory with `if`?

**Answer:**

No. The `else` block is optional.

```python
age = 20

if age >= 18:
    print("Eligible")
```

---

### Q49. Can we use multiple `elif` statements?

**Answer:**

Yes. We can use multiple `elif` statements.

```python
marks = 65

if marks >= 90:
    print("A+")
elif marks >= 75:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("Fail")
```

---

### Q50. What is Nested `if`?

**Answer:**

An `if` statement inside another `if` statement is called a **nested if**.

```python
age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```

---

# ⭐ Most Important Comparison Questions

## Q51. Difference between List and Tuple?

| List              | Tuple             |
| ----------------- | ----------------- |
| Mutable           | Immutable         |
| Uses `[]`         | Uses `()`         |
| Can be changed    | Cannot be changed |
| Supports indexing | Supports indexing |
| Supports slicing  | Supports slicing  |

---

## Q52. Difference between List and Set?

| List              | Set                       |
| ----------------- | ------------------------- |
| Ordered           | Unordered                 |
| Allows duplicates | Does not allow duplicates |
| Supports indexing | Does not support indexing |
| Mutable           | Mutable                   |
| Uses `[]`         | Uses `{}`                 |

---

## Q53. Difference between Tuple and Set?

| Tuple             | Set           |
| ----------------- | ------------- |
| Ordered           | Unordered     |
| Immutable         | Mutable       |
| Allows duplicates | No duplicates |
| Supports indexing | No indexing   |
| Uses `()`         | Uses `{}`     |

---

## Q54. Difference between String and List?

| String                 | List                   |
| ---------------------- | ---------------------- |
| Sequence of characters | Collection of elements |
| Immutable              | Mutable                |
| Uses quotes            | Uses `[]`              |
| Supports indexing      | Supports indexing      |
| Supports slicing       | Supports slicing       |

---

# 🔥 Quick Interview Revision

| Topic      | Key Point                          |
| ---------- | ---------------------------------- |
| List       | Ordered + Mutable + Duplicates     |
| Tuple      | Ordered + Immutable + Duplicates   |
| Set        | Unordered + Unique                 |
| Dictionary | Key-Value pairs                    |
| String     | Immutable sequence of characters   |
| Indexing   | Access single element              |
| Slicing    | Access multiple elements           |
| `if`       | Checks a condition                 |
| `elif`     | Checks another condition           |
| `else`     | Executes when conditions are false |

---

#  One-Line Interview Answers

**List:** A list is an ordered and mutable collection that allows duplicate values.

**Tuple:** A tuple is an ordered and immutable collection that allows duplicate values.

**Set:** A set is an unordered collection of unique elements.

**Dictionary:** A dictionary is a mutable collection of key-value pairs with unique keys.

**String:** A string is an immutable sequence of characters.

**Slicing:** Slicing is used to extract a portion of a sequence using `start:stop:step`.

**if:** `if` executes code when a condition is true.

**elif:** `elif` checks another condition when the previous condition is false.

**else:** `else` executes when all preceding conditions are false.

---

# 1. Nested `if`

## Definition

A **nested `if`** is an `if` statement written inside another `if` statement.

## Syntax

```python
if condition1:
    if condition2:
        statement
```

## Example

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
```

## Interview Answer

> A nested if is an if statement inside another if statement. It is used to check dependent conditions.

---

# 2. Loops

## Definition

A **loop** is used to execute a block of code repeatedly.

## Types of Loops in Python

1. `for` loop
2. `while` loop

---

# 3. `for` Loop

## Definition

A `for` loop is used to iterate over a sequence or a range of values.

## Syntax

```python
for variable in sequence:
    statement
```

## Example

```python
for i in range(1, 6):
    print(i)
```

### Output

```text
1
2
3
4
5
```

## `range()` Function

### Syntax

```python
range(start, stop, step)
```

### Example

```python
for i in range(2, 11, 2):
    print(i)
```

### Output

```text
2
4
6
8
10
```

### Important

The `stop` value is not included.

```python
range(1, 6)
```

gives:

```text
1 2 3 4 5
```

## Interview Answer

> A for loop is used to iterate over a sequence or range of values.

---

# 4. `while` Loop

## Definition

A `while` loop executes a block of code as long as the given condition is `True`.

## Syntax

```python
while condition:
    statement
```

## Example

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

### Output

```text
1
2
3
4
5
```

## Important

The variable should be updated inside the loop.

```python
i += 1
```

Otherwise, the loop may become an **infinite loop**.

## Interview Answer

> A while loop repeatedly executes a block of code as long as the given condition is true.

---

# 5. `for` Loop vs `while` Loop

| `for` Loop                               | `while` Loop                                     |
| ---------------------------------------- | ------------------------------------------------ |
| Used to iterate over a sequence or range | Used based on a condition                        |
| Generally used when iteration is known   | Generally used when condition controls iteration |
| Uses `for` keyword                       | Uses `while` keyword                             |
| Example: `for i in range(5)`             | Example: `while i < 5`                           |

## Interview Answer

> We generally use a for loop when iterating over a sequence or known range, and a while loop when execution depends on a condition.

---

# 6. Reverse a Number

## Definition

Reversing a number means arranging its digits from last to first.

### Example

```text
Input  : 12345
Output : 54321
```

## Program

```python
num = 12345
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)
```

### Output

```text
54321
```

## Logic

```text
% 10  → Gets the last digit
// 10 → Removes the last digit
```

### Example

```text
12345 % 10 = 5
1234  % 10 = 4
123   % 10 = 3
12    % 10 = 2
1     % 10 = 1
```

## Interview Answer

> To reverse a number, I extract the last digit using `% 10` and remove the last digit using `// 10`.

---

# 7. Reverse a String

## Example

```python
text = "python"

reverse = text[::-1]

print(reverse)
```

### Output

```text
nohtyp
```

## String Slicing

```python
string[start:stop:step]
```

For:

```python
text[::-1]
```

the step is `-1`, so the string is read from right to left.

## Interview Answer

> We can reverse a string using slicing with a step of `-1`.

---

# 8. Factorial Number

## Definition

The **factorial of a number `n`** is the product of all positive integers from `1` to `n`.

## Formula

```text
n! = n × (n-1) × (n-2) × ... × 1
```

### Example

```text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

### Special Case

```text
0! = 1
```

---

## Factorial Using `for` Loop

```python
num = 5
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(fact)
```

### Output

```text
120
```

---

## Factorial Using `while` Loop

```python
num = 5
fact = 1
i = 1

while i <= num:
    fact = fact * i
    i += 1

print(fact)
```

### Output

```text
120
```

## Why `fact = 1`?

Factorial uses multiplication.

If we write:

```python
fact = 0
```

then:

```text
0 × any number = 0
```

So the result will always be `0`.

## Interview Answer

> Factorial is the product of all positive integers from 1 to a given number. For example, 5 factorial is 120.

---

# 9. Loop Control Statements

Loop control statements change the normal execution of a loop.

## Types

1. `break`
2. `continue`
3. `pass`

---

# 10. `break`

## Definition

`break` is used to immediately terminate the loop.

## Example

```python
for i in range(1, 10):

    if i == 5:
        break

    print(i)
```

### Output

```text
1
2
3
4
```

When `i` becomes `5`, the loop stops.

## Interview Answer

> Break is used to immediately terminate the loop.

---

# 11. `continue`

## Definition

`continue` skips the current iteration and moves to the next iteration.

## Example

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

### Output

```text
1
2
4
5
```

Here, `3` is skipped.

## Interview Answer

> Continue skips the current iteration and moves to the next iteration.

---

# 12. `pass`

## Definition

`pass` is a null statement. It does nothing.

## Example

```python
for i in range(5):
    pass
```

## Use

`pass` is mainly used as a **placeholder** when code will be written later.

## Interview Answer

> Pass is a null statement used as a placeholder. It does nothing when executed.

---

# 13. `break` vs `continue` vs `pass`

| Statement  | Meaning                     |
| ---------- | --------------------------- |
| `break`    | Stops the complete loop     |
| `continue` | Skips the current iteration |
| `pass`     | Does nothing                |

### Easy Memory Trick

```text
break     → STOP
continue  → SKIP
pass      → DO NOTHING
```

---

# 14. Function

## Definition

A **function** is a reusable block of code designed to perform a specific task.

## Syntax

```python
def function_name():
    statement
```

## Example

```python
def greet():
    print("Hello")

greet()
```

### Output

```text
Hello
```

## Advantages of Functions

* Code reusability
* Avoids code repetition
* Easy debugging
* Better code organization
* Improves readability

## Interview Answer

> A function is a reusable block of code that performs a specific task.

---

# 15. Function with Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

### Output

```text
30
```

Here:

```text
a, b   → Parameters
10, 20 → Arguments
```

---

# 16. Parameter vs Argument

## Parameter

A parameter is a variable defined in the function definition.

```python
def add(a, b):
    print(a + b)
```

Here:

```text
a and b → Parameters
```

## Argument

An argument is the actual value passed during the function call.

```python
add(10, 20)
```

Here:

```text
10 and 20 → Arguments
```

## Interview Answer

> A parameter is a variable defined in the function definition, while an argument is the actual value passed during the function call.

---

# 17. Five Types of Function Arguments

Python commonly has five types of function arguments:

1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-Length Positional Arguments
5. Variable-Length Keyword Arguments

---

# 18. Positional Arguments

## Definition

Arguments are passed according to the position of parameters.

## Example

```python
def student(name, age):
    print(name)
    print(age)

student("Shivani", 22)
```

Here:

```text
name = Shivani
age  = 22
```

The position matters.

## Interview Answer

> Positional arguments are passed according to the position of the parameters.

---

# 19. Keyword Arguments

## Definition

Arguments are passed using parameter names.

## Example

```python
def student(name, age):
    print(name)
    print(age)

student(age=22, name="Shivani")
```

The order does not matter because parameter names are specified.

## Interview Answer

> Keyword arguments are passed using parameter names.

---

# 20. Default Arguments

## Definition

A default argument has a predefined value.

## Example

```python
def student(name, city="Pune"):
    print(name)
    print(city)

student("Shivani")
```

### Output

```text
Shivani
Pune
```

If we provide a value:

```python
student("Shivani", "Mumbai")
```

### Output

```text
Shivani
Mumbai
```

## Interview Answer

> A default argument has a predefined value that is used when the caller does not provide a value.

---

# 21. Variable-Length Positional Arguments — `*args`

## Definition

`*args` allows a function to accept any number of positional arguments.

## Example

```python
def add(*numbers):
    total = 0

    for i in numbers:
        total = total + i

    return total

print(add(10, 20, 30, 40))
```

### Output

```text
100
```

## Important

```text
*args → Tuple
```

## Interview Answer

> `*args` allows a function to accept multiple positional arguments. These arguments are stored as a tuple.

---

# 22. Variable-Length Keyword Arguments — `**kwargs`

## Definition

`**kwargs` allows a function to accept any number of keyword arguments.

## Example

```python
def student(**details):
    print(details)

student(name="Shivani", age=22, city="Pune")
```

### Output

```text
{'name': 'Shivani', 'age': 22, 'city': 'Pune'}
```

## Important

```text
**kwargs → Dictionary
```

## Interview Answer

> `**kwargs` allows a function to accept multiple keyword arguments. These arguments are stored as a dictionary.

---

# 23. `*args` vs `**kwargs`

| `*args`                       | `**kwargs`                 |
| ----------------------------- | -------------------------- |
| Multiple positional arguments | Multiple keyword arguments |
| Stored as tuple               | Stored as dictionary       |
| Uses `*`                      | Uses `**`                  |

### Example

```python
def fun(*args):
    print(args)

fun(10, 20, 30)
```

```python
def fun(**kwargs):
    print(kwargs)

fun(name="Shivani", age=22)
```

---

# 24. Python Function Types

## 24.1 Built-in Functions

Built-in functions are functions already provided by Python.

### Examples

```python
print()
len()
type()
sum()
max()
min()
```

### Example

```python
numbers = [10, 20, 30]

print(len(numbers))
```

---

# 25. User-Defined Functions

A user-defined function is created by the programmer using `def`.

## Example

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

### Interview Answer

> A user-defined function is a function created by the programmer to perform a specific task.

---

# 26. Lambda Function

## Definition

A lambda function is a small anonymous function created using the `lambda` keyword.

## Syntax

```python
lambda arguments: expression
```

## Example

```python
square = lambda x: x * x

print(square(5))
```

### Output

```text
25
```

## Interview Answer

> A lambda function is a small anonymous function written using the `lambda` keyword.

---

# 27. Recursive Function

## Definition

A recursive function is a function that calls itself.

## Example

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

### Output

```text
120
```

## Important

A recursive function must have a **base condition** to stop recursion.

```python
if n == 0:
    return 1
```

## Interview Answer

> A recursive function is a function that calls itself until a base condition is reached.

---

# 28. Higher-Order Function

## Definition

A higher-order function is a function that takes another function as an argument or returns another function.

## Example

```python
def add(a, b):
    return a + b

def calculate(fun, a, b):
    return fun(a, b)

result = calculate(add, 10, 20)

print(result)
```

### Output

```text
30
```

Here:

```text
add       → Function passed as argument
calculate → Higher-order function
```

## Interview Answer

> A higher-order function is a function that accepts another function as an argument or returns another function.

---

# 29. Function Types Based on Arguments and Return Value

There are four common categories.

## 1. No Argument and No Return Value

```python
def greet():
    print("Hello")

greet()
```

---

## 2. Argument and No Return Value

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

---

## 3. No Argument and With Return Value

```python
def number():
    return 10

x = number()

print(x)
```

---

## 4. Argument and With Return Value

```python
def add(a, b):
    return a + b

x = add(10, 20)

print(x)
```

### Output

```text
30
```

---

# 30. `return` Statement

## Definition

`return` is used to send a value from a function back to the caller.

## Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

### Output

```text
30
```

## `print()` vs `return`

| `print()`                                                | `return`                                   |
| -------------------------------------------------------- | ------------------------------------------ |
| Displays the result                                      | Sends the result back                      |
| Used for output                                          | Used to return a value                     |
| Cannot normally be used by caller as the returned result | Returned value can be stored in a variable |

---


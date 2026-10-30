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


Python List

A List in Python is a collection of multiple values stored in a single variable.

Features of List

- Ordered
- Mutable (Changeable)
- Allows duplicate values
- Can store different data types
- Supports indexing and slicing

Syntax

my_list = [10, 20, 30, 40]

Example

student = ["Shivu", 21, "BE IT", 85.5]

print(student)

Output:

['Shivu', 21, 'BE IT', 85.5]

---

List Indexing

Indexing means accessing a particular element from a list using its position.

Python indexing starts from 0.

fruits = ["Apple", "Mango", "Banana", "Orange"]

Element| Index
Apple| 0
Mango| 1
Banana| 2
Orange| 3

Example

print(fruits[0])
print(fruits[2])

Output:

Apple
Banana

Negative Indexing

Negative indexing starts from the last element.

Element| Negative Index
Apple| -4
Mango| -3
Banana| -2
Orange| -1

Example

print(fruits[-1])

Output:

Orange

---

List Slicing

Slicing means extracting a part of a list.

Syntax

list[start:stop]

«The "stop" index is not included.»

Example

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

print(fruits[1:4])

Output:

['Mango', 'Banana', 'Orange']

More Examples

print(fruits[:3])

Output:

['Apple', 'Mango', 'Banana']

print(fruits[2:])

Output:

['Banana', 'Orange', 'Grapes']

print(fruits[:])

Output:

['Apple', 'Mango', 'Banana', 'Orange', 'Grapes']

Step Slicing

Syntax

list[start:stop:step]

Example

print(fruits[0:5:2])

Output:

['Apple', 'Banana', 'Grapes']

---

List Methods

List methods are built-in methods used to perform different operations on a list.

1. append()

Adds an element at the end of the list.

fruits.append("Kiwi")

print(fruits)

---

2. insert()

Adds an element at a specific index.

Syntax

list.insert(index, value)

Example

fruits.insert(1, "Pineapple")

print(fruits)

---

3. remove()

Removes a specific value from the list.

fruits.remove("Banana")

print(fruits)

---

4. pop()

Removes an element using its index.

fruits.pop(2)

print(fruits)

If no index is given, it removes the last element.

fruits.pop()

---

5. clear()

Removes all elements from the list.

fruits.clear()

print(fruits)

Output:

[]

---

6. index()

Returns the index of a specific value.

fruits = ["Apple", "Mango", "Banana"]

print(fruits.index("Mango"))

Output:

1

---

7. count()

Returns the number of times a value occurs.

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

Output:

3

---

8. sort()

Sorts the list in ascending order.

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

Output:

[10, 20, 30, 40]

---

9. reverse()

Reverses the order of elements.

numbers.reverse()

print(numbers)

---

10. copy()

Creates a copy of the list.

new_list = numbers.copy()

print(new_list)

---

11. extend()

Adds elements from another list.

a = [1, 2]
b = [3, 4]

a.extend(b)

print(a)

Output:

[1, 2, 3, 4]

---

Important List Methods

Method| Description
"append()"| Adds element at the end
"insert()"| Adds element at specific index
"remove()"| Removes a specific value
"pop()"| Removes element by index
"clear()"| Removes all elements
"index()"| Returns index of a value
"count()"| Counts occurrences
"sort()"| Sorts the list
"reverse()"| Reverses the list
"copy()"| Creates a copy
"extend()"| Adds another list

---

Quick Example

fruits = ["Apple", "Mango", "Banana", "Orange"]

# Indexing
print(fruits[0])

# Slicing
print(fruits[1:3])

# Add element
fruits.append("Grapes")

# Remove element
fruits.remove("Banana")

# Reverse
fruits.reverse()

print(fruits)

Python: String, Dictionary and Tuple

1. String

Definition

A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.

Example

name = "Shivani"
city = 'Pune'
message = "India is my country"

print(name)
print(city)
print(message)

String Indexing

Each character in a string has an index number.

name = "Python"

print(name[0])   # P
print(name[3])   # h
print(name[-1])  # n

String Slicing

Slicing is used to extract a part of a string.

Syntax

string[start:end]

The "end" index is not included.

name = "Python"

print(name[0:3])
print(name[2:5])

Output:

Pyt
tho

---

2. String Methods

"upper()"

Converts all characters to uppercase.

name = "shivani"
print(name.upper())

Output:

SHIVANI

---

"lower()"

Converts all characters to lowercase.

name = "SHIVANI"
print(name.lower())

Output:

shivani

---

"capitalize()"

Converts the first character to uppercase.

name = "shivani"
print(name.capitalize())

Output:

Shivani

---

"title()"

Converts the first character of every word to uppercase.

text = "india is my country"
print(text.title())

Output:

India Is My Country

---

"istitle()"

Checks whether the string is in title case.

Returns "True" or "False".

text = "India Is My Country"
print(text.istitle())

Output:

True

---

"isalpha()"

Checks whether the string contains only alphabetic characters.

a = "Python"
b = "Python123"

print(a.isalpha())
print(b.isalpha())

Output:

True
False

«Numbers, spaces, and special characters make "isalpha()" return "False".»

---

"isdigit()"

Checks whether the string contains only digits.

number = "12345"

print(number.isdigit())

Output:

True

---

"isalnum()"

Checks whether the string contains only alphabets and numbers.

a = "Python123"
b = "Python@123"

print(a.isalnum())
print(b.isalnum())

Output:

True
False

«Special characters and spaces make "isalnum()" return "False".»

---

"isspace()"

Checks whether the string contains only whitespace characters.

text = "   "

print(text.isspace())

Output:

True

---

"startswith()"

Checks whether a string starts with a specified value.

text = "Python Programming"

print(text.startswith("Python"))

Output:

True

---

"endswith()"

Checks whether a string ends with a specified value.

text = "Python Programming"

print(text.endswith("Programming"))

Output:

True

---

"find()"

Returns the index of the first occurrence of a specified value.

text = "Python"

print(text.find("t"))

Output:

2

---

"replace()"

Replaces one value with another value.

text = "I like Java"

print(text.replace("Java", "Python"))

Output:

I like Python

---

"strip()"

Removes spaces from the beginning and end of a string.

name = "   Shivani   "

print(name.strip())

Output:

Shivani

---

"split()"

Splits a string into a list.

text = "India is my country"

print(text.split())

Output:

['India', 'is', 'my', 'country']

---

"join()"

Joins multiple strings into one string.

words = ("India", "is", "great")

print(" ".join(words))

Output:

India is great

---

"zfill()"

Adds zeros to the left side of a string.

number = "25"

print(number.zfill(5))

Output:

00025

---

"center()"

Places a string in the center of a specified width.

text = "Python"

print(text.center(10))

---

3. Dictionary

Definition

A dictionary is a collection of key-value pairs.

Dictionary stores data in:

key : value

Syntax

dictionary = {
    "key": "value"
}

Example

student = {
    "name": "Shivani",
    "age": 21,
    "course": "IT"
}

print(student)

Output:

{'name': 'Shivani', 'age': 21, 'course': 'IT'}

Here:

name     -> key
Shivani  -> value

age      -> key
21       -> value

---

4. Access Dictionary Values

student = {
    "name": "Shivani",
    "age": 21,
    "course": "IT"
}

print(student["name"])
print(student["age"])

Output:

Shivani
21

---

5. Dictionary Methods

"keys()"

Returns all keys.

student = {
    "name": "Shivani",
    "age": 21,
    "course": "IT"
}

print(student.keys())

---

"values()"

Returns all values.

print(student.values())

---

"items()"

Returns all key-value pairs.

print(student.items())

---

"get()"

Returns the value of a specified key.

student = {
    "name": "Shivani",
    "age": 21
}

print(student.get("name"))

Output:

Shivani

If the key does not exist:

print(student.get("city"))

Output:

None

---

"update()"

Adds a new key-value pair or updates an existing value.

student = {
    "name": "Shivani",
    "age": 21
}

student.update({"city": "Pune"})

print(student)

Output:

{'name': 'Shivani', 'age': 21, 'city': 'Pune'}

---

"pop()"

Removes a specified key-value pair.

student = {
    "name": "Shivani",
    "age": 21,
    "city": "Pune"
}

student.pop("age")

print(student)

Output:

{'name': 'Shivani', 'city': 'Pune'}

---

"popitem()"

Removes the last inserted key-value pair.

student = {
    "name": "Shivani",
    "age": 21,
    "city": "Pune"
}

student.popitem()

print(student)

Output:

{'name': 'Shivani', 'age': 21}

---

"clear()"

Removes all items from the dictionary.

student = {
    "name": "Shivani",
    "age": 21
}

student.clear()

print(student)

Output:

{}

---

"copy()"

Creates a copy of the dictionary.

student = {
    "name": "Shivani",
    "age": 21
}

new_student = student.copy()

print(new_student)

---

6. Tuple

Definition

A tuple is an ordered and immutable collection of elements.

Immutable means we cannot change the tuple after creating it.

Syntax

my_tuple = (10, 20, 30)

Example

numbers = (10, 20, 30, 40)

print(numbers)

Output:

(10, 20, 30, 40)

---

7. Important Features of Tuple

- Tuple uses round brackets "()"
- Tuple is ordered
- Tuple allows duplicate values
- Tuple supports indexing
- Tuple supports slicing
- Tuple is immutable
- Tuple can contain different data types

Example

data = ("Shivani", 21, 85.5, True)

print(data)

---

8. Tuple Indexing

fruits = ("Apple", "Mango", "Banana")

print(fruits[0])
print(fruits[1])
print(fruits[-1])

Output:

Apple
Mango
Banana

---

9. Tuple Slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

Output:

(20, 30, 40)

---

10. Tuple Methods

Tuple has two main built-in methods.

"count()"

Counts how many times a value occurs in a tuple.

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))

Output:

3

---

"index()"

Returns the index of the first occurrence of a value.

fruits = ("Apple", "Mango", "Banana")

print(fruits.index("Mango"))

Output:

1

---

11. Tuple Unpacking

Assigning tuple values to different variables is called tuple unpacking.

student = ("Shivani", 21, "IT")

name, age, course = student

print(name)
print(age)
print(course)

Output:

Shivani
21
IT

---

# Python Set


A **set** is a built-in collection data type in Python used to store **multiple unique elements**.

### Definition

> A set is an **unordered, mutable collection of unique elements**.

---

# 1. Creating a Set

A set is created using **curly brackets `{}`**.

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

### Output

```text
{10, 20, 30, 40}
```

---

# 2. Set Does Not Allow Duplicate Values

A set automatically removes duplicate values.

```python
numbers = {10, 20, 20, 30, 30, 40}

print(numbers)
```

### Output

```text
{10, 20, 30, 40}
```

### Explanation

The values `20` and `30` were repeated, but the set keeps only one copy of each value.

---

# 3. Set is Unordered

A set does not maintain a fixed order of elements.

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

The output order may not always be the same.

### Important

> A set is **unordered**, so we should not depend on the position of elements.

---

# 4. Set Does Not Support Indexing

Sets do not support indexing.

```python
numbers = {10, 20, 30}

print(numbers[0])
```

This will give an error because a set has **no index-based access**.

### ❌ Incorrect

```python
numbers[0]
```

### ✅ Correct

We can access set elements using a loop.

```python
numbers = {10, 20, 30}

for number in numbers:
    print(number)
```

---

# 5. Set is Mutable

A set is mutable, which means we can **add or remove elements** after creating it.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

### Output

```text
{10, 20, 30, 40}
```

---

# 6. Set Methods

## `add()`

The `add()` method is used to add **one element** to a set.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

---

## `update()`

The `update()` method is used to add **multiple elements**.

```python
numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)
```

### Output

```text
{10, 20, 30, 40, 50}
```

---

## `remove()`

The `remove()` method removes a specified element.

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
```

### Output

```text
{10, 30}
```

### Important

If the element does not exist, `remove()` raises a `KeyError`.

---

## `discard()`

The `discard()` method also removes an element.

```python
numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)
```

Unlike `remove()`, `discard()` does not give an error if the element is not present.

```python
numbers.discard(50)
```

No error will occur.

---

## `pop()`

The `pop()` method removes and returns an **arbitrary element** from the set.

```python
numbers = {10, 20, 30}

value = numbers.pop()

print(value)
print(numbers)
```

Because sets are unordered, we should not assume which element will be removed.

---

## `clear()`

The `clear()` method removes all elements from a set.

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```

### Output

```text
set()
```

---

# 7. Set Operations

Sets support mathematical operations such as **Union, Intersection, Difference, and Symmetric Difference**.

---

## Union `|`

Union combines elements from both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

### Output

```text
{1, 2, 3, 4, 5}
```

### Method

```python
print(a.union(b))
```

---

## Intersection `&`

Intersection returns the elements that are common to both sets.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)
```

### Output

```text
{2, 3}
```

### Method

```python
print(a.intersection(b))
```

---

## Difference `-`

Difference returns elements that are present in the first set but not in the second set.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a - b)
```

### Output

```text
{1}
```

### Method

```python
print(a.difference(b))
```

---

## Symmetric Difference `^`

Symmetric difference returns elements that are present in either set but **not in both**.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a ^ b)
```

### Output

```text
{1, 4}
```

### Method

```python
print(a.symmetric_difference(b))
```

---

# 8. Empty Set

### ❌ This is not an empty set

```python
s = {}
```

`{}` creates an **empty dictionary**.

### ✅ Correct way

```python
s = set()

print(type(s))
```

### Output

```text
<class 'set'>
```

---

# 9. Set with Different Data Types

A set can contain different data types, as long as its elements are hashable.

```python
data = {10, "Python", 20.5, True}

print(data)
```

---

# 10. Set with String Values

```python
languages = {"Python", "Java", "SQL", "Python"}

print(languages)
```

### Output

```text
{'Python', 'Java', 'SQL'}
```

The duplicate `"Python"` is automatically removed.

---
# Python if, elif and else

## 📌 Introduction

`if`, `elif`, and `else` are **conditional statements** in Python.

They are used to make decisions in a program based on whether a condition is **True or False**.

---

## 1. if Statement

The `if` statement is used to execute a block of code when a specified condition is **True**.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote")
```

### Output

```text
You are eligible to vote
```

### Explanation

The condition `age >= 18` is checked.

Since the condition is `True`, the statement inside the `if` block is executed.

---

## 2. else Statement

The `else` statement is executed when the `if` condition is **False**.

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Example

```python
age = 15

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```

### Output

```text
You are not eligible to vote
```

### Explanation

The condition `age >= 18` is `False`, so Python executes the `else` block.

---

## 3. elif Statement

`elif` means **"else if"**.

It is used to check **multiple conditions**.

### Syntax

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

### Output

```text
Grade A
```

### Explanation

Python checks the conditions from top to bottom.

* `marks >= 90` → False
* `marks >= 75` → True
* `Grade A` is printed
* The remaining conditions are not checked

---

# 4. if + elif + else

We can use `if`, `elif`, and `else` together when there are multiple possible outcomes.

### Example

```python
age = 65

if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
```

### Output

```text
Senior Citizen
```

---

# 5. Real-Life Example: Movie Ticket

```python
age = 25

if age < 5:
    print("Ticket is Free")
elif age < 18:
    print("Child Ticket = ₹100")
elif age < 60:
    print("Adult Ticket = ₹200")
else:
    print("Senior Citizen Ticket = ₹150")
```

### Output

```text
Adult Ticket = ₹200
```

### Explanation

| Age         | Ticket                |
| ----------- | --------------------- |
| Below 5     | Free                  |
| 5 to 17     | Child Ticket          |
| 18 to 59    | Adult Ticket          |
| 60 or above | Senior Citizen Ticket |

---

# 6. Even or Odd Example

```python
number = 10

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

### Output

```text
Even Number
```

---

# 7. Positive, Negative or Zero

```python
number = -5

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")
```

### Output

```text
Negative Number
```

---

# 8. Temperature Example

```python
temperature = 35

if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Normal")
else:
    print("Cold")
```

### Output

```text
Hot
```

---

# 9. Important Rules

### Rule 1: `if` is required

An `elif` cannot be used without an `if`.

```python
if condition:
    statement
```

---

### Rule 2: Multiple `elif` statements are allowed

```python
if condition1:
    statement
elif condition2:
    statement
elif condition3:
    statement
elif condition4:
    statement
```

---

### Rule 3: Only one `else` is allowed

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

---

### Rule 4: `else` is optional

```python
if age >= 18:
    print("Eligible")
```

---

### Rule 5: Indentation is mandatory

Correct:

```python
if age >= 18:
    print("Eligible")
```

Incorrect:

```python
if age >= 18:
print("Eligible")
```

---

# 10. How Python Executes Conditions

Python checks conditions **from top to bottom**.

```text
if condition
     ↓
   True? ── Yes ──> Execute if block
     │
     No
     ↓
elif condition
     ↓
   True? ── Yes ──> Execute elif block
     │
     No
     ↓
else
     ↓
Execute else block
```

Once Python finds a **True condition**, it executes that block and skips the remaining blocks.

---

# 11. Difference Between if, elif and else

| Statement | Purpose                                |
| --------- | -------------------------------------- |
| `if`      | Checks the first condition             |
| `elif`    | Checks additional conditions           |
| `else`    | Executes when all conditions are False |

---

# 12. Interview Definition

> **`if`, `elif`, and `else` are conditional statements in Python used to control the flow of a program based on different conditions.**

### Short Definition

> **if** → first condition
> **elif** → additional condition
> **else** → when all conditions are False

---

# 13. Key Points

* `if` checks a condition.
* `elif` means "else if".
* `else` executes when all previous conditions are False.
* Multiple `elif` statements can be used.
* Only one `else` can be used.
* `else` is optional.
* Conditions are checked from top to bottom.
* Python executes the first matching `True` condition.
* Proper indentation is required.

# Python Control Flow & Functions

Complete beginner-to-intermediate revision notes covering:

* Nested `if`
* Loops
* `for` loop
* Reverse loop
* `while` loop
* Factorial
* Loop control statements
* `break`
* `continue`
* `pass`
* Functions
* Five types of arguments
* Python function types
* Built-in functions
* User-defined functions
* Lambda functions
* Recursive functions
* Higher-order functions
* `map()`, `filter()`, `reduce()`

---

# 1. Nested If

## Definition

A **nested if** means writing one `if` statement inside another `if` statement.

## Syntax

```python
if condition1:
    if condition2:
        statement
```

## Example

```python
age = 22
qualification = "BE"

if age >= 18:
    if qualification == "BE":
        print("Eligible for job")
```

### Output

```text
Eligible for job
```

### Explanation

First, Python checks:

```python
age >= 18
```

If it is `True`, Python checks the second condition:

```python
qualification == "BE"
```

If both conditions are `True`, the statement executes.

---

# 2. Loops

## Definition

A **loop** is used to execute a block of code repeatedly.

Instead of writing:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

We can use:

```python
for i in range(5):
    print("Hello")
```

## Types of Loops

Python mainly provides two types of loops:

1. `for` loop
2. `while` loop

---

# 3. For Loop

## Definition

A `for` loop is used to iterate over a sequence or range of values.

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

## range()

```python
range(start, stop, step)
```

Example:

```python
range(1, 6)
```

Here:

```text
Start = 1
Stop = 6
```

The stop value is not included.

So the output is:

```text
1 2 3 4 5
```

---

# 4. For Loop with List

```python
fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)
```

### Output

```text
Apple
Mango
Banana
```

---

# 5. Reverse Loop

## Definition

A reverse loop executes from a larger value to a smaller value.

## Example

```python
for i in range(5, 0, -1):
    print(i)
```

### Output

```text
5
4
3
2
1
```

## Explanation

```python
range(5, 0, -1)
```

Means:

```text
Start = 5
Stop = 0
Step = -1
```

`0` is not included.

---

# 6. Reverse Loop with Step

```python
for i in range(10, 0, -2):
    print(i)
```

### Output

```text
10
8
6
4
2
```

---

# 7. While Loop

## Definition

A `while` loop executes a block of code as long as the condition is `True`.

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

## Working

```text
i = 1
1 <= 5 → True → print 1
i = 2

2 <= 5 → True → print 2
i = 3

3 <= 5 → True → print 3
i = 4

4 <= 5 → True → print 4
i = 5

5 <= 5 → True → print 5
i = 6

6 <= 5 → False
Loop stops
```

> **Important:** In a `while` loop, update the variable when required. Otherwise, an infinite loop may occur.

---

# 8. Factorial Number

## Definition

The factorial of a positive integer `n` is the multiplication of all positive integers from `1` to `n`.

It is represented as:

```text
n!
```

Example:

```text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

---

# 9. Factorial Using For Loop

```python
num = 5
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)
```

### Output

```text
Factorial = 120
```

## Logic

```text
fact = 1

i = 1 → 1 × 1 = 1
i = 2 → 1 × 2 = 2
i = 3 → 2 × 3 = 6
i = 4 → 6 × 4 = 24
i = 5 → 24 × 5 = 120
```

---

# 10. Factorial Using While Loop

```python
num = 5
fact = 1
i = 1

while i <= num:
    fact = fact * i
    i += 1

print("Factorial =", fact)
```

### Output

```text
Factorial = 120
```

---

# 11. Loop Control Statements

Loop control statements are used to change the normal execution of a loop.

There are three important loop control statements:

1. `break`
2. `continue`
3. `pass`

---

# 12. Break

## Definition

`break` is used to immediately stop a loop.

## Example

```python
for i in range(1, 11):

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

When `i == 5`, the `break` statement terminates the loop.

---

# 13. Continue

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

When `i == 3`, Python skips that iteration.

---

# 14. Pass

## Definition

`pass` is a null statement. It does nothing.

It is useful when we want to create a block of code but implement it later.

## Example

```python
for i in range(1, 6):

    if i == 3:
        pass

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

---

# 15. Break vs Continue vs Pass

| Statement  | Purpose                     |
| ---------- | --------------------------- |
| `break`    | Stops the loop completely   |
| `continue` | Skips the current iteration |
| `pass`     | Does nothing                |

---

# 16. Function

## Definition

A **function** is a reusable block of code that performs a specific task.

## Syntax

```python
def function_name():
    statements
```

## Example

```python
def greet():
    print("Hello Shivani")

greet()
```

### Output

```text
Hello Shivani
```

Here:

```python
def greet():
```

defines the function.

```python
greet()
```

calls the function.

---

# 17. Function with Parameters

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
a, b → Parameters
10, 20 → Arguments
```

---

# 18. Function with Return

The `return` statement sends a value back to the caller.

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

## print vs return

| `print()`                            | `return`                 |
| ------------------------------------ | ------------------------ |
| Displays a value                     | Sends a value back       |
| Mainly used for output               | Used to return result    |
| Does not return the result to caller | Returns result to caller |

---

# 19. Five Types of Function Arguments

Python commonly uses five types of arguments:

1. Positional arguments
2. Default arguments
3. Keyword arguments
4. Arbitrary positional arguments - `*args`
5. Arbitrary keyword arguments - `**kwargs`

---

# 20. Positional Arguments

## Definition

Positional arguments are passed according to their position or order.

## Example

```python
def employee(name, salary):
    print(name)
    print(salary)

employee("Shivani", 50000)
```

### Output

```text
Shivani
50000
```

Here:

```text
"Shivani" → name
50000 → salary
```

### Interview Definition

> Positional arguments are arguments passed to a function based on their position or order.

---

# 21. Default Arguments

## Definition

A default argument has a predefined value that is used when the caller does not provide a value.

## Example

```python
def employee(name, city="Pune"):
    print(name)
    print(city)

employee("Shivani")
```

### Output

```text
Shivani
Pune
```

Here:

```python
city="Pune"
```

is the default value.

We can also provide another value:

```python
employee("Shivani", "Mumbai")
```

Output:

```text
Shivani
Mumbai
```

---

# 22. Keyword Arguments

## Definition

Keyword arguments are passed using the parameter name.

## Example

```python
def employee(name, salary):
    print(name)
    print(salary)

employee(salary=50000, name="Shivani")
```

### Output

```text
Shivani
50000
```

The order does not matter because we specify the parameter names.

### Interview Definition

> Keyword arguments are arguments passed using the parameter name.

---

# 23. Arbitrary Positional Arguments - `*args`

## Definition

`*args` allows a function to accept any number of positional arguments.

## Example

```python
def total(*numbers):
    print(numbers)

total(10, 20, 30, 40)
```

### Output

```text
(10, 20, 30, 40)
```

`*args` stores the values as a **tuple**.

## Practical Example

```python
def total(*numbers):

    result = 0

    for number in numbers:
        result = result + number

    return result

print(total(10, 20, 30))
```

### Output

```text
60
```

We can pass any number of values:

```python
total(10)
total(10, 20)
total(10, 20, 30, 40)
```

---

# 24. Arbitrary Keyword Arguments - `**kwargs`

## Definition

`**kwargs` allows a function to accept any number of keyword arguments.

## Example

```python
def employee(**details):
    print(details)

employee(
    name="Shivani",
    city="Pune",
    salary=50000
)
```

### Output

```text
{'name': 'Shivani', 'city': 'Pune', 'salary': 50000}
```

`**kwargs` stores the values as a **dictionary**.

## Practical Example

```python
def employee(**details):

    for key, value in details.items():
        print(key, "=", value)

employee(
    name="Shivani",
    city="Pune",
    skill="Python"
)
```

### Output

```text
name = Shivani
city = Pune
skill = Python
```

---

# 25. `*args` vs `**kwargs`

| `*args`                       | `**kwargs`                 |
| ----------------------------- | -------------------------- |
| Multiple positional arguments | Multiple keyword arguments |
| Stored as tuple               | Stored as dictionary       |
| Uses `*`                      | Uses `**`                  |
| Example: `fun(10, 20, 30)`    | Example: `fun(a=10, b=20)` |

---

# 26. Python Function Types

Important function types:

1. Built-in functions
2. User-defined functions
3. Lambda functions
4. Recursive functions
5. Higher-order functions

---

# 27. Built-in Functions

## Definition

Built-in functions are predefined functions provided by Python.

We can use them directly without defining them.

## Examples

```python
print()
len()
type()
max()
min()
sum()
range()
input()
int()
str()
list()
```

## Example

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

### Output

```text
4
40
10
100
```

---

# 28. User-Defined Function

## Definition

A user-defined function is a function created by the programmer using the `def` keyword.

## Example

```python
def square(number):
    return number * number

print(square(5))
```

### Output

```text
25
```

---

# 29. Lambda Function

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

## Two Arguments

```python
add = lambda a, b: a + b

print(add(10, 20))
```

### Output

```text
30
```

## Even Number

```python
check_even = lambda x: x % 2 == 0

print(check_even(10))
```

### Output

```text
True
```

---

# 30. Recursive Function

## Definition

A recursive function is a function that calls itself.

A recursive function generally has:

1. Base condition
2. Recursive call

## Example: Factorial

```python
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
```

### Output

```text
120
```

## Working

```text
factorial(5)
    ↓
5 × factorial(4)
    ↓
5 × 4 × factorial(3)
    ↓
5 × 4 × 3 × factorial(2)
    ↓
5 × 4 × 3 × 2 × factorial(1)
    ↓
factorial(1) = 1
    ↓
120
```

## Important

The base condition prevents infinite recursive calls.

### Interview Definition

> A recursive function is a function that calls itself until a base condition is satisfied.

---

# 31. Fibonacci Using Recursion

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(7):
    print(fibonacci(i), end=" ")
```

### Output

```text
0 1 1 2 3 5 8
```

---

# 32. Higher-Order Function

## Definition

A higher-order function is a function that:

1. Takes another function as an argument, or
2. Returns another function.

## Example

```python
def add(a, b):
    return a + b


def calculate(operation, x, y):
    return operation(x, y)


result = calculate(add, 10, 20)

print(result)
```

### Output

```text
30
```

Here:

```python
calculate(add, 10, 20)
```

passes the `add` function as an argument.

Therefore, `calculate()` is a higher-order function.

---

# 33. Higher-Order Function with Lambda

```python
def calculate(operation, a, b):
    return operation(a, b)


result = calculate(
    lambda x, y: x + y,
    10,
    20
)

print(result)
```

### Output

```text
30
```

---

# 34. map()

## Definition

`map()` applies a function to every element of an iterable.

## Example

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))
```
### Output

```text
[2, 4, 6, 8, 10]
```
# 35. filter()

## Definition

`filter()` selects elements that satisfy a condition.

## Example

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```
### Output

```text
[2, 4, 6]
```

Only even numbers are selected.

---

# 36. reduce()

## Definition

`reduce()` repeatedly applies a function to elements and produces a single final result.

It is available from the `functools` module.

## Example

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

### Output

```text
15
```
## Logic

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```-
# 37. map vs filter vs reduce

| Function   | Purpose                | Result                      |
| ---------- | ---------------------- | --------------------------- |
| `map()`    | Transform each element | Multiple transformed values |
| `filter()` | Select elements        | Filtered values             |
| `reduce()` | Combine elements       | Single value                |


# Python OOPs – Complete Notes

## 1. Object-Oriented Programming (OOP)

### Definition
Object-Oriented Programming (OOP) is a programming approach based on classes and objects. It helps organize code, reuse code, and manage data effectively.

### Four Pillars of OOP
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

### Real-World Example
Consider a mobile phone.

- Class: Mobile
- Object: Samsung mobile
- Attributes: Brand, price, battery
- Methods: Call, message, take_photo

---

## 2. Class and Object

### Class
A class is a blueprint for creating objects.

### Object
An object is an instance of a class.

### Example

```python
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


m1 = Mobile("Samsung", 20000)
m1.display()
```

### Output

```text
Brand: Samsung
Price: 20000
```

### Explanation
- `class` defines a class.
- `__init__()` initializes an object.
- `self` refers to the current object.
- `brand` and `price` are instance attributes.
- `display()` is an instance method.
- `m1` is an object.

---

## 3. Attributes in Python

Attributes are variables associated with a class or an object.

### 3.1 Instance Attributes

Instance attributes belong to individual objects.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Amit", 30000)
e2 = Employee("Priya", 40000)

print(e1.name)
print(e2.name)
print(e1.salary)
print(e2.salary)
```

Output:

```text
Amit
Priya
30000
40000
```

### 3.2 Class Attributes

Class attributes are defined inside the class but outside its methods.

```python
class Employee:
    company = "Tech Solutions"

    def __init__(self, name):
        self.name = name


e1 = Employee("Amit")
e2 = Employee("Priya")

print(e1.company)
print(e2.company)
print(Employee.company)
```

Output:

```text
Tech Solutions
Tech Solutions
Tech Solutions
```

### 3.3 Local Variables

Local variables are defined inside a function or method.

```python
class Employee:
    def display(self):
        message = "Welcome to the company"
        print(message)


e1 = Employee()
e1.display()
```

Output:

```text
Welcome to the company
```

### Difference Between Attributes

| Instance Attribute | Class Attribute | Local Variable |
|---|---|---|
| Belongs to an object | Belongs to a class | Belongs to a function's scope |
| `self.name` | `company` | `message` |
| Usually different for each object | Shared through the class | Used within the function or method |

---

## 4. Methods in Python

A method is a function defined inside a class.

### 4.1 Instance Method

An instance method uses `self` to access object attributes.

```python
class Mobile:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(self.brand)


m1 = Mobile("Samsung")
m1.show_brand()
```

Output:

```text
Samsung
```

### 4.2 Class Method

A class method uses `cls` to access class-level data. It is declared using `@classmethod`.

```python
class Company:
    company_name = "Tech Solutions"

    @classmethod
    def show_company(cls):
        print(cls.company_name)


Company.show_company()
```

Output:

```text
Tech Solutions
```

### 4.3 Static Method

A static method does not automatically receive `self` or `cls`.

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
```

Output:

```text
30
```

### Difference Between Methods

| Instance Method | Class Method | Static Method |
|---|---|---|
| Uses `self` | Uses `cls` | No automatic `self` or `cls` |
| Works with object data | Works with class-level data | Performs a related utility task |
| No special decorator required | `@classmethod` | `@staticmethod` |

---

## 5. Constructor in Python

### Definition
A constructor is commonly described as a special method used to initialize an object. In Python, `__init__()` initializes an object after it has been created.

### 5.1 Default Constructor

When a class does not define its own `__init__()`, Python can use an inherited or default initialization mechanism.

```python
class Mobile:
    def display(self):
        print("Mobile is ready")


m1 = Mobile()
m1.display()
```

Output:

```text
Mobile is ready
```

### 5.2 Non-Parameterized Constructor

A custom `__init__()` that takes only `self`.

```python
class Mobile:
    def __init__(self):
        self.brand = "Samsung"
        self.price = 20000

    def display(self):
        print(self.brand, self.price)


m1 = Mobile()
m1.display()
```

Output:

```text
Samsung 20000
```

### 5.3 Parameterized Constructor

A constructor that accepts additional arguments to initialize object attributes.

```python
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(self.brand, self.price)


m1 = Mobile("Apple", 50000)
m1.display()
```

Output:

```text
Apple 50000
```

### Difference Between Constructor Types

| Type | Description |
|---|---|
| Default | No custom initializer is defined in the class |
| Non-parameterized | Custom initializer without extra arguments |
| Parameterized | Initializer accepts extra arguments |

**Note:** Python does not support traditional constructor overloading through multiple `__init__()` definitions. The last definition replaces earlier definitions.

---

## 6. Inheritance in Python

### Definition
Inheritance allows a child class to acquire attributes and methods from a parent class. It promotes code reusability.

- Parent class: Base class or superclass
- Child class: Derived class or subclass

### Example

```python
class Company:
    def company_info(self):
        print("Welcome to Tech Solutions")


class Intern(Company):
    def intern_info(self):
        print("I am a Data Science Intern")


i1 = Intern()

i1.company_info()
i1.intern_info()
Output:

```text
Welcome to Tech Solutions
I am a Data Science Intern
```

### Types of Inheritance

#### 6.1 Single Inheritance

One child inherits from one parent.

```python
class A:
    def show(self):
        print("Parent class")


class B(A):
    pass


b = B()
b.show()
```

#### 6.2 Multiple Inheritance

One child inherits from multiple parent classes.

```python
class A:
    def show_a(self):
        print("Class A")


class B:
    def show_b(self):
        print("Class B")


class C(A, B):
    pass


c = C()
c.show_a()
c.show_b()
```

Output:

```text
Class A
Class B
```

#### 6.3 Multilevel Inheritance

A class inherits from another child class, forming a chain.

```python
class A:
    def show_a(self):
        print("Class A")


class B(A):
    pass


class C(B):
    pass


c = C()
c.show_a()
```

#### 6.4 Hierarchical Inheritance

Multiple child classes inherit from the same parent.

```python
class Company:
    def info(self):
        print("Company information")


class Developer(Company):
    pass


class Tester(Company):
    pass


d = Developer()
t = Tester()

d.info()
t.info()
```

#### 6.5 Hybrid Inheritance

A combination of two or more inheritance types.

```python
class A:
    def show(self):
        print("Class A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()
d.show()
```

### The `super()` Function

`super()` allows a child class to call a method from its parent according to the method resolution order (MRO).

```python
class Company:
    def __init__(self):
        print("Company constructor")


class Intern(Company):
    def __init__(self):
        super().__init__()
        print("Intern constructor")


i1 = Intern()
```

Output:

```text
Company constructor
Intern constructor
```

---

## 7. Method Overloading and Method Overriding

### 7.1 Method Overloading

Method overloading means using the same method name with different parameter patterns.

Python does not support traditional method overloading through multiple same-named method definitions in one class. Similar behavior can be achieved using default arguments or variable-length arguments.

```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


c = Calculator()

print(c.add(10, 20))
print(c.add(10, 20, 30))
print(c.add(10))
```

Output:

```text
30
60
10
```

### 7.2 Method Overriding

Method overriding occurs when a child class provides its own implementation of an inherited method.

```python
class Notification:
    def send(self):
        print("Sending a general notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending an email")


n1 = EmailNotification()
n1.send()
```

Output:

```text
Sending an email
```

### Difference Between Overloading and Overriding

| Method Overloading | Method Overriding |
|---|---|
| Same method name with different parameter patterns | Child redefines an inherited method |
| Commonly associated with one class | Requires inheritance |
| Python uses alternative techniques | Supported directly in Python |
| Example: `add(2, 3)` and `add(2, 3, 4)` | Parent and child both define `send()` |

---

## 8. Polymorphism in Python

### Definition
Polymorphism means "many forms." It allows the same operation or method name to behave differently for different objects or data types.

### Example: Method Behavior

```python
class Developer:
    def work(self):
        print("Developer writes code")


class Tester:
    def work(self):
        print("Tester tests software")


def perform_work(employee):
    employee.work()


d = Developer()
t = Tester()

perform_work(d)
perform_work(t)
```

Output:

```text
Developer writes code
Tester tests software
```

### Operator Overloading

Operators can perform different operations depending on the data type.

```python
print(10 + 20)
print("Hello " + "Python")
print([1, 2] + [3, 4])
```

Output:

```text
30
Hello Python
[1, 2, 3, 4]
```

### Compile-Time vs Runtime Polymorphism

| Compile-Time Polymorphism | Runtime Polymorphism |
|---|---|
| Commonly resolved during compilation | Behavior is selected during execution |
| Often associated with traditional method overloading | Often associated with method overriding |
| Python does not have Java-style signature-based method overloading | Python supports runtime method overriding |

---

## 9. Encapsulation in Python

### Definition
Encapsulation means bundling data and methods into a single unit and controlling how internal data is accessed or modified.

### Example: Mobile Battery

```python
class Mobile:
    def __init__(self, battery):
        self.__battery = battery

    def get_battery(self):
        return self.__battery

    def set_battery(self, value):
        if 0 <= value <= 100:
            self.__battery = value
        else:
            print("Invalid battery percentage")


m1 = Mobile(70)

print(m1.get_battery())

m1.set_battery(85)
print(m1.get_battery())

m1.set_battery(150)
```

Output:

```text
70
85
Invalid battery percentage
```

### Explanation
- `__battery` uses name mangling.
- `get_battery()` reads the battery value.
- `set_battery()` validates changes.
- Invalid values are rejected.

### Benefits
1. Protects data from accidental changes.
2. Provides controlled access to internal data.
3. Supports validation.
4. Improves code maintainability.

---

## 10. Access Modifiers in Python

Access modifiers describe how attributes and methods are intended to be accessed.

Python uses naming conventions rather than strict access enforcement.

### 10.1 Public

Public members can be accessed wherever the object or class is accessible.

```python
class Mobile:
    def __init__(self):
        self.brand = "Samsung"


m1 = Mobile()
print(m1.brand)
```

### 10.2 Protected-Style

A single underscore indicates that a member is intended for internal use.

```python
class Mobile:
    def __init__(self):
        self._battery = 80


m1 = Mobile()
print(m1._battery)
```

Output:

```text
80
```

### 10.3 Private-Style

A double underscore triggers name mangling.

```python
class Mobile:
    def __init__(self):
        self.__pin = 1234

    def show_pin(self):
        print(self.__pin)


m1 = Mobile()
m1.show_pin()
```

Output:

```text
1234
```

### Difference Between Access Modifiers

| Type | Syntax | Meaning |
|---|---|---|
| Public | `name` | General access |
| Protected-style | `_name` | Intended for internal/subclass use |
| Private-style | `__name` | Name-mangled to reduce accidental access |

**Note:** Python's private-style members are not absolutely inaccessible. Double underscores provide name mangling, not strict privacy.

---

## 11. Getter and Setter Methods

### Definition
A getter retrieves an attribute's value, while a setter changes the value, often after validation.

### Example

```python
class Laptop:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive")


l1 = Laptop(45000)

print(l1.get_price())

l1.set_price(50000)
print(l1.get_price())

l1.set_price(-100)
```

Output:

```text
45000
50000
Price must be positive
```

### Getter and Setter Using `@property`

```python
class Laptop:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError("Price must be positive")


l1 = Laptop(45000)

print(l1.price)

l1.price = 50000
print(l1.price)
```

Output:

```text
45000
50000
```

### Benefits
- Provides controlled access.
- Supports input validation.
- Helps maintain valid object state.
- Allows the implementation to change without changing attribute-style access.

---

## 12. Abstraction in Python

### Definition
Abstraction hides implementation details and shows only essential functionality to the user.

Python supports abstraction using abstract classes and abstract methods from the `abc` module.

### Example: Payment System

```python
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using UPI")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using Card")


p1 = UpiPayment()
p2 = CardPayment()

p1.pay(1000)
p2.pay(2000)
```

Output:

```text
Paid Rs. 1000 using UPI
Paid Rs. 2000 using Card
```

### Explanation
- `ABC` is the base class for abstract classes.
- `@abstractmethod` declares a method that concrete subclasses must implement.
- `Payment` defines the required interface.
- `UpiPayment` and `CardPayment` implement the payment behavior.

### Benefits
1. Reduces complexity.
2. Defines a common interface.
3. Encourages consistent implementations.
4. Makes code easier to extend.

### Encapsulation vs Abstraction

        Encapsulation                                     Abstraction 
| Bundles data and methods and controls access  | Hides implementation details |
| Focuses on managing internal state            | Focuses on essential functionality |
| Example: validating battery percentage        | Example: using a payment interface |

---

## 13. Decorators in Python

### Definition
A decorator is a function that modifies or extends the behavior of another function or method without changing its original source code.

### 13.1 Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@my_decorator
def greet():
    print("Hello Python")


greet()
```

Output:

```text
Before function execution
Hello Python
After function execution
```

### Explanation
1. `my_decorator()` receives the original function.
2. `wrapper()` adds extra behavior.
3. `return wrapper` returns the new function.
4. `@my_decorator` applies the decorator.
5. Calling `greet()` executes the wrapped behavior.

The following syntax is equivalent to applying the decorator:

```python
greet = my_decorator(greet)
```

### 13.2 Decorator with Arguments

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function completed")
        return result
    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

Output:

```text
Function started
Function completed
30
```

### Explanation
- `*args` accepts positional arguments.
- `**kwargs` accepts keyword arguments.
- `result` stores the returned value.
- `return result` passes the value back to the caller.

### 13.3 Important Built-In Decorators

#### `@staticmethod`

Defines a method that does not automatically receive `self` or `cls`.

```python
class Calculator:
    @staticmethod
    def square(n):
        return n * n
print(Calculator.square(5))
Output: `25`

#### `@classmethod`

Defines a method that receives the class as `cls`.

```python
class Company:
    name = "Tech Solutions"

    @classmethod
    def show(cls):
        print(cls.name)


Company.show()
Output: `Tech Solutions`

#### `@property`

Allows a method to be accessed like an attribute.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2
c = Circle(5)
print(c.area)
Output: `78.5`

#### `@abstractmethod`

Declares a method that must be implemented by a concrete subclass.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
      
Errors in Python

An error is a problem in a program that prevents it from running correctly.

Types of Errors

Syntax Error: Occurs when Python syntax rules are not followed.

Runtime Error: Occurs while the program is running.

Logical Error: The program runs, but the output is incorrect.

Example: Syntax Error

if 10 > 5
    print("Hello")

Output: SyntaxError

Correction:

if 10 > 5:
    print("Hello")

2. Common Python Exceptions

Exception

Meaning

ZeroDivisionError

Dividing a number by zero

ValueError

Correct data type but invalid value

TypeError

Operation on incompatible data types

NameError

Using an undefined variable

IndexError

Accessing an invalid list index

KeyError

Accessing a missing dictionary key

FileNotFoundError

File does not exist

AttributeError

Accessing a missing attribute

ImportError

Importing an unavailable module or name

Example: ZeroDivisionError

a = 10
b = 0

print(a / b)

Output:

ZeroDivisionError: division by zero

Example: ValueError

age = int("hello")
print(age)

Output: ValueError

Example: TypeError

a = 10
b = "20"

print(a + b)

Output: TypeError

Example: IndexError

numbers = [10, 20, 30]

print(numbers[5])

Output: IndexError

3. Exception Handling

Exception handling is the process of handling runtime errors so that a program can respond appropriately instead of terminating unexpectedly.

try and except

try: Contains code that may raise an exception.

except: Handles the exception if it occurs.

try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

Output:

Cannot divide by zero

Handling Multiple Exceptions

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")

The else Block

The else block executes when no exception occurs in the try block.

try:
    a = 10
    b = 2
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Program executed successfully")

Output:

5.0
Program executed successfully

The finally Block

The finally block executes whether an exception occurs or not. It is commonly used for cleanup operations.

try:
    print(10 / 2)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program completed")

Output:

5.0
Program completed

The raise Keyword

The raise keyword is used to raise an exception manually.

age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")

print("Eligible")

Output: ValueError: Age must be 18 or above

4. File Handling in Python

File handling is the process of creating, reading, writing, and updating files using Python.

Syntax

file = open("demo.txt", "r")
file.close()

File Opening Modes

Mode

Description

r

Read an existing file

w

Write to a file; creates it or overwrites existing content

a

Append content at the end of a file

x

Create a new file; raises an error if it already exists

r+

Read and write

w+

Write and read; overwrites existing content

a+

Append and read

rb

Read a file in binary mode

wb

Write a file in binary mode

Create a File

file = open("demo.txt", "x")
file.close()

print("File created successfully")

Note: This raises FileExistsError if the file already exists.

Write to a File

file = open("demo.txt", "w")
file.write("Hello Python")
file.close()

print("Data written successfully")

Read a File

file = open("demo.txt", "r")
data = file.read()
print(data)
file.close()

Output:

Hello Python

Append Data to a File

file = open("demo.txt", "a")
file.write("\nWelcome to Python")
file.close()

The new text is added at the end of the file.

5. File Reading Methods

read()

Reads the entire file or a specified number of characters.

with open("demo.txt", "r") as file:
    print(file.read())

readline()

Reads one line at a time.

with open("demo.txt", "r") as file:
    print(file.readline())

readlines()

Reads all lines and returns them as a list.

with open("demo.txt", "r") as file:
    print(file.readlines())

write()

Writes a string to a file.

with open("demo.txt", "w") as file:
    file.write("Python is easy to learn.")

writelines()

Writes multiple strings to a file. It does not automatically add newline characters.

lines = ["Python\n", "Java\n", "SQL\n"]

with open("demo.txt", "w") as file:
    file.writelines(lines)

6. The with open() Statement

The with open() statement automatically closes the file when the block finishes, including when an exception occurs.

with open("demo.txt", "r") as file:
    data = file.read()
    print(data)

This is generally preferred over manually calling close().

7. tell() and seek()

tell()

Returns the current position of the file cursor.

with open("demo.txt", "r") as file:
    print(file.tell())
    file.read(5)
    print(file.tell())

seek()

Moves the file cursor to a specified position.

with open("demo.txt", "r") as file:
    file.seek(0)
    print(file.read())

8. File Handling with Exception Handling

try:
    with open("demo.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File does not exist")

except PermissionError:
    print("Permission denied")

This prevents common file access errors from terminating the program unexpectedly.

9. Real-World Example: Billing System

try:
    customer_name = input("Enter customer name: ")
    amount = float(input("Enter bill amount: "))

    if amount < 0:
        raise ValueError("Bill amount cannot be negative")

    with open("bill.txt", "a") as file:
        file.write(
            f"Customer: {customer_name}, Bill: {amount:.2f}\n"
        )

    print("Bill saved successfully")

except ValueError as e:
    print("Invalid input:", e)

except OSError:
    print("Unable to save the bill")

finally:
    print("Billing process completed")

Concepts used:

try and except

raise

with open()

Append mode

File exception handling

finally

10. Difference Between Errors and Exceptions

Errors

Exceptions

Indicate problems in a program

Represent conditions that can often be handled

Syntax errors prevent code from being parsed

Runtime exceptions may occur during execution

Logical errors can produce incorrect results

Exceptions can be handled using try and except


Append new data to an existing file.

Handle FileNotFoundError.

Create a simple billing system using file handling.

Demonstrate try, except, else, and finally.

Iterators in Python

What is an Iterator?

An iterator is an object that returns one element at a time from a collection or sequence.

An iterator remembers its current position and provides the next available element whenever we request it.

Example

numbers = [10, 20, 30, 40]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

Output:

10
20
30
40

Explanation

numbers is a list.

iter(numbers) creates an iterator.

next(it) returns the next element.

Each call moves the iterator forward.

If you request another element after the iterator is exhausted, Python raises StopIteration.

numbers = [10, 20]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

Output:

10
20
StopIteration

The third call raises the exception because no elements remain.

2. Types of Iterators

Python does not define a fixed set of official iterator types. However, iterators can be classified by how they are created and used.

2.1 Built-in Collection Iterators

These iterators are created from collections such as lists, tuples, strings, dictionaries, and sets.

List Iterator

numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))

Output:

10
20

Tuple Iterator

colors = ("red", "green", "blue")

it = iter(colors)

print(next(it))
print(next(it))

Output:

red
green

String Iterator

name = "Python"

it = iter(name)

print(next(it))
print(next(it))

Output:

P
y

Dictionary Iterator

By default, iterating over a dictionary returns its keys.

employee = {
    "name": "Shivani",
    "role": "Developer",
    "city": "Pune"
}

it = iter(employee)

print(next(it))
print(next(it))

Output:

name
role

To iterate over dictionary values:

employee = {
    "name": "Shivani",
    "role": "Developer"
}

for value in employee.values():
    print(value)

Output:

Shivani
Developer

2.2 File Iterators

A file object is iterable. It returns one line at a time.

with open("demo.txt", "w") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("SQL\n")

with open("demo.txt", "r") as file:
    it = iter(file)

    print(next(it), end="")
    print(next(it), end="")

Output:

Python
Java

2.3 Generator Iterators

Generators produce values one at a time using yield.

def numbers():
    yield 10
    yield 20
    yield 30

it = numbers()

print(next(it))
print(next(it))
print(next(it))

Output:

10
20
30

2.4 Custom Iterators

We can create our own iterator by defining the __iter__() and __next__() methods.

class Count:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        raise StopIteration


counter = Count(3)

for number in counter:
    print(number)

Output:

1
2
3

Explanation

__iter__() returns the iterator object.

__next__() returns the next value.

StopIteration signals that iteration is complete.

3. Iterable vs Iterator

An iterable is an object from which an iterator can be created. An iterator is an object that produces elements one at a time.

Iterable

Iterator

Can provide an iterator

Produces the next element

Supports iter()

Supports next()

Examples: list, tuple, string

Examples: iter(list), generators

Often can be iterated over repeatedly

Usually gets exhausted after one complete pass

Example

numbers = [10, 20, 30]  # Iterable

it = iter(numbers)      # Iterator

print(next(it))
print(next(it))

Output:

10
20

To check whether an object is an iterator:

numbers = [10, 20, 30]
it = iter(numbers)

print(hasattr(numbers, "__iter__"))
print(hasattr(numbers, "__next__"))

print(hasattr(it, "__iter__"))
print(hasattr(it, "__next__"))

Output:

True
False
True
True

4. iter() and next()

iter()

The iter() function returns an iterator from an iterable.

fruits = ["Apple", "Mango", "Banana"]

it = iter(fruits)

print(it)

next()

The next() function retrieves the next element from an iterator.

fruits = ["Apple", "Mango", "Banana"]

it = iter(fruits)

print(next(it))
print(next(it))
print(next(it))

Output:

Apple
Mango
Banana

Using a Default Value with next()

You can supply a default value to avoid StopIteration when the iterator is exhausted.

numbers = iter([10, 20])

print(next(numbers, "Finished"))
print(next(numbers, "Finished"))
print(next(numbers, "Finished"))

Output:

10
20
Finished

5. Generators and yield

What is a Generator?

A generator is a special type of iterator that produces values one at a time instead of building and returning the entire result at once.

Generators are commonly created using:

Generator functions with yield.

Generator expressions.

5.1 Generator Function

def my_generator():
    yield 10
    yield 20
    yield 30

for value in my_generator():
    print(value)

Output:

10
20
30

Explanation

Calling my_generator() creates a generator object.

The function starts executing when the generator is advanced.

yield returns a value and pauses the function.

The next iteration resumes execution after the previous yield.

5.2 Generator Expression

A generator expression is similar to a list comprehension, but it produces values lazily.

List Comprehension

numbers = [n * n for n in range(5)]

print(numbers)

Output:

[0, 1, 4, 9, 16]

This creates a list containing all the results.

Generator Expression

numbers = (n * n for n in range(5))

print(next(numbers))
print(next(numbers))
print(next(numbers))

Output:

0
1
4

This calculates each result as it is requested.

5.3 Real-World Example: Processing Large Data

Suppose a file contains millions of records. A generator can process records one at a time rather than loading every record into a list.

def read_numbers(limit):
    for number in range(1, limit + 1):
        yield number

for number in read_numbers(5):
    print(number)

Output:

1
2
3
4
5

This approach is useful when working with large datasets, files, or streams.

6. yield vs return

yield

return

Produces a value and pauses the function

Ends the function

Preserves the function's local state

Does not resume that function call

Used to create generator functions

Used to return a final result

Can produce multiple values over time

A function call returns when it reaches return

Example Using return

def get_number():
    return 10
    return 20

print(get_number())

Output:

10

The function ends at the first return.

Example Using yield

def get_numbers():
    yield 10
    yield 20
    yield 30

for number in get_numbers():
    print(number)

Output:

10
20
30

The generator pauses after each yield and resumes when the next value is requested.

7. Method Resolution Order (MRO)

What is MRO?

Method Resolution Order (MRO) is the order in which Python searches classes for a method or attribute, particularly when inheritance involves multiple parent classes.

Python uses the C3 linearization algorithm to calculate MRO for new-style classes.

7.1 Single Inheritance

class Parent:
    def show(self):
        print("Parent method")


class Child(Parent):
    pass


obj = Child()
obj.show()

print(Child.mro())

Output:

Parent method
[<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>]

Explanation

Python searches in this order:

Child

Parent

object

Since Child does not define show(), Python finds it in Parent.

7.2 Multiple Inheritance

class Father:
    def show(self):
        print("Father method")


class Mother:
    def show(self):
        print("Mother method")


class Child(Father, Mother):
    pass


obj = Child()
obj.show()

print(Child.mro())

Output:

Father method
[<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]

Explanation

The inheritance declaration is:

class Child(Father, Mother):

Python checks Child first, then Father, then Mother, then object.

Because both parents define show(), the Father version is called first.

Changing the parent order changes the lookup order in this example.

class Child(Mother, Father):
    pass

Now Mother is searched before Father.

7.3 MRO with super()

The super() function calls the next implementation in the MRO. It does not always mean "call my direct parent."

class A:
    def show(self):
        print("A")
        

class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


obj = D()
obj.show()

print([cls.__name__ for cls in D.mro()])

Output:

D
B
C
A
['D', 'B', 'C', 'A', 'object']

Explanation

The MRO of D is:

D → B → C → A → object

Each super().show() continues to the next class in this order.

This coordinated behavior is especially useful in multiple inheritance.

7.4 Ways to Check MRO

Using mro()

print(D.mro())

Using __mro__

print(D.__mro__)

Both show the class lookup order.

Interview Definition

MRO is the order in which Python searches a class hierarchy for methods and attributes. Python calculates it using the C3 linearization algorithm.

8. Memory Management in Python

What is Memory Management?

Memory management is the process of allocating, using, and releasing computer memory for objects and data while a program runs.

Python manages memory automatically, so developers generally do not need to manually allocate and free memory.

Python's memory management includes:

Memory allocation

Object references

Reference counting

Garbage collection

Memory allocation and reuse by the Python memory manager

8.1 Creating Objects

name = "Shivani"
age = 22
numbers = [10, 20, 30]

Python creates objects to represent the string, integer, and list. The variables refer to those objects.

The exact internal memory layout depends on the Python implementation.

8.2 Variables and References

a = [10, 20, 30]
b = a

print(a)
print(b)
print(a is b)

Output:

[10, 20, 30]
[10, 20, 30]
True

Explanation

a refers to a list object.

b = a makes b refer to the same list.

It does not create a separate list.

If you modify the list through either variable, the change is visible through both.

a = [10, 20, 30]
b = a

b.append(40)

print(a)
print(b)

Output:

[10, 20, 30, 40]
[10, 20, 30, 40]

This is an important concept when learning Python memory management.

9. Reference Counting

What is Reference Counting?

Reference counting is a memory-management technique that tracks how many references point to an object.

In CPython, an object can often be reclaimed when its reference count reaches zero, provided no other mechanism or implementation detail keeps it alive.

Example

import sys

numbers = [10, 20, 30]

print(sys.getrefcount(numbers))

sys.getrefcount() reports the reference count in CPython, but calling the function itself creates a temporary reference. Therefore, the displayed value is generally one greater than the references you might count in your source code.

Example: Multiple References

numbers = [10, 20, 30]

other = numbers
another = numbers

print(numbers is other)
print(numbers is another)

Output:

True
True

All three variables refer to the same list.

Removing a Reference

numbers = [10, 20, 30]

other = numbers

del numbers

print(other)

Output:

[10, 20, 30]

Explanation

Deleting numbers removes that variable's reference. It does not delete the list because other still refers to it.

Important: del removes a name or reference; it does not necessarily destroy the object immediately.

10. Garbage Collection

What is Garbage Collection?

Garbage collection is a process that identifies and reclaims memory occupied by objects that are no longer needed.

In CPython:

Reference counting handles many objects when their reference counts reach zero.

A cyclic garbage collector detects certain groups of objects that refer to one another but are no longer reachable from the program.

10.1 Simple Example

numbers = [10, 20, 30]

numbers = None

print(numbers)

Output:

None

The variable now refers to None. If the original list has no other references, it can be reclaimed.

10.2 Circular References

Two objects can refer to each other, creating a cycle.

class Item:
    pass


a = Item()
b = Item()

a.other = b
b.other = a

del a
del b

The objects refer to one another, even after the variables a and b are deleted.

In CPython, the cyclic garbage collector can detect and reclaim unreachable cycles such as this one.

10.3 The gc Module

Python provides the gc module to inspect and manage cyclic garbage collection.

import gc

print(gc.isenabled())

This reports whether automatic cyclic garbage collection is enabled.

You can request a collection:

import gc

collected = gc.collect()

print("Collected objects:", collected)

gc.collect() requests a collection and returns the number of objects collected in that run. The result depends on the objects present and the Python implementation.

Reference Counting vs Garbage Collection

Reference Counting

Garbage Collection

Tracks references to objects

Detects unreachable cycles

Can reclaim objects when the count reaches zero

Can reclaim cyclic groups that reference counting alone cannot reclaim

Used by CPython as a primary mechanism

Complements reference counting in CPython

Often acts immediately when the last reference disappears

Collection timing can vary

11. Stack and Heap Memory

Stack Memory

The call stack tracks active function calls and their execution frames.

For example, it helps Python keep track of which function is running and where to return when the function finishes.

Heap Memory

Python objects, such as lists, dictionaries, strings, and instances of classes, are generally allocated in managed memory on the heap.

Example

def display():
    name = "Shivani"
    numbers = [10, 20, 30]

    print(name)
    print(numbers)


display()

Output:

Shivani
[10, 20, 30]

Explanation

The function call creates an execution frame.

The local names name and numbers belong to that frame.

They refer to Python objects.

When the function returns, its frame is released, but an object can remain alive if a reference to it exists elsewhere.

Important Note

It is an oversimplification to say that every local variable is stored directly on the stack and every object is always stored on the heap. The details depend on the Python implementation and runtime optimizations.

12. Shallow Copy vs Deep Copy

What is Copying?

Copying creates another object based on an existing object.

Python provides two common copying approaches:

Shallow copy

Deep copy

They behave differently when the original object contains other mutable objects, such as nested lists or dictionaries.

12.1 Shallow Copy

A shallow copy creates a new outer object but keeps references to the original object's nested elements.

For a nested list, the outer list is new, but its inner lists are shared.

Example

import copy

original = [[10, 20], [30, 40]]

shallow = copy.copy(original)

print("Original:", original)
print("Shallow:", shallow)
print(original is shallow)
print(original[0] is shallow[0])

Output:

Original: [[10, 20], [30, 40]]
Shallow: [[10, 20], [30, 40]]
False
True

Explanation

original and shallow are different outer lists.

original[0] and shallow[0] refer to the same inner list.

Therefore, changing a shared inner list affects both outer lists.

Example: Modifying a Nested Element

import copy

original = [[10, 20], [30, 40]]

shallow = copy.copy(original)

shallow[0].append(50)

print("Original:", original)
print("Shallow:", shallow)

Output:

Original: [[10, 20, 50], [30, 40]]
Shallow: [[10, 20, 50], [30, 40]]

Why Did Both Change?

Because original[0] and shallow[0] refer to the same inner list.

Appending 50 modifies that shared list.

Another Shallow Copy Example

import copy

original = [10, 20, 30]

shallow = copy.copy(original)

shallow.append(40)

print(original)
print(shallow)

Output:

[10, 20, 30]
[10, 20, 30, 40]

Here, the lists are independent because their elements are immutable integers. Appending to the outer copy does not change the original outer list.

12.2 Deep Copy

A deep copy creates a new outer object and recursively copies nested objects as well, subject to the behavior of the objects being copied.

The copy.deepcopy() function is used for deep copying.

Example

import copy

original = [[10, 20], [30, 40]]

deep = copy.deepcopy(original)

print("Original:", original)
print("Deep:", deep)
print(original is deep)
print(original[0] is deep[0])

Output:

Original: [[10, 20], [30, 40]]
Deep: [[10, 20], [30, 40]]
False
False

Explanation

original and deep are different outer lists.

Their nested lists are also separate objects.

Changes to a nested list in the deep copy do not affect the original.

Example: Modifying a Nested Element

import copy

original = [[10, 20], [30, 40]]

deep = copy.deepcopy(original)

deep[0].append(50)

print("Original:", original)
print("Deep:", deep)

Output:

Original: [[10, 20], [30, 40]]
Deep: [[10, 20, 50], [30, 40]]

Only the deep copy changes.

12.3 Difference Between Shallow Copy and Deep Copy

Shallow Copy

Deep Copy

Creates a new outer object

Creates a new outer object

Shares references to nested objects

Recursively copies nested objects where applicable

Nested mutable changes may affect both copies

Nested mutable changes are generally independent

Often less expensive

Can use more time and memory

Created using copy.copy()

Created using copy.deepcopy()

12.4 Copying with List Slicing

For a list, slicing can create a shallow copy.

original = [10, 20, 30]

new_list = original[:]

new_list.append(40)

print(original)
print(new_list)

Output:

[10, 20, 30]
[10, 20, 30, 40]

The outer lists are independent, but nested objects would still be shared.

12.5 Copying with list.copy()

original = [10, 20, 30]

new_list = original.copy()

new_list.append(40)

print(original)
print(new_list)

Output:

[10, 20, 30]
[10, 20, 30, 40]

The list.copy() method creates a shallow copy.

12.6 Real-World Example: Employee Data

import copy

employee = {
    "name": "Shivani",
    "skills": ["Python", "SQL"]
}

shallow = copy.copy(employee)
deep = copy.deepcopy(employee)

shallow["skills"].append("Machine Learning")

print("Original:", employee)
print("Shallow:", shallow)
print("Deep:", deep)

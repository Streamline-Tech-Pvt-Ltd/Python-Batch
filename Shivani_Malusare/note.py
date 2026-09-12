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


# 11/06/2026

# Variables in python

# Variables
 # A variable is a name used to store data in a program.
 # Ex:.name = "Urmila"
  #    age = 20
      
# Variables Rules

# Rule 1:Variable name must start with a letter (A-Z, a-z) or underscore (_)
name = "Urmila"
print(name)

_name="Urmila"
print(_name)

# Rule 2:Variable name cannot start with a number
 # Ex: Invalid
     # 2Name = "Urmila" 
      #Correct
name2 = "Urmila"
print(name2)

 # Rule 3:Special characters are not allowed
  # Ex: Invalid     
       # student@name = "Urmila"
      
# Rule 4:Variable names are case-sensitive
name = "Urmila"
Name = "Said"
print(Name) # Said
print(name) # Urmila

# Rule 5:Spaces are not allowed
  # Ex:Invalid
     # my name = "Urmila"
     # print(my name)
    # Correct
my_name = "Urmila"
print(my_name)

# Rule 6:Keywords cannot be used as variable names
  # Ex:Invalid
    # if = "Urmila"
    # print(if)
   # Correct
student_name = "Urmila"
print(student_name)



# Naming Conventions (Cases)
 # Naming conventions are rules for writing variable, function, class, and constant names in a readable format.

# 1.snake_case (recommended variables & function)
 # All letters are lowercase & Words are separated by underscores (_).
student_name = "Urmila"

# 2.camelCase 
# First word starts with a lowercase letter & Next word start with uppercase letter. 
studentName = "Urmila"

# 3.PascalCase (use for classes)
 # Every word starts with a capital letter.
class StudentDetails:

# 4.UPPER_CASE (used for constants)
# All letters are capital & Words are separated by underscores.
 MAX_SIZE = 100



# Keywords
 # Keywords are reserved words in Python that have special meanings and predefined functions.They cannot be used as variable names, function names, or class names.
 # Ex: if, else, for, while, True, False, class, def, return.

# Python keywords
 import keyword 
 print(keyword.kwlist)
 '''['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
  'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']'''



# f-string in python
 # An f-string (formatted string) is used to insert variables or expressions directly inside a string using {} brackets.

  # Syntax:f"string {variable}"
   
name = "Urmila"
age = 20
print(f"My name is {name} and I am {age} years old.")
  # Output:My name is Urmila and I am 20 years old.

 

# Input function in python
#   The input() function is used to take input from the user through the keyboard.

#  * Syntax: input("Message")
name = input("Enter your name: ")
print("Hello", name)
         # O/P : Enter your name: Urmila
              #  Hello Urmila
     
age = int(input("Enter your age: "))
print("Age =", age)
    # O/P:Enter your age: 20
        # Age = 20

# Important Notes
 # The input() function always returns data as a string.

num = input("Enter a number: ")
print(type(num))
  #  O/P: <class 'str'>  
# File Handling
# File Handling is the process of creating, reading, writing, updating, and deleting files

# | Mode | Meaning       | File Exists | File Doesn't Exist |
# | ---- | ------------- | ----------- | ------------------ |
# | r    | Read          | Opens       | Error              |
# | w    | Write         | Overwrites  | Creates            |
# | a    | Append        | Adds data   | Creates            |
# | x    | Create        | Error       | Creates            |
# | r+   | Read + Write  | Opens       | Error              |
# | w+   | Read + Write  | Overwrites  | Creates            |
# | a+   | Read + Append | Opens       | Creates            |



# 1. Read Mode (r)
# file = open("book.txt","x")
# file.close()
# Used to read existing file.

# file = open("Student.txt","r")
# print(file.read())
# file.close()
# If file doesn't exist
# FileNotFoundError

# create to a file
# with open("sample.txt", "x") as file:
#     file.close()


# 2. Write Mode (w)
# Creates new file.
# If file already exists, all old data is deleted.

# file = open("demo.txt", "w")
# file.write("Hello Python")
# file.close()

# with open("demo.txt","w") as file:
#     file.write("pallavi")
    

# 3. Append Mode (a)
# Adds new data at the end.
# Old data remains.
file = open("student.txt", "a")
file.write("\nWelcome")
file.close()

with open("demo.txt","a")as file:
    file.write("\nHi this Pallavi")
# 4. Create Mode (x)
# Creates file only if it doesn't exist.
# file = open("demo.txt", "x")        

# If file already exists
# FileExistsError


# Reading from a file
with open("sample.txt", "r") as file:
    f1 = file.read()
    print(f1)
    

with open("student.txt", "r") as file:
    (file.read())

# **readline()
# Reads one line.
file = open("student.txt", "r")
print(file.readline())
file.close()


# File
# Python
# Java
# C++

# Output
# Python

# readlines()
# Returns list of all lines.
file = open("student.txt", "r")
print(file.readlines())
file.close()
# Output
# ['Python\n', 'Java\n', 'C++']
file = open("student.txt","r+")
file.write("\n hi")
file.close()

# =====================================================================

# Replace concept
# file = open("replace.txt","x")
# file.close()

# file =open("replace.txt","r")
# f1 =file.read()
# print(f1)
# file.close()
# f1 = f1.replace("Pallavi","Pallu")
# print(f1)
# file = open("replace.txt","w")
# file.write(f1)
# file.close()


with open("replace.txt","r") as file:
    f1 =file.read()
    f1 = f1.replace("Pallavi","Pallu")
with open("replace.txt","w") as file:
    file.write(f1)

    




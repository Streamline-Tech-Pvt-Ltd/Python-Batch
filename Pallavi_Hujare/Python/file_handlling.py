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

file = open("Student.txt","r")
print(file.read())
file.close()
# If file doesn't exist
# FileNotFoundError


# 2. Write Mode (w)
# Creates new file.
# If file already exists, all old data is deleted.

file = open("student.txt", "w")
file.write("Hello Python")
file.close()

# 3. Append Mode (a)
# Adds new data at the end.
# Old data remains.
file = open("student.txt", "a")
file.write("\nWelcome")
file.close()

# 4. Create Mode (x)
# Creates file only if it doesn't exist.
# file = open("demo.txt", "x")        

# If file already exists
# FileExistsError

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
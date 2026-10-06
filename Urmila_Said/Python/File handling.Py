# File Handling
# File Handling is the process of creating, opening, reading, writing, 
# updating, and deleting files using Python.

# Types of files
#1.text files(.txt) : These files store readable text.

#2.Binary files(.jpg,.pdf): These store data in binary format.


#1.Create Mode (x): Creates a new file.
# file = open("student.txt","x")

# #2.write Mode(w) : File create and write at a time
# file = open("student.txt","w")
# file.write("Hello Python")
# file.close()

# #3.Append Mode(a) :Adds new data at the end of the file.
# file = open("student.txt","a")
# file.write("\n Urmila")
# file.close()

# #4. Read Mode(r) :Reads the complete file.
# file = open("student.txt","r")
# print(file.read())
# file.close()

#readline(): Reads one line at a time.
# file = open("student.txt","r")
# print(file.readline())
# print(file.readline())
# file.close()

#readlines(): Reads all lines into a list.
# file = open("student.txt","r")
# print(file.readlines())
# file.close()

#5 Read and Write Mode (r+): Can read and write.
# file = open("student.txt","r+")
# print(file.read())
# file.write("\nI am a fullstack developer")
# file.close()

#6 write and read(w+): Deletes old data
# file = open("student.txt","w+")
# file.write("Hello")
# print(file.read())
# file.close()

#remove(): Deletes a file
# import os
# os.remove("student.txt")

# With use
# with open("Student.txt","r") as file:
#     file.read()


# replace(): repalce the file exit value

file = open("Student.txt","w")
file.write("Urmila Said")
file.close()

file = open("Student.txt","r")
data = file.read()
file.close()

data = data.replace("Said","Hujare")

file = open("Student.txt","w")
data = file.write(data)
file.close()







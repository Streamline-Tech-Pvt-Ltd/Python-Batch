# File Handling
# File Handling is the process of creating, opening, reading, writing, 
# updating, and deleting files using Python.

# Types of files
#1.text files(.txt) : These files store readable text.

#2.Binary giles(.jpg,.pdf): These store data in binary format.


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

#4 readline(): Reads one line at a time.
# file = open("student.txt","r")
# print(file.readline())
# print(file.readline())
# file.close()

#5 readlines(): Reads all lines into a list.
# file = open("student.txt","r")
# print(file.readlines())
# file.close()

#6 Read and Write Mode (r+): Can read and write.
# file = open("student.txt","r+")
# print(file.read())
# file.write("\nI am a fullstack developer")
# file.close()




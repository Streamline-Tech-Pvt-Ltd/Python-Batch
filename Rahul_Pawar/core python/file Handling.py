# File Handling:
    #  it is used to create,read,write,and modify files in python

#   function:
            #   1)open() : open file or notebook
            #   2)write():write in a file or notebook
            #   3)read() :read a file or notebook
            #   4)close():close a file or notebook


# function use in file handling(mode):

# r = read
# w = write
# a = append
# \n = new line 
# \t = tab 
# x = create and exit File 
# r+ = read and write
# w+ = write and read
# a+ = append and read

# use for image and video files:

# rb = read binary
# wb = write binary

# example:
# syntax: file = open("filename","mode")
# file = open("data.txt","r")

# file = open("data.txt","r")
# print(file.read())
# file.close()


# ex:

with open("demo.txt","w") as file:
    file.write("Hello python")
    
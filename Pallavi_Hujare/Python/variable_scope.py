# Types of variable: 
# 1. Local variable: Local vairable is used inside a function.
# def my_fun():
#     name = "Sai" #local variable
#     print(name)
# my_fun()


# 2. Global variable : Global variable is used outside a function.
# print(name) #outside a function not work
# name = "Pallavi" # global variable
# def my_fun():
#     print(name)
# my_fun()
# print(name)

# global keyword:

# Stu_name = "Pallavi"
# def change():
#     global Stu_name
#     name = "Urmila"
#     print(name)
# change()
# print(Stu_name)


# Practice question:
# 1. Create a local variable inside a function and print it.

def info():
    stream = "BSC CS" 
    print(stream)
info()

# 2. Create a global variable and print it inside and outside the function.
stream = "BSC CS"
def info():
    print(stream)
info()
print(stream)


# 3. Create a program using the global keyword to update a variable.
stream = "BSc CS"
def update_stream():
    global stream
    stream = "MCA"
print("Before :", stream)
update_stream()
print("After Update:", stream)

# 4. Create local and global variables with the same name and observe the output.
stream = "BSC CS"
def info():
    stream = "MCA"
    print(stream)
info()
print(stream)  #MCA
              #BSC CS


# 5. Create a counter program using a global variable.
count = 0
def counter():
    global count
    count = count + 1
    print("count is:", count)

counter()
counter()
counter()
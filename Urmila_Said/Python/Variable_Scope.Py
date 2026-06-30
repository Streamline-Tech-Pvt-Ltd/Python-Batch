# Types of variable: 
# 1. Local variable: A local variable is declared inside a function and can be used only within that function.

# def my_fun():

#     name = "Sai" #local variable

#     print(name)
# my_fun()
# print(name) #outside a function not work


# 2. Global variable : A global variable is declared outside all functions and can be accessed throughout the program.

# name = "Pallavi" # global variable

# def my_fun():

#     print(name)

# my_fun()
# print(name)


# global keyword:The global keyword is used inside a function to modify a global variable.
# if you assign a value to a variable inside a function, Python treats it as a local variable.
# By using the global keyword, Python knows you want to use the global variable instead.

# Stu_name = "Pallavi"
# def change():
#     global Stu_name

#     name = "Urmila"

#     print(name)
    
# change()

# print(Stu_name)


# Practice question:
# 1. Create a local variable inside a function and print it.
# def my_fun():
#     name = "Urmila"
#     print(name)
# my_fun()


# 2. Create a global variable and print it inside and outside the function.
# name = "Urmila"
# def my_fun():
#     name = "Urmila"
#     print(name)
# my_fun()
# print(name)    

# 3. Create a program using the global keyword to update a variable.
# num = 10 
# def update():
#     global num
#     num = num + 5
# update()
# print(num)

# 4. Create local and global variables with the same name and observe the output.
# name = "Urmila"
# def my_fun():
#     name = "Urmila"
#     name = "Urmila"
#     print(name)
# my_fun()
# print(name)

# O/P: Urmila
#      Urmila

# 5. Create a counter program using a global variable.
count = 0
def counter():
    global count
    count += 1
    print(count)

counter()
counter()

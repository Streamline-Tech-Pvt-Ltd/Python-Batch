print("$$$$$$$$$$$$$$  File Handling in Python  $$$$$$$$$$$$$$$$$$$")
print("---------------------------------------------------")
# # 1. Creating A file:-

# file = open("C:\\Users\\Akshada\\Desktop\\streamline tech\\Python-Batch\\Anuj_Kakad\\Back-End\\python\\Demo.txt", "x")
# print("File Created Successfully")
# file.close()

print("---------------------------------------------------")
# 2. Writing Data into a file:-

file = open("C:\\Users\\Akshada\\Desktop\\streamline tech\\Python-Batch\\Anuj_Kakad\\Back-End\\python\\Demo.txt", "w")
file.write("Hello, World!")
print("Data Written Successfully")
file.close()

print("---------------------------------------------------")
# 3. Reading Data from a file:-

file =open("C:\\Users\\Akshada\\Desktop\\streamline tech\\Python-Batch\\Anuj_Kakad\\Back-End\\python\\Demo.txt", "r")
data = file.read()
print("Data Read Successfully")
print("Data in the file is:", data)
file.close()

print("---------------------------------------------------")
# 4. Appending Data into a file:-

file = open("C:\\Users\\Akshada\\Desktop\\streamline tech\\Python-Batch\\Anuj_Kakad\\Back-End\\python\\Demo.txt", "a")
file.write("\nHello From Anuj Kakad")
file.write("\nHow are you doing today?")
print("Data Appended Successfully")
file.close()

print("---------------------------------------------------")
# 5. Reading Data from a file after appending:-

file = open("C:\\Users\\Akshada\\Desktop\\streamline tech\\Python-Batch\\Anuj_Kakad\\Back-End\\python\\Demo.txt", "r")
data = file.read()
print("Data Read Successfully")
print("Data in the file is:", data)
file.close()

print("---------------------------------------------------")
# 6. read and write data into a file:-

file = open("C:\\Users\\Akshada\\Desktop\\streamline tech\\Python-Batch\\Anuj_Kakad\\Back-End\\python\\Demo.txt", "r+")
data = file.read()
print("Data Read Successfully")
print("Data in the file is:-", data)
file.write("\nAre you doing good?")
print("Data Written Successfully")
file.close()

print("---------------------------------------------------")
file = open("C:\\Users\\Akshada\\Desktop\\streamline tech\\Python-Batch\\Anuj_Kakad\\Back-End\\python\\Demo.txt", "r")
data = file.read()
print("Data Read Successfully")
print("Data in the file is:-", data)
file.close()

print("---------------------------------------------------")
file = open("C:\\Users\\Akshada\\Desktop\\streamline tech\\Python-Batch\\Anuj_Kakad\\Back-End\\python\\Demo.txt", "r")
data = file.readline()
print("Data Read Successfully")
print("Data in the file is:-", data)
file.close()

print("---------------------------------------------------")
file = open("C:\\Users\\Akshada\\Desktop\\streamline tech\\Python-Batch\\Anuj_Kakad\\Back-End\\python\\Demo.txt", "r")
data = file.readlines()
print("Data Read Successfully")
print("Data in the file is:-", data)
file.close()
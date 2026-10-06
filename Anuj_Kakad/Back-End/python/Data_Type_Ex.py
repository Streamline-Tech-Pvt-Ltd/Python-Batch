print("List Methods in Python:-")

num = [10, 50, 30, 40, 20, 70]

print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(type(num))

# Essential List Methods in Python:-

# Adding Elements
num.append(60)  # Adds an element to the end
print(num)
num.insert(2, 25)  # Inserts an element at a specific index
print(num)
num.extend([70, 80])  # Adds multiple elements to the end
print(num)

# Removing elements:-

num.remove(30)  # Removes the first occurrence of a value
print(num)

num.pop(4)  # Removes an element at a specific index
print(num)

num.clear()  # Removes all elements from the list
print(num)

# Sorting & Utility Functions:-

num = [10, 50, 30, 40, 20, 70]

num.sort()  # Sorts the list in ascending order
print(num)

num.reverse()  # Reverses the order of elements in the list
print(num)

print(num.count(70))  # Counts the occurrences of a value in the list

print(num.index(50))  # Returns the index of the first occurrence of a value

num.sort(reverse=True)
print(num)

num1 = num.copy()  # Creates a shallow copy of the list
print(num1)



print()
print("String Methods in Python:-")

# String Methods

# 1. capitalize() - Capitalizes the first character of the string

str = "anuj kakad"
print(str.capitalize())

#2. casefold() - Converts the string to lowercase

str = "ANUJ KAKAD"
print(str.casefold())

#3. index() - Returns the index of the first occurrence of a substring

str = "anuj kakad"
print(str.index("kakad"))

#4. count() - Returns the number of occurrences of a substring

str = "anuj kakad"
print(str.count("a"))

#5. find() - Returns the index of the first occurrence of a substring, or -1 if not found

str = "India is my country"
print(str.find("my"))

#6. isalpha() - Checks if all characters in the string are alphabetic

str = "anujkakad"
print(str.isalpha())

str = "anuj kakad"
print(str.isalpha())

str = "anuj123"
print(str.isalpha())

#7. isalnum() - Checks if all characters in the string are alphanumeric

str = "anujkakad123"
print(str.isalnum())

str = "anuj kakad"
print(str.isalnum())

str = "anuj@123"
print(str.isalnum())

str = "123456"
print(str.isalnum())

#8. center() - Centers the string within a specified width

str = "anuj kakad"
print(str.center(40, "*"))

#9. zfill() - Pads the string with zeros on the left to fill a specified width

str = "anuj kakad"
print(str.zfill(20))

#10. startswith() - Checks if the string starts with a specified prefix

str = "anuj kakad"
print(str.startswith("anuj"))

#11. endswith() - Checks if the string ends with a specified suffix

str = "anuj kakad"
print(str.endswith("kakad"))


print()
print("Indexing And Slicing of Lists in Python:-")
list = ["apple", "banana", "cherry", "date", 30, 40, 50, 60, 70]


print(list[0])
print(list[3][2])
print(list[-1])
print(list[1][4])
print(list[2:6])
print(list[0:9:2])
print(list[::3])
print(list[-5:-1])
print(list[:-1])
print(list[::-1])
print(list[-7][-4])

print()
print("Indexing And Slicing of Nested Lists in Python:-")
l1 = [1,2,3,[7,3],[3,8],4,5] 

print(l1[3][0], l1[3][1])
print(l1[3][0:2])
print(l1[-4][0:2])



print()
print("Indexing And Slicing of Strings in Python:-")
str = "india is my country"

print(str[1:8])
print(str[2:12:2])
print(str[::])
print(str[::-1])
print(str[-1])
print(str[:-1])
print(str[9][-1])
print(str[12])
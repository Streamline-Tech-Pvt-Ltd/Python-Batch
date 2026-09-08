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

# num.clear()  # Removes all elements from the list
# print(num)

# Sorting & Utility Functions:-

num.sort()  # Sorts the list in ascending order
print(num)

num.reverse()  # Reverses the order of elements in the list
print(num)

num.count(70)  # Counts the occurrences of a value in the list
print(num)

num.index(50)  # Returns the index of the first occurrence of a value
print(num)
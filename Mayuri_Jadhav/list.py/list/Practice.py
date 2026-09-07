#List

#1 append.
fruits = ["Apple","orange","mango"]
fruits.append("Banana")
print(fruits)


fruits = ["Apple","orange","mango"]
print(type(fruits))

#remove.
fruits = ["Apple","orange","mango"]
fruits.remove("mango")
print(fruits)

# insert.
fruits = ["Apple", "Mango", "Banana"]
fruits.insert(2,"orange")
print(fruits)

#pop
fruits = ["Apple","orange","mango"]
fruits.pop(1)
print(fruits)

# delete 
fruits = ["Apple","orange","mango"]
del fruits[1]
print(fruits)

#extend
fruits = ["Apple","orange","mango"]
fruits.extend(["apple","orange","mango"])
print(fruits)

#sort
fruits = ["Apple","orange","mango"]
fruits.sort()
print(fruits)

#count
fruits = ["Apple","orange","mango"]
print(fruits.count("orange"))

#reverse

fruits = ["Apple","orange","mango"]
fruits.reverse()
print(fruits)

#copy
fruits = ["Apple","orange","mango"]
new_fruits=fruits.copy()
print(new_fruits)
print(type(new_fruits))
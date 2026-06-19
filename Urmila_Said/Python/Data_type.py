 # Data Types:data types are used store different type of data in a variable.

 # Numeric data type:int,float,complex

 #int
 num = 10
 print(type(num))

 #float
 a = 15.5
 print(type(a))

 #complex
 c = 4 + 5j
 print(type(c))

 

 #boolean data type:bool
 isplaced = True
 print(type(isplaced))

# isplaced = False
 print(type(isplaced))

 #Type function:Type() function is used to check the data type of the variable.

 #Id function:Id() Function is used to check the memory address of a variable.

 num1 = 103
 print(id(num1))

 num2 = 103
 print(id(num2))

 #Task 1

 print("Product Information")
 product_name = "Powder"
 product_id = 102
 product_category = "makeup"
 product_prize = 10

 print(f"Product Name:{product_name},\nProduct ID: {product_id},\nProduct Category:{product_category},\nProduct Price: {product_prize}")

  product_name = "Powder"
  print(type(product_name))

  product_id = 102
 print(type(product_id))

 product_category = "makeup"
 print(type(product_category))

 product_prize = 10
 print(type(product_prize))

# # Task 2

 print("Product Information")
 product_name = "Rice"
 product_id = 10
 product_category = "Food"
 product_prize = 100
 print("Product Name:", product_name,
       "\nProduct Id:" , product_id,
      "\nProduct Prize:" , product_prize,
       "\nProduct Category:" , product_category)

 print(type(product_name))
 print(type(product_id))
 print(type(product_category))
 print(type(product_prize))


# Sequence Data Types
# 1.List : List is a comma separated by elements within a square brakets[].
Ex:[1,2,3,4,5]
 
 # List is a collection of items which are ordered and changeable.
 # 1.list is a mutable it can be changed
 # 2.list is order. it means the order of the elements is preserved.
 # 3.It alllows duplicate members.

 # List Operations
 # List Operations are actions that can be performed on lists, such as adding, removing, updating, searching, and combining elements.
# 1.Creating the list
fruits = ["Apple","Mango","Banana"]
print(fruits)
 
# 2.Accessing Elements
print(fruits[0])
print(fruits[2])

# 3.Updating Elements
fruits[1] = "Orange"
print(fruits)

# 4.Adding Elements
# append()
# adds an element at the end.
fruits.append("Banana")
print(fruits)

# 5.insert()
# adds an element at a specific position.
fruits.insert(2,"orange")
print(fruits)

# 6. remove()
# remove a specific element.
fruits.remove("Banana")
print(fruits)

# 7. pop()
# Removes an element by index.
 fruits.pop(0)
 print(fruits)

# 8. delete()
# Delets on element or entire list.
del fruits[1]
print(fruits)

# 9. extend()
# Adds Multiple Elements.
fruits.extend(["Grape","Mango","Pineapple"])
print(fruits)

# 10.sort()
# method is used to arrange the elements of a list in ascending or descending order.
fruits.sort()
print(fruits)

# 11. reverse()
# method is used to reverse the order of elements in a list.
fruits.reverse()
print(fruits)

# 12.count()
# is used to count how many times a specific element appears in a list, tuple, or string.
print(fruits.count("Mango"))

# 13.copy()
# method is used to create a copy (duplicate) of a list.
new_fruits = fruits.copy()
print(fruits)




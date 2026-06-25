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



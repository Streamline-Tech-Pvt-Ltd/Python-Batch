#Data type
#Data types are used store different types of  data in a variable

#1.Numeric data type :int , float , complex

#a.Whole number without decimal point.
num=20
print(type(num))

#b.number with decimal point
num=10.2
print(type(num))

#c. Complex is Numbers with imeaginary part
c=3+2j
print(type(c))

#2. Sequence data types : list ,tuple ,string


#3. dictionary data type : dict


#4.set  data types : set


#5.boolean data types  : bool(true ,fales)
isPlaced =True
print(type(isPlaced))

# type() function:  type() function is uesd to check the data type of a variable.
# id () function: id() function is used to cheack the memory Address of a variable.


num=100
print(id(num))


#************ Task ***********#

print("####### Product information #######")

product_name = "oil"
p_id = 1
p_category = "grocery"
p_price = 1000.00

print(f" Product Name : {product_name},\n Product id:{p_id},\n Product category:{p_category},\n Product price:{p_price}")

print(type(product_name))
print(type(p_id))
print(type(p_category))
print(type(p_price))

print("\n")

product_name="ghee"
p_id=2
p_category="grocery"
p_price=3000

print(f" Product name : {product_name},\n Product id:{p_id},\n Product category:{p_category},\n Product price:{p_price}")

print(type(product_name))
print(type(p_id))
print(type(p_category))
print(type(p_price))

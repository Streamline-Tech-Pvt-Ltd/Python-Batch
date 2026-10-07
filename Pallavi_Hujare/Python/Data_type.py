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
#i]
# # list:- list is a comma seprated by elements within a square brakets.[]
# Ex:- [1,2,2,3,4,5]
        # 0,1,2,3,4
        #-4,-3,-2,-1


# list is a collection of items which are ordered and changeable.
# 1. list is mutable.it can be changed.
# 2. list is ordered.it means the order of the elements is preserved.
# 3. it allows duplicate members.

# Method	                Purpose

# append()           	Add one item at end
# extend()	        Add multiple items
# insert()	       Add item at specific index
# pop()	            Remove item by index
# remove()	         Remove item by value
# clear()	            Remove all items
# count()	            Count occurrences
# copy()	            Create copy of list
# sort()	             Sort list
# reverse()	         Reverse list order



l1 = [1,2,2,2,3,4,5]
print(l1)

l1.append(2)
print(l1)  #[1, 2, 2, 2, 3, 4, 5, 2]

l1.extend([6,7,8,9,10])
print(l1)    #[1, 2, 2, 2, 3, 4, 5, 2, 6, 7, 8, 9, 10]

l1.insert(2,0)
print(l1)    #[1, 2, 0, 2, 2, 3, 4, 5, 2, 6, 7, 8, 9, 10]

l1.pop(5)
print(l1)  #[1, 2, 0, 2, 2, 4, 5, 2, 6, 7, 8, 9, 10]

l1.clear()
print(l1)  #[ ]

l1 = [1,2,2,2,3,4,5]
print(l1)

l1.remove(5)
print(l1) #[1, 2, 2, 2, 3, 4]

print(l1.count(2))  #3

l1.copy()
print(l1) #[1, 2, 2, 2, 3, 4]

l2 = [1,2,20,4,5,2,10,9,7]

l2.sort()
print(l2) # [1, 2, 2, 4, 5, 7, 9, 10, 20]

l2.reverse()
print(l2)  # [20, 10, 9, 7, 5, 4, 2, 2, 1]


#Additional functions 
# index()            	Returns the index of a specified value
# len()	            Returns the number of elements in the list
# min()	            Returns the smallest element
# max()	            Returns the largest element
# sum()	            Returns the sum of all elements
# sorted()	        Returns a new sorted list without changing the original list
# del	                Deletes an element or entire list
# in	                Checks if an element exists in the list
# not in	            Checks if an element does not exist in the list


# Examples

l1 = [1,2,3,4,5]

#index()
print(l1.index(3))
# Output: 2

# len()
print(len(l1))
# Output: 5

# min()
print(min(l1))
# Output: 1

# max()
print(max(l1))
# Output: 5

# sum()
print(sum(l1))
# Output: 15


#ii]

# Tuple - Tuple is a collection of multiple data items in a simgle variable.
# Tuple is denoted by ()
#Tuple is immutable
#tuple is ordered

tuple1 = (1,2,3,4,5,6,7,"India","Pune",[1,2,3])
print(type(tuple))
print(tuple1[: : -1]) #reverse the tuple
print(tuple1[:]) # all tuple elements
print(len(tuple1))
print(tuple1[9][1])

#tuple methods
#1. index() - index() method is used to return the index of the first occurrence of the specified value.
tuple1 = (1,2,3,4,5,6,7,"India","Pune",[1,2,3])
print(tuple1.index("India"))

#2. concatenation - we can add one or more tuples

t1 = (1,2,3)
t2 = (4,5,6)
t = t1 + t2
print(t)

#3. repetition - we can repeat a tuple for a specified number of times using the * operator.
t3 = (1,2,3)
t4 = t3 * 2
print(t4)

t = t4 * 2
print(t)

#4. count() - count() method is used to count the number of occurrences of a specified value in a tuple.
tuple1 = (1,2,3,4,2,4,1,1,5,3,6)
print(tuple1.count(2))

#iii]
# string - String is represent a Seuqence of characters.
# string is denoted by " " or ''
#string is immutable 

#string Methods

#1. capitalize() - convert the first character of the string to uppercase.

name = "india is my country"
print(name.capitalize())

#2. casefold() - convert the string to lowercase.

name = "INDIA IS MY COUNTRY"
print(name.casefold())

#3.index() - return the index of the first occurrence of the specified value.
name = "india is my country"
print(len(name))
print(name.index("is"))


#len() function: len() function is used to check the length of a string.

#4.find()- return the index of the first occurrence of the specified value. if the value 
# is not found then its output is -1.

name = "india is my country"
print(name.find("my"))
print(name.find("My"))

#5. isalpha()- only alphabets do not allow numbers
#6. isalnum() - alphabets and numbers 
#do not allow space , special characters

str = "India"
print(str.isalpha())

str = "01"
print(str.isalpha())

str = "2345" 
print(str.isalnum())

str = "streamline" 
print(str.isalnum())

#7. center()- center() method is used to center align the string with the specified width and fill character.

str1 = "India"
print(str1.center(13, "*"))

#8. zfill() - zfill() method is used to fill the string with 0 until it reaches the specified width.
str2 = "India"
print(str2.zfill(7))

#9.count() - count() method is used to count the number of occurrences of a substring in a string.

str = "Maharashtra"
print(str.count("h"))

#10.startswith()- startswith() method is used to check if the string starts with the specified value.
str = "Maharashtra"
print(str.startswith("M"))

#11.endswith() - endswith() method is used to check if the string ends with the specified value.
str = "Maharashtra"
print(str.endswith("a"))




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

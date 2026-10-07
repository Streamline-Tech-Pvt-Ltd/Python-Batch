# 16/06/2026

# Sequence data Types
# 2. String: A String is a sequence of characters enclosed in quotes.
# string is denoted by " " or "
# String is immutable

# String Methods:
# 1. Capitallize():Converts the first character to uppercase.
text = "python programming"
print(text.capitalize())
# OUTPUT:Python programming

# 2.Casefold:-convert the string to lowercase.
name = "INDIA IS MY COUNTRY"
print(name.casefold())

# 3.index() - return the index of the first occurrence of the specified value.
name = "india is my country"
print(name.index("is"))

# len() function: len() function is used to check the length of a string.
print(len(name))

# 4.find()- return the index of the first occurrence of the specified value. if the value 
# is not found then its output is -1.
name = "india is my country"
print(name.find("my"))

#5. isalpha()- only alphabets do not allow numbers
str = "India"
print(str.isalpha())

#6.isalnum(): alphabets and numbers allow. do not allow space & special characters
str = "2345" 
print(str.isalnum())

str = "streamline" 
print(str.isalnum())

#7.center(): method is used to center align the string with the specified width and fill character.
str1 = "India"
print(str1.center(13, "*"))

#8. zfill(): zfill() method is used to fill the string with 0 until it reaches the specified width.
str2 = "India"
print(str2.zfill(7))

#9.count(): count() method is used to count the number of occurrences of a substring in a string.
str = "Maharashtra"
print(str.count("h"))

#10.startswith():method is used to check if the string starts with the specified value.
str = "Maharashtra"
print(str.startswith("M"))

#11.endswith(): method is used to check if the string ends with the specified value.
str = "Maharashtra"
print(str.endswith("a"))















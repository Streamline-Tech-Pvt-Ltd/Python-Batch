#string - String is represent a Seuqence of characters.
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


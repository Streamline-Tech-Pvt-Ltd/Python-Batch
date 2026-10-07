#Write a Python program to take a  word from the user and check whether it is a Palindrome or not.
name=input("Enter a word:")
if name==name[::-1]:
    print("the word is palindrome")
else:
    print("the word is not palindrome")

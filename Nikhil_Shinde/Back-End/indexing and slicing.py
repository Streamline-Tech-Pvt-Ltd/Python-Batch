# indexing & slicing

#indexing :- indexing means accessing a single element using itd position number.

# index always starts from 0.
# text = "Python"
# print(text[0])   --- P
# print(text[3])   --- h

# negative index starts from the end.
# print(text[-1])   --- n
# print(text[-2])   --- o


# positive index --- left to right
# negative index --- right to left



# Slicing :- Slicing is used to get multiple element.

# syntax :- 
#        sequence[start : stop : step]
# Start :- starting index
# Stop :- stopping index
# Step :- jump value

#Ex:-
# text :"Python"
# print(text[0:4])   --- pyth
# print(text[2:6])   --- thon
# print(text[:4])   --- pyth
# print(text[2:])   --- thon

# using step :-
# print(text[0 : 6 : 2]) ---- pto

# Reverse String :-
# print (text[::-1])  ---- nohtyP


# Example with list:-

#num = [10,20,30,40,50]
#print(num[1]) ---- 20
#print(num[1:4])  ----[20,30,40]
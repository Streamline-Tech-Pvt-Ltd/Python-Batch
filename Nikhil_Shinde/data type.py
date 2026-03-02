# Collective Data Type:-
#       Collective data types stores multiple values in a single variable.


# there are two types:-
#                      1)primitive
#                       2)non primitive/ collective

#    1)primitive :

#        a. int - store only integer/whole number (ex. a = 10)

#        b.float - store only float (ex.10.00)

#        c. string- store text (ex. name ="rahul")

#        d.boolean = store true or false

 
# list:-
#        it is denoted by squared bracket[].
#           comma seperated by value or element within [] is called list.

# Mutable:-
#        it can be changed after creation.

# Ordered:-
#        it maintain the ordered in which element are added.

# Indexed:-
#        Each element in list have index number which all you to access and modify the element by their index number.

# Duplicate:-
#        Duplicated are allowed.

# List1=[]  # Empty List

# l2=[11,22,33,44]

# Accessing single element in list
# print(l2[1])
# print(l2[-3])

# list=["Sanket","Rahul","Nikhil","Pramod"]
# print(list[2])

#l4=[11,"string",3.5]


# List Method:-

# 1) Append():-
#           using append function we can add ellement in last of the list.
# list1=[11,22,44,55]
# list1=list1+[10]
# list1.append(66)
# print(list1)


# 2) insert():-
#       using insert() function we can add element at perticular positon.
# list1=[11,22,44,55]
# list1.insert(2,33)
# print(list1)


# 3) Remove():-
# list1=[11,22,33,44]
# list1.remove(22)
# print(list1)

# 4) pop():-
# list1=[11,22,33,44]
# list1.pop()
# print(list1)

# 5) sort():-
# list1=[21,34,56,76,19,67,87]
# list1.sort()
# print(list1)

# 6) REVERSE():-
# list1.reverse()
# print(list1)

# 7) count():-
# list1=[11,22,33,22,54,67,22,44]
# num=list1.count(22)
# print(num)

# 8) len():-
# list1=[11,22,33,44]
# print(len(list1))

# list=[11,22,33,44,55,[22,33,[10,50,41],44,55],66,77]

# print(list[-3][-3][-1:-3])  
 
 
 

# Dictionary:-Dict{}
#   comma seperated by key value pair within curely bracket is called dict/dictionary.

# {"key":"value"}
# {"name":"Rahul",'age':21}

#mutable
# unorderd
# duplicates:key-it should be unique - dont allow

#value-must be duplicate - allow 
# indexed


Student={
    "name":"Nikhil",
    "age":21,
    "City":"Nashik",
    "Course":"ai"
}
#print(Student["age"])
#print(Student.get("City"))

#Student["age"]=22
#print(Student)

#Student.pop("age")
#print(Student)


#Dictionary method-
# 1 keys():-

#print(Student.keys())
#print(Student.values())
#print(Student.items())
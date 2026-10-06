#Q1. create a tuple of 5 student roll numbers.
r_no = (1,2,3,4,5,2,3)

#Q2. print the first and last roll number from the tuple.
print(r_no[0])
print(r_no[-1])

#Q3. find the length of the tuple.
print(len(r_no))

#Q4. check whether a specific roll number is exists in the tuple .
roll_no = 3
if roll_no in r_no:
    print("Roll number is exists in tuple.")
else:
    print("Roll number is not exist in tuple.")
    
#Q5. Count how many times a roll number appears in the tuple.
roll_no = 2
r_no.count(r_no)
print(roll_no)

#Q6.Convert the tuple into a list and modify one element.
list1 = list(r_no)
list1[5] = 10
print(list1)

#Q7.Concatenate two tuples of student names.
tuple1 = ("Pramod", "rushikesh", "saras")
tuple2 = ("rohan", "rahul", "yogesh")
tuple3 = tuple1 + tuple2
print(tuple3)

#Q8. Create a tuple of student grades and print them using a loop.
grades=("A","B","C","D","F")
for grade in grades:
    print(grade)
    
#Q9.Access a tuple element using index.
r_no = (1,2,3,4,5,2,3)
print(r_no[1])
print(r_no[3])

#Q10.Slice the tuple to print the first three elements.
print(r_no[0:2])
print(r_no[0:5])
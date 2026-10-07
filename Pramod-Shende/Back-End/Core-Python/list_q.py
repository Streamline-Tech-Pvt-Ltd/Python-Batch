# 1)Create a list of 5 student names and print the list.
students = ["Pramod", "Rushikesh", "Saras", "Yogesh", "Rahul"]
print(students)

# 2)Add a new student name to the existing list.
students.append("Rohan")
print(students)

# 3)Remove a specific student name from the list.
students.remove("Saras")
print(students)

# 4)Find the total number of students in the list.
students.count(students)
print(students)

# 5)Sort the student names in alphabetical order.
students.sort()
print(students)

# 6)Reverse the list of student names.
students.reverse()
print(students)

# 7)Check whether a particular student name exists in the list.
sname = "Rohan"
if sname in students:
    print("sname is exists in list.")
else:
    print("sname does not exist in list.")
    
# 8)Create a list of student marks and find the highest mark.
marks = [85, 90, 78, 92, 88]
highest = max(marks)
print("Highest mark is:", highest)

# 9)Replace one student name with another name in the list.
students[0] = "Pramod Shende"
print(students)

    
# 10)Count how many times a particular mark appears in the list.
mark = 90
mcount = marks.count(mark)
print("Mark", mark, "appears", mcount, "times in the list.")

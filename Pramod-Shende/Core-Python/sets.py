# 1)Create a set of student IDs.
stud_id = {101, 102, 103, 104, 105}
print(stud_id)

# 2)Add a new student ID to the set.
stud_id.add(106)
print(stud_id)

# 3)Remove a student ID from the set.
stud_id.remove(103)
print(stud_id)

# 4)Check whether a specific student ID exists in the set.
if 103 in stud_id:
    print("Student ID 103 exists in the set.")
else:
    print("Student ID 103 does not exist in the set.")

# 5)Find the total number of unique student IDs.
print("Total number of unique student IDs:", len(stud_id))

# 6)Create two sets representing two classes and find common students (intersection).
class_a = {101, 102, 103, 104, 105}
class_b = {104, 105, 106, 107, 108}
common_students = class_a.intersection(class_b)
print("Common students:", common_students)

# 7)Find students who are in Class A but not in Class B (difference).
diff_students = class_a.difference(class_b)
print("Students in Class A but not in Class B:", diff_students)

# 8)Combine two sets of students (union).
all_students = class_a.union(class_b)
print("All students:", all_students)

# 9)Remove all elements from the set.
stud_id.clear()
print("Student IDs after clearing:", stud_id)

# 10)Convert a list of student names into a set to remove duplicates.
snames = ["saras", "rushikesh", "rahul", "rohan", "yogesh", "saras", "rushikesh"]
unique_student_names = set(snames)
print("Unique student names:", unique_student_names)


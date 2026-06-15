# 15/06/2026
# Slicing: Slicing is used to access a range of a string, list, or tuple.It allows you to access multiple elements at one time.

# Syntax 
# sequence[start : stop : step]
# start → Starting index (included)
# stop → Ending index (Index it will stop before that number)
# step → Increment/decrement value (Number of position to move)

# Positive indexing  start from left to write.
# Negative indexing start from right to left

# Ex:
# 1. List = [10,20,30,40,50,60]

# print(List[1:3:1])
# print(List[1:4:2])
# print(List[1:6:4])

 List = [10,20,30,[40,50,60],70,80,90]
 
# print(List[3][0:3:2])
# print(List[4:7:2])
# print(List[1:6:6])

 print(List[-1:-10:-2])


 # List = [10,20,30,[40,50,[60,70,80],25,35,45],55,65,74]

# print(List[4][1:3:1])










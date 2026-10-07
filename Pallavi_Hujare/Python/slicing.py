#SLicing :- To access more then 1 element. used tio access a range of element of list.
            
 #i.e : list, tuple, string, etc.
 #Syntax : sequence[start:stop:step]
            #start → Index where the slice begins (inclusive). Defaults to 0 if omitted.
            # stop → Index where the slice ends (exclusive). Defaults to the length of the sequence if omitted.
            # step → Interval between elements. Defaults to 1. Can be negative for reverse slicing
 #Ex : 

l1 =[1,2,3,4,5,6,[7,8,9,10],11,12,13,14,15]
print(l1[6][1:4:2]) 
# Output: [8,10]


######### Practice ##########
l1 = [1,2,[3,4,5,6,7],8,9]
print(l1[2][0:5:2])
# Output: [3,5,7]

l1 = [10,20,[30,40,50,60],70,80]
print(l1[2][1:3:1])
# Output: [40,50]

l1 = [11,22,[33,44,55,66],77]
print(l1[-2][-1:-5:-1])
# Output: [66,55,44,33]

l1 = [100,200,[300,400,500,600,700],800]
print(l1[2][1:4:2])
# Output: [400,600]

l1 = [1,2,3,[4,5,6,7,8,9],10]
print(l1[3][1:4:1])
# Output: [5,6,7]


l1 = [5,10,15,[20,25,30],35]
print(l1[3][1:4])
# Output: [25,30]

l1 = [1,2,3,4,5,6,7,8,9,10]
print(l1[3:7:1])
# Output: [4,5,6,7]

l1 = [10,20,30,40,50,60,70,80]
print(l1[-1:-8:-2])
# Output: [80,60,40,20]

l1 = [11,22,33,[44,55,66],77]
result=[l1[1], l1[4]]
print(result)
# Output: [22,77]

l1 = [11,22,33,[44,55,66],77]
result=[l1[-1], l1[-4]]
print(result)
#output: [77,22]

l1 = [100,200,300,[400,500],600]
result=[l1[0], l1[4]]
print(result)
# Output: [100,600]

l1 = [5,10,15,[20,25,30],35]
result=[l1[0], l1[4]]
print(result)
# Output: [5,35]

l1 = [100,200,300,[400,500],600]
print([l1[0], l1[4]])
# Output: [100,600]


l1 = [100,200,[300,400,500,600,700],800]
print([l1[-1], l1[-3]])
# Output: [800,200]

l1 = [1,2,3,4,5,6,7,8,9]
print(l1[-1:-10:-2])
# Output: [9,7,5,3,1]

name = "Programming"
print(name[1:11:2])
# Output: "rgamn"

l1 = [1,2,3,4,5,6,7,8,9,10]
print(l1[-1:-10:-2])
# Output: [10,8,6,4,2]

print(l1[0:11:2])
#output: [1,3,5,7,9]

print(l1[-2:-11:-2])
#output :[9,7,5,3,1]

print(l1[1:11:2])
#output :[2,4,6,8,10]

l1 =[10, 20, 30, 40, 50]
print(l1[1:4:2])
#output : [20,40]

l1 =(100, 200, 300, 400, 500)
print(l1[2:5:1])

l1 = [10,20,30,[40,50,60,70],80,90]
print(l1[3][1], l1[4])
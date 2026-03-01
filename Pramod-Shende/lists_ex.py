
#multiple examples of accessing  element from different lists.

#1. accesing 3rd element 40 from 1st list
list1=[1,2,3,4,5,[10,20,[30,40],50,60],6,7]
print(list1[5][2][1])

#2. acccesing 3rd element 30
a = [10, 20, [30, 40, 50], 60]
print(a[2][0])

#3.acccesing 3rd element 4 from second list
b = [[1, 2], [3, 4], [5, 6]]
print(b[1][1])

#4. accesing 3rd element from 3rd list 300
c = [100, [200, [300, 400], 500], 600]
print(c[1][1][0])

#5. accessing 3rd element 30 from 1st list
d = [[10, 20, 30], 40, 50]
print(d[0][2])

#6.accessing 3rd element 6 from 2nd list
e = [1, [2, 3], [4, [5, 6]], 7]
print(e[2][1][1])

#7. accessing 3rd element 500 from 2nd list
f = [100, [200, [300, 400], 500], 600]
print(f[1][2])

#8. accessing 3rd element 9 from 3rd list
g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(g[2][2])

#9. accessing 3rd element 50 from 1st list
h = [10, 20, [30, 40, 50], 60]
print(h[2][2])

#10. accessing 3rd element 300 from 2nd list
i = [100, [200, [300, 400], 500], 600]
print(i[1][1][0])

#output
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# n =5
# for i in range(1,n=1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# ______________________________________________________
# n= 6
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

#______________________________________
# n = 5
# for i in range(1, n + 1):
#     for j in range(1, i):
#         print(" ", end=" ")
#     for k in range(1, n - i + 2):
#         print("*", end=" ")
#     print()

# * * * * * 
#   * * * * 
#     * * * 
#       * *
#         * 

#_________________________________________________
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

#___________________________________________
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(i):
            print("*", end=" ")
        print()

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *









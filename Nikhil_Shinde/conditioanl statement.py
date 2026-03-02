# if elif and else 

# 1) if :- The if statement runs a block of code only if the condition is True.

#age = 20

#if age >= 18:
#    print("You are eligible to vote")


# 2) if - else Statement
#        use else when you want to execute a diffrent block if the condition is false.

#age = 16

#if age >= 18:
#    print("You are eligible to vote")
#else:
#   print("You are not eligible to vote")


# 3) if-elif-else statement:-
#        use elif (else if) when you want to check multiple conditions.

#marks=int(input("Enter Your Marks :- "))

#if marks > 75:
#    print("Grade A")

#elif marks > 50:
#    print("Grade B")

#elif marks > 35:
#    print("Grade C")

#else:
#    print("Fail")



# Transfer Satement:- 
#        Transfer statement are used to change the normal flow of execution in loops or programs.
# break,continue and pass

# break:- Stops the loop completely
# continue :- skips current iteration
# pass :- Does nothing (placeholder)
 
# 1) break
# for i in range (1,6):
#   if i == 3:
#       break
#   print(i)     

#output :- 1
#          2

# 2) continue :-
# for i in range (1,6):
#   if i == 3:
#       continue
#   print(i)     

# output:-1
#         2
#         4
#         5


# 3) pass
# for i in range (1,4):
#   if i == 2:
#       pass
#   print(i)     

# output :-1
#          2
#          3
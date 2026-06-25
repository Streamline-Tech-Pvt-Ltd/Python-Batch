#Operator : used to perform operation of values and variable 

# ex- 
# a = 1
# b = 2
# print (a + b)

# here the a and b is operands(variable) , 1 and 2 is values
# + is a operator


# Types of operator:

# 1. Arithematic operator (+,-, ,/,%,*,//)
# 2.Assisgnment opeartor (=,+=, -=, *=,/=, and all arithmetic operators are used)
# 3.Comparison/Relational opeartor (==, !=, >, < ,>=, <=)
# 4.Logical operator (and,or,not)
# 5.Identity operator(is, is not)
# 6.Membership operator(in, not in)
# 7.Bitwise opeartor(&, |, ~, ^)



#1.Arithematic operator:(+,-, ,/,%,*,//)

# a) +  :For the addition

# a = 1
# b = 2
# print (a + b)


# b) -  :for the subtraction

# a = 10
# b = 2
# print (a - b)


# c) *  :for the multipication

# a = 10
# b = 2
# print (a * b)

#     **   : exponential  (find the power of the values)

# a = 2                                         
# b = 10                                      
# print(a ** b)
 
# or

# a = 2             
# print(a ** 3)






# d)  /  :division

# a = 10
# b = 2
# print (a / b)


# e)  %  :modulus (quotient)

# a = 10
# b = 2
# print (a % b)


# f) //  :floar division(reminder)

# a = 10
# b = 2
# print (a // b)




# 2.Assignment operator   (=,+=, -=, *=,/=, and all arithmetic operators are used)


# a) =  : assign value to a variable
# x = 10


# b) +=  :
# a = 1
# a += 10           (a = a + 10)
# print(a)



# c)  -=  :
# a = 10
# a -= 1
# print(a)       (a = a - 1)



# d)   *=     :
# a = 2
# a *= 10
# print(a)        (a = a*10)



# d)   /=     :
# a = 10
# a /= 2
# print(a)       # (a = a/10)



# 3.  Comparison/Relational opeartor (==, !=, >, < ,>=, <=)


# a) ==  :show to all variable values are equal
# if var are not equal show false otherwise true

# a = 10
# b = 10
# print(a == b)


#  b) !=  :show to all variable values are not equal
# if the values are equal show false otherwise show true

# a = 15
# b = 10
# print(a != b)

# c)   <  :show less than
# a = 10
# b = 12
# print(a < b)


# d)   >  :show greater than
# a = 15
# b = 12
# print(a > b)


# e)   <=  :less than equal to

# a = 15
# b = 19
# print(a <= b)


# f)   >=  :greater than equal to
# a = 15
# b = 100
# print(a <= b)



# 4.Logical operator (and,or,not)

# a) and :
# 
# a = 10
# b = 20
# print(a>=9 and b<=20)


# b) or :
# a = 10
# b = 20
# print(a>20 or b<=21)

# c) not :
# a = 10
# print(not a > 12 )



# 5.Identity operator(is, is not)

# a) is : it operator check to both variable refer to one object or not 

# a = 3
# b = a
# print(a is 3)


# b) is not : means both objects are different in memory
# (store variable value in different location so those are not same )

# a = [1,2,3]
# b = [1,2,3]
# print (a is not b)


# 6.Membership operator(in, not in)


# a)  in :

# number = [1,2,3,4]

# if 1 in number:
#     print("number is in a string")



# b)  not in :  

# number = [1,2,3,4]

# if 7 not in number:
#     print("number is not in a string")




# 7.Bitwise opeartor(&, |, ~, ^)

# a)  &  :and(use a truth table)

# a = 5         101
# b = 3         011
# print (a & b)


# b)  |  : or 
# a = 5         
# b = 3        
# print (a | b)
                #    (addition of all bits means 4+2+1 = 7)



# c)   ~   :negation

# a = 5
# print (~5)

# formula : -(a + 1)


# d)   ^  :xor  (if two bits are differ result get 1 and two bits are same result will be 0)

# a = 5         
# b = 3         
# print (a ^ b)
                # (answer is 6)

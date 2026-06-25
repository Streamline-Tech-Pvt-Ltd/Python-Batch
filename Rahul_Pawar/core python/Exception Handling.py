# Exception Handling:

        #   it is use to handle runtime errors so program does not crash and can continue executing
        #  exception means error occurs during program execution
            # example:division by zero , file not found , invalid input


    # there are two types of error :
                                #  syntax error
                                #  runtime error



 #  1) Syntax error:

    # means syntax of python are not followed while writing the program
    
    #    try:cod that might raise error an execution

               # num1 = input("Enter your num1 :")
               # num2 = input("Enter your num2 :")
               # print(num1/num2)    
                   
                               # TypeError: unsupported operand type(s) for /: 'str' and 'str'



    # try  :    code that might raise error an execution
    # except :  code that handle exception.
    # optional :- execute if no exception are occured
    # finally : execute regardless of execution.


# try:                 
#     num1 = eval(input("Enter your num1 :"))
#     num2 = input("Enter your num2 :")
#     x = num1/num2
#     print(x)
# except ZeroDivisionError:
#     print("can not divied by zero.")
# except TypeError:
#     print("you can't pass second value as 0")


# try :
#     amount = int(input("Enter your amout to withdraw :"))
#     balance = 40000

#     if amount > balance :
#         raise Exception("Insufficient balance")
#     else:
#         print("withdraw sucessfull")
    
# except Exception as e:
#     print("Error : ",e)
    
# finally:
#     print("Thank you visit again.")
    


#  Built in exception:
# 1 syntax errror 
# 2 ZeroDivisionError
# 3 TypeError
# 4 Value Error
# 5 KeyError
# 6 FileNotFound
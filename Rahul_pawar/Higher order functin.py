# Higher Order Function: 

             # function that work with other function

    #  Types :
                #  filter()
                #  map()
                #  reduce()



    #  1.Filter() :
     
        #  used to filter condition based on a condition

        #  example :

              # num = [1,2,3,4,5,6]
              # result = list(filter(lambda x:x%2 == 0,num))

             # print(result)


    #  2.map() :   used to apply function to every element of a list

             # example :

                  # num = [1,2,3] 
                  # result = list(map(lambda x:x + 5,num))
                  # print(result)



    #  3.reduce() :  reduce a list to a single value

           #  example :

              # from  functools import reduce
              # number = [1,2,3,4,5]

              # result = reduce(lambda a, b : a + b,number)
              # print(result)


                  # output : 15







# four types to import module :

        # import numpy as np

        # import keyword

        # from module_name import fun_name

        # from module_name import *  (* = all)
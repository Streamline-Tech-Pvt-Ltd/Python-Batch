# Argument :

        #  passed actual value or function

          # example :

           # def add (a,b):           //(a and b is parameter)
           #     print(a + b)

           # add (5,3)              //(5 and 3 is a arguments)

    #  types :  

            #  positional arg
            #  keyword arg
            #  default arg


    # 1. positional Argument : 

          # Values passed in the same order as parameter

            # example :
              # def student(name,age):
              #     print(name,age)
              # student("rahul",20)



    # 2. Keyword argument :

           # argument are passed with parameter name

           #  Example :

             # def student(name,age):
             #     print(name,age)
             # student(name="rahul",age=20)



   # 3. Default argument : 

           # a default value is given to parameter

        #  example :
 

           # def greet (name = 'user'):
           #     print ("hello",name)
           # greet()
           # greet("rahul")



# Arbitrary Arguments :

    #    use when do not known how many argument passed to a function


      #   type :

        #  Arbitrary Positional Argument
        #  Arbiratry Keyword Argument


    #   1. Arbitrary Positional Argument (*args) :

              # allow to function ton accept any number of positional argument
              # all values stored in tuple

            #   syntax :
                    #  def function_name(*args):
                        #code

       #  example:

             # def number(*num):
             #     print(num)

             # number(10,20,30,"rahul")


    #  2.Arbiratry Keyword Argument :

               # accept any number of keyword argument
               # are values are store in dictionary

            # syntax :

                    #  def function_name(**kwargs):
                        #code


            #  example :
                # def number(**num):
                #       print(num)

                # number(number=10,name="rahul")

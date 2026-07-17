#fucntional arguments: There are 5 types arguments:
    # example :

           # def add (a,b):           //(a and b is parameter)
           #     print(a + b)

           # add (5,3)              //(5 and 3 is a arguments)

    #  types :  

            #  positional arg
            #  keyword arg
            #  default arg


#  demo

# 1. Required argument:  # argument are passed with parameter name

# def fun(a,b):
#     return a + b
# print(fun(10,20))


# 2. Default argument:
# a default value is given to parameter

        #  example :
 
           # def greet (name = 'user'):
           #     print ("hello",name)
           # greet()
           # greet("rahul")

# def demo(name = "student"):
#     return ("Welcome", name)
# print(demo())
# print(demo("Neha"))



# 3. keyword argument: # argument are passed with parameter name

# def abc(name,age,city):
#     return name , age, city
# print(abc(age=21,city="Nahsik",name="Rahul"))


# 4. Variable length/Arbitrary agruments (*args):
 #    use when do not known how many argument passed to a function

      #   type :

        #  Arbitrary Positional Argument
        #  Arbiratry Keyword Argument


# def stud_marks(*args):
#     return args
# print(stud_marks(35,80,90,67))


# 5. Keyword arbitrary arguments (**kwargs):
  # accept any number of keyword argument
 # are values are store in dictionary

# syntax :

                    #  def function_name(**kwargs):
                        #code

# def stud(**kwargs):
#     return kwargs
# print(stud(name="Anu",age=23,city="Pune"))


    
# Scope :-

            # Scope is the area or region where a variable can be accessed.
            # Scope decides where a variable is visible and usable in a program.

       # Types :

                 # Local Scope
                 # Global Scope
                 # Built-in Scope
                 # Enclosing Scope



        # 1) Local Scope :

                   # Created inside a function
                   # Used only inside that function


           #  Example:

                # def my_function():
                #     x = 10     # local variable
                #     print(x)
                # my_function()


        # 2) Global Scope :

                # Declared outside the function
                # Used anywhere in the program

           # Example:

              # x = 20
              # def show():
              # print(x)

             # show()
             # print(x)

                  # Output:

                       # 20
                       # 20



       # 3) Built-in Scope :

               # Predefined names in Python that are always available.

           # Examples:

                      # print()
                      # len()
                      # type() etc.



        # 4) Enclosing Scope

                # Occurs in nested functions (function inside another function)

           # Example:

                # def outer():
                #     x = 30
                #     def inner():
                #         print(x)
                #     inner()
                # outer()

                  # Output: 30


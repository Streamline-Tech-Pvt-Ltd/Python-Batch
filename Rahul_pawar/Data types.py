# Data taypes :

#             -there are use to what kind of data are stores in variable
#             - there are two types :
#                                    1.Primitive 
#                                    2.Collective (non-primitive)



# 1.Primitive Data Type :

        # -store single simple value
 
     # types:  
             # int
             # float
             # complex
             # bool


    # a.int : store whole number
           
        #    ex. : a = 10
        #          b = 20

                
    # b.float : stores decimal number 
               
     #           ex.: a = 2.10 
          
   
    #  c.complex : store complex number

        #    ex:  3 + 2j

    #  d. bool : stores true or false
       
      #  ex:

        # a = [1,2,3]
        # b = [1,2,3]
        # print (a is not b)

          # otput : true



# 2. Collective (non-primitive) data types :-
                  
                #    stores multiple value or collection of data types


    # types :
             # string
             # list
             # dictionary
             # set 
             # frozenset
             # tuple  


    #  1.string : 

          #      -  sequence of character use to store text Data 
          #      -  written inside Quotes : ("_")   ('_')   ('''_''')
         
               #     - example : "this is a string "


    #  2.list()  : 

              # Ordered collection of elements that can be changed (mutable).
              # Denoted by square brackets [ ]
                 
                # example :
  
                    # l1 = [ ]        # empty list
                    # l2 = [10, 20, 30, 40]


              # Access single element using indexing.
              # Access multiple elements using slicing.


          # Properties :

                # Mutable – modify
                # Ordered
                # Duplicate
                # Indexed


         # Use Functions :

        # 1) append() – adding element at the end
                  # syntax : list_name.append(element)
        
            # Example:

             # list1 = [11, 22, 33, 44]
             # list1.append(66)
             # print(list1)

        
        #  2) insert() : add element in specific position in a list 
            # syntax : list_name.insert(index_position , element)

            #  example :
                   # list1 = [11, 22, 33, 44]
                   # list1.insert(2,55)
                   # print(list1)


        #  3) remove() : remove specific element without index
             # syntax : list_name.remove(element)
          

            # example :
               
              # list1 = [11, 22, 33, 44]
              # list1.remove(33)
              # print(list1)


        #  4) pop() :  remove specific element with index
                    # syntax : list_name.pop(index)


            # example :

              # list1 = [11, 22, 33, 44]
              # list1.pop(2)    
              # print(list1)


        #   5) sort() : arrange list element into asending order
                    # syntax : list_name.sort()

            #   example :

                  # list1 = [11,10,22,2,33,55,44]
                  # list1.sort()
                  # print(list1)

                     # output : [2, 10, 11, 22, 33, 44, 55]


        #   6)  reverse() :  reverse order of list element

                        # syntax : list_name.reverse()

            # example : 

                   # list1 = [11,10,22,2,33,55,44]
                   # list1.reverse()
                   # print(list1)


             # reverse with slicing :
    
             # list1 = [11,10,22,2,33,55,44]
             # list1 = list1[1:4][::-1]
             # print(list1)

              #   output : [11, 10, 22, 2, 33, 55, 44]


 
        #  7) count() :  hoe many times an element appear in a list 
                        #   syntax : print(list_name.count(element))

            # example : 
                    
             # list1 = [11,10,2,2,33,55,2,44]
             # print(list1.count(2))

                # output : 3


        #  8)  extend()  : concatenate 2 list 
                    #    add element of another list to the current list

                #   example :
                 # list1 = [11, 22, 33, 44]
                 # list2 = [44,55,66]
                 # list1.extend(list2)
                 # print(list1)

        #  9)  len()  : number of element in a list

            # example :

                 # list1 = [11,10,2,2,33,55,2,44]
                 # print(len(list1))


        #  10)  clear() : remove all elements from the list

            # example: 

                  # list1 = [11,10,2,2,33,55,2,44]               
                  # list1.clear()
                  # print(list1)


    # 3.  Dictionary() : 
                    
            # collection data type use to store data in key-value pairs
            # denoted by curly braces {}
            #  syntax : {"key":"value"}
            

              # example :
                # my_dict = {"name":"rahul","age":21,"city":"nashik"}
                #  print(my_dict)  

         # Properties :

                # Mutable – modify
                # Unordered
                # Duplicate- keys:not allow     value:allow
                
         
        #  use function :


            #   1) keys() :return all keys of the dictionary

                #    example :

                 # my_dict = {"name":"rahul","age":21,"city":"nashik"}
                 # print(my_dict.keys())

  
            #  2)values() :return all values

                #   example :
                 
             
                 # my_dict = {"name":"rahul","age":21,"city":"nashik"}
                 # print(my_dict.values())

                            
            #  3)items()  : return both keys and values


                # example :

                 # my_dict = {"name":"rahul","age":21,"city":"nashik"}
                 # print(my_dict.items())


            #  4) update()  : add or update elements

                #  Example :

                  # my_dict = {"name":"rahul","age":21,"city":"nashik"}
                  # my_dict.update({"age":20})
                  # print(my_dict)


            #  5) popitem() : remove last inserted keys value pair

                # example
                  
                   # my_dict = {"name":"rahul","age":21,"city":"nashik"}
                   # print(my_dict.popitem())




    # 4. Set :  
                #  collection data type used to store multiple items in a single variable.
                #  collection of unique elements.
                #  declare as {}

         
            # Properties :

                # Mutable - modify
                # UnOrdered - do not have fix order(changable)
                # Duplicate - not allow
                # Indexed - not supported

        # Operations :

            #  1. Union : Combines two sets.

                  # A = {1,2,3}
                  # B = {3,4,5}

                 # print(A | B)     or

                 # A.union(B)

                       # Output :{1,2,3,4,5}


           # 2. Intersection : Common elements.

              # A = {1,2,3}
              # B = {2,3,4}

              # print(A & B)

              #    Output : {2,3} 


           # 3. Difference : Elements in first set but not second.

             # A = {1,2,3}
             # B = {2,3,4}

             # print(A - B)

                 # Output : {1}


           # 4. Symmetric Difference : Elements not common in both sets.

             # A = {1,2,3}
             # B = {3,4,5}

             # print(A ^ B)

             #   Output : {1,2,4,5}

    # 5. Frozen Set :

                # A frozenset is an immutable set.
                # You cannot add or remove elements.

        #   example:
                    # A = frozenset([1,2,3])
                    #  print(A)



    #  6. Tuple :  
    
                 # is an ordered and immutable collection of elements
               


            # Properties :

                # Immutable – can not modify
                # Ordered
                # Duplicate
                # Indexed


            # 1. len()

                    # Returns the number of elements 
                     # t = (10, 20, 30, 40)
                     # print(len(t))


            # 2. max()

                # Returns the largest element 

               # t = (10, 20, 30, 40)
               # print(max(t))

                     # Output:40


           # 3. min()

                # Returns the smallest element 
                   # t = (10, 20, 30, 40)
                   # print(min(t))

               
           # 4.sum()

                 # Returns the sum of all elements 

                 # t = (10, 20, 30)
                 # print(sum(t))


           # 5. sorted()

                  # Returns the sorted list 

                 # t = (30, 10, 20)
                 # print(sorted(t))

                    # Output :[10, 20, 30]


          # 6. tuple()

                 # Converts other data types into a tuple.

                    # l = [1, 2, 3]
                    # t = tuple(l)
                    # print(t)

                       # Output: (1, 2, 3)




           # 7. count() :

                    # how many times an element appears.

                       # t = (10, 20, 20, 30)
                       # print(t.count(20))

                        # Output :2


           # 8. index() :

                    # Returns the index position of an element.

                      # t = (10, 20, 30)
                      # print(t.index(20))

                         # Output :1


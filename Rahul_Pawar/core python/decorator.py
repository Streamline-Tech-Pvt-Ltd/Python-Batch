#  Decorator:-
#  It is denoted by @ symbol.

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()



def rahul_here(thanks):
    def Welcome():
        print("thank you for watch code")
        thanks()
        print("thank you for watch code")
    return Welcome

@rahul_here
def user():
    print("hello")

user()



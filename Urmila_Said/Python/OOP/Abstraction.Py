# Abstraction: Abstraction means hiding unnecessary implementation details and showing only the essential features to the user.

# abstraction using the abc module (Abstract Base Class).

# Import ABC and abstractmethod
# Create an abstract class
# Create abstract methods
# Inherit the abstract class
# Override all abstract methods

from abc import ABC,abstractmethod

class Streamline_Ai(ABC):
    @abstractmethod
    def chatbox(self):
        pass

    @abstractmethod
    def user_profile(self):
        pass

    @abstractmethod
    def enter_Button(self):
        pass

    @abstractmethod
    def history(self):
        pass

    @abstractmethod
    def setting(self):
        pass

class Urmila(Streamline_Ai):
    def chatbox(self):
        print("the chatbox is created")

    def user_profile(self):
        print("The user profile is created")

    def enter_Button(self):
        print("The enter button is created")

    def history(self):
        print("The History is created")

    def setting(self):
        print("The setting is created")

class Pallavi(Streamline_Ai):
    def chatbox(self,message):
        print("message:",message)

    def user_profile(self,name):
        print("name:",name)

    def enter_Button(self,button):
        print(button,"button is clicked")

    def history(self,history):
        print(history,"history is generated")

    def setting(self,setting):
        print(setting,"open the setting")

U1 = Urmila()
U1.chatbox()
U1.user_profile()

# Import Method                     	Example

# Import entire module	            import math
# Import specific function        	from math import sqrt
# Import multiple functions	        from math import sqrt, factorial
# Import with alias	                import math as m
# Import everything	                from math import *


#  Abstraction :- 

        #    hiding unnnecessary details and showing only important feature of the user
        #     abstraction is mainly acheive using :
                    #  abstract class
                    #  abstract method
        # these create using abc module(Abstract Base Class)
        

#  module :- 

# user module:- 
# 1 website
    # -registration
    # -atttence mark
    # -payment gateway
    # -feedback
    
# Admin module:- 

    #  crud opertaion
    
#  database Module :-


#  example of abstraction :-  
#  CBI,UBI,SBI

# Banking website
#   - registration
#   - Acoount
#   - payment gateways
#   - tracsaction
#   - Services


# abc  ABC 
# @decorator -- it gives additional information to our currect function

# @abstractmethod
from abc import ABC,abstractmethod

# abc file
# ABC
# abstractmethod

class RBI(ABC):
    @abstractmethod
    def registration(self):
        pass
    
    @abstractmethod
    def account(self):
        pass
    
    @abstractmethod
    def payment_gateway(self):
        pass
    
    @abstractmethod
    def transaction(self):
        pass
    
    @abstractmethod
    def services(self):
        pass


class CBI(RBI):
    def registration(self):
        return "Registraion complete.."

    def account(self):
        return "Account created"

    def payment_gateway(self):
        return "Payment done"
    
    def transaction(self):
        return  "Trasaction done"
    
    def services(self):
        return  "Trasaction done"
    
    def ifsc(self):
        return "services offered"
    
class SBI(RBI):
    def registration(self):
        return "Registraion complete.."

    def account(self):
        return "Account created"

    def payment_gateway(self):
        return "Payment done"
    
    def transaction(self):
        return  "Trasaction done"
    
    def services(self):
        return  "Trasaction done"
    
    def ifsc(self):
        return "services offered"
    
class UBI(RBI):
    def registration(self):
        return "Registraion complete.."

    def account(self):
        return "Account created"

    def payment_gateway(self):
        return "Payment done"
    
    def transaction(self):
        return  "Trasaction done"
    
    def services(self):
        return  "Trasaction done"
    
    def ifsc(self):
        return "services offered"
    
obj = CBI()
print(obj.ifsc())
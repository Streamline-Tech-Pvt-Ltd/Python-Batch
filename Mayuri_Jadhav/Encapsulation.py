# class Mobile:

#     def __init__(self):
#         self.__volume = 50

#     def set_volume(self, volume):
#         self.__volume = volume

#     def get_volume(self):
#         return self.__volume


# mobile = Mobile()

# mobile.set_volume(80)       
# print(mobile.get_volume())  

#Q2.getter and setter method 
# Q2. Getter and Setter Method

class mobile:

    def __init__(self):
        self.volume = 50
        self.brightness = 70
        self.battery = 100
        self.color = "black"
        self.model = "samsung"

    def set__volume(self, volume):
        self.volume = volume

    def get__volume(self):
        return self.volume

    def set__brightness(self, brightness):
        self.brightness = brightness

    def get__brightness(self):
        return self.brightness


phone = mobile()

phone.set__volume(80)
print(phone.get__volume())

phone.set__brightness(90)
print(phone.get__brightness())

#absraction  example
from abc import ABC, abstractmethod
class car(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class car:
    def __init__(self):
        self.brand = "Toyota"        # public
        self._speed = 80             # protected
        self.__engine_no = "E12345"  # private

    def show(self): 
        print("Brand:", self.brand)
        print("Speed:", self._speed)
        print("Engine:", self.__engine_no)

    # Getter method
    def get_engine_no(self):
        return self.__engine_no

    # Setter method
    def set_engine_no(self, engine_no):
        self.__engine_no = engine_no

c1 = car()
c1.show()
print("Old Engine:", c1.get_engine_no())
c1.set_engine_no("E67890")
print("New Engine:", c1.get_engine_no())
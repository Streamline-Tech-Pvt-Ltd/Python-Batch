# 1. Example of Single Inheritance in Python:-

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

car = Car()
car.start()  # Inherited from Vehicle
car.drive()  # Defined in Car

# 2. Example of Multiple Inheritance in Python:-
        
class Engine:
    def start_engine(self):
        print("Engine starts")

class Car(Vehicle, Engine):
    def __init__(self):
        super().__init__()
        self.engine = Engine()

car = Car()
car.start()  # Inherited from Vehicle
car.start_engine()  # Inherited from Engine

# Example of Encapsulation in Python:-

class Patient:
    
    def __init__(self, name, doctor_notes, record_no):
        self.name = name                            # Public
        self._doctor_notes = doctor_notes           # Protected
        self.__record_no = record_no                # Private

    def get_record_no(self):                        # Getter
        return self.__record_no

    def set_record_no(self, new_record_no):         # Setter
        if new_record_no > 0:
            self.__record_no = new_record_no
        else:
            print("Invalid record number")

    def display(self):
        print("Patient Name:", self.name)
        print("Doctor Notes:", self._doctor_notes)
        print("Record Number:", self.__record_no)

patient = Patient("Rahul", "Needs regular checkup", 1025)

print(patient.name)                                 # Public
print(patient._doctor_notes)                        # Protected
print(patient.get_record_no())                      # Private → Access through Getter
patient.set_record_no(2050)                         # Private → Modify through Setter
print(patient.get_record_no())
# print("Hello Streamline")
# print("Hello, I am Anuj Kakad")
# a= "Anuj"
# b= "Kakad"
# print(a,b)
# print("Hello, World!")
# print("This is a sample Python script.")
# print("It demonstrates basic print statements.")
# print("You can use print to display text, variables, and more.")
# print("Feel free to modify this script and experiment with Python!")
# print("Goodbye!")
# print("Sampada kakad")
# a= 30
# b= 60
# c= a*b
# print("The product of", a, "and", b, "is:", c)

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
patient.set_record_no(105)                         # Private → Modify through Setter
print(patient.get_record_no())
patient.display()
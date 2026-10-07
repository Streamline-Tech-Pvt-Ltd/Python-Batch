class vehicale:
     def start(self):
           print("vehicale is starting")

     def stop(self):
           print("vehicale is stopped")

     def fuel(self):
           print("vehical needs fuel")

class car(vehical):
     def drive(self):
                 print ("car is driving")

     def horn(self):
            print("car horn is sounding")


c= car()

c.start()
c.stop()
c.fuel()
c.drive()
c.horn()

    
                         
class Vehicle:
    licenseNumber = ""
    serialCode = ""
    face = ""
    def turnOnAirConditionner(self):
        print("Turn On : Air")

class PickUp(Vehicle):
    def brand(self):
        print("PickUp")
class Car(Vehicle):
    def brand(self):
        print("Car")
class Van(Vehicle):
    def brand(self):
        print("Van")
class Estatecar(Vehicle):
    def brand(self):
        print("Estatecar")

pickup1 = PickUp()
pickup1.brand()
pickup1.turnOnAirConditionner()

car1 = Car()
car1.brand()
car1.turnOnAirConditionner()

van1 = Van()
van1.brand()
van1.turnOnAirConditionner()

estareacar1 = Estatecar()
estareacar1.brand()
estareacar1.turnOnAirConditionner()

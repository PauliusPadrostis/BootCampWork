"""
Write a program that would:
* have a class "Car".
* Car class would have parameters: year, make, fuel type
* Car would have methods: drive, stop, refuel which would print "Driving", "Parked", "Refueled".
* Would have a class "Electric car". Its parent class would be Car.
* Electric car class would overwrite the Car's method "refuel" into "Charging".
* Electric car class would overwrite the Car's method "driving" into "Driving autonomously.
"""

class Car:
    def __init__(self, make, year, fuel):
        self.make = make
        self.year = year
        self.fuel = fuel

    def __str__(self):
        return f"Object created: {self.make}, {self.year}, fuel type: {self.fuel} "

    def drive(self):
        print("Driving")

    def stand(self):
        print("Standing")

    def refuel(self):
        print("Refueling")


class Electric(Car):
    def refuel(self):
        print("Charging")

    def autodrive(self):
        print("Driving autonomously")


car1 = Car("BMW", 1990, "Petrol")
ecar1 = Electric("Prius", 2024, "Electricity")

car1.stand()
ecar1.stand()

car1.drive()
ecar1.drive()
ecar1.autodrive()

car1.refuel()
ecar1.refuel()
""" Vehicle → Car Inheritance
Class Vehicle: brand, speed
Class Car: inherits from Vehicle, adds fuel_type
Method to display full info"""
class vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def details(self):
        print(f"Vehicle Details is brand: {self.brand}, speed: {self.speed}km/h")
class car(vehicle):
    def __init__(self, brand, speed,fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type
    def details(self):
        super().details()
        print(f"Car fuel type : {self.fuel_type}")
car1= car("Toyota", 180, "Petrol")
car1.details()
v= vehicle("Honda", 150)
v.details()
class vehicle:
    def __init__(self,name,model):
        self.name = name
        self.model = model
    def display(self):
        print(f"Vehicle Name: {self.name}, Model: {self.model}")
class car(vehicle):
    def horn(self):
        print("Beep Beep! This is a car horn.")
class bike(vehicle):
    def ring(self):
        print("Honk Honk! This is a bike horn.")
c=car("Toyota", "Corolla")
b=bike("Yamaha", "FZ")
b.display()
b.ring()
c.display() 
c.horn()
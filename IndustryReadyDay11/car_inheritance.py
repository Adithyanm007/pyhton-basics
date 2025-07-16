class vehicle:
    def show(self):
        print("This is a vehicle")
class car(vehicle):
    def show(self):
        print("This is a car")
v=vehicle()
v.show()
c=car()
c.show()
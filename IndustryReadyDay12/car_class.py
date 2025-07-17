class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def details(self):
        print(f" Car Details is: brand {self.brand}, model {self.model}, year {self.year}")
car1=car("Toyota", "Corolla", 2020)
car1.details()
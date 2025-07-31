class Animal:
    def speak(self):
        return "Some sound"
class Cat(Animal):
    def speak(self):
        return "Meow"   
class Dog(Animal):
    def speak(self):
        return "Woof"
animal=[Cat(),Dog(),Animal()]
for a in animal:
    print(a.speak())
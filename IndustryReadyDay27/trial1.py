class cat:
    def speak(self):
        return "Meow"
class dog:
    def speak(self):
        return "Woof"
def animal_sound(animal):
    return animal.speak()
d=dog()
c=cat()
print(animal_sound(d))
print(animal_sound(c))
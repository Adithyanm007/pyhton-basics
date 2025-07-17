""" Animal → Dog/Cat
Override methods like speak()"""
class animal:
    
    def speak(self):
        print("Animals do not speak")
class dog(animal):
    def speak(self):
        print("Dog barks")
class cat(animal):
    def speak(self):
        print("Cat meows")
d1=dog()
d1.speak()
c=cat()
c.speak()
a=animal()
a.speak()
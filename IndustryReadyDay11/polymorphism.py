class bird:
    def intro(self):
        print("I am a bird")
    def flight(self):
        print("some birds can fly")
class penguin(bird):
    def flight(self):
        print("Penguins cannot fly")
b=bird()
p=penguin()
b.intro()
b.flight()
p.intro()
p.flight()
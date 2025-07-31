"""Create a base class Shape with method area(). Then define:
Circle (with radius)
Square (with side)
Both should override the area() method.
Test it by looping through objects of both classes and calling .area().
Want help building it? I can walk you through."""
class Shape:
    def area(self):
        return "Area not defined"
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side*self.side
shapes=[Circle(4), Square(8),Shape()]
for a in shapes:
    print(f"Area: {a.area()}")
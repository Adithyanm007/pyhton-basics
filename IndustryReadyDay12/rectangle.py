class rectangle:
    def __init__(self,len,bre):
        self.len=len
        self.bre=bre
    def perimeter(self):
        return 2*(self.len+self.bre)
    def area(self):
        return self.len*self.bre
r=rectangle(10,5)
print(f"The area of rectangle with size {r.len},{r.bre} is {r.area()}")
print(f"The perimeter of rectangle with size {r.len},{r.bre} is {r.perimeter()}")
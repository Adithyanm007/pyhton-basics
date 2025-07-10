class emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary  
    def display(self):
        print(f"The employee {self.name} has a salary of {self.salary}")
class mgr(emp):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def display(self):
        super().display()
        print(f"the manager {self.name} works in the {self.dept} department")
mgr("Jack",120000,"TECH").display()

        